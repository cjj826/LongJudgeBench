#!/bin/bash
# Parallel launcher — run multiple dataset × prompt combinations concurrently.
# Self-contained: calls src/evaluation modules directly.
# Uses bash job control (& + wait) for parallelism.
#
# Usage:
#   bash scripts/run_parallel.sh --model deepseek-v4-flash --workers 4
#   bash scripts/run_parallel.sh --model gpt-4o-mini --model glm-5.1 --workers 6
#   bash scripts/run_parallel.sh --model qwen3-32b --dataset ma,surge
#   bash scripts/run_parallel.sh --model qwen3-32b --prompt vanilla

PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

# ── Defaults ──
MODELS=()
DATASET_FILTER=""
PROMPT_FILTER=""
WORKERS=4

# Parse args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --model) MODELS+=("$2"); shift 2 ;;
        --dataset) DATASET_FILTER="$2"; shift 2 ;;
        --prompt) PROMPT_FILTER="$2"; shift 2 ;;
        --workers) WORKERS="$2"; shift 2 ;;
        *) echo "Unknown: $1"; exit 1 ;;
    esac
done
if [[ ${#MODELS[@]} -eq 0 ]]; then
    echo "Error: --model is required"
    echo "Usage: run_parallel.sh --model NAME [--model NAME ...] [--workers N]"
    exit 1
fi

# ── Dataset definitions ──
DATASETS=(
    "deepresearch_bench pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "realdr pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "verify_bench_hard pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "wp_bench pairwise vanilla,vanilla_rubric"
    "ma pairwise insights_vanilla,insights_vanilla_rubric,insights_vanilla_reference,insights_vanilla_rubric_reference"
    "surge listwise structure_vanilla,structure_vanilla_rubric,structure_vanilla_reference,structure_vanilla_rubric_reference,content_vanilla,content_vanilla_rubric,content_vanilla_reference,content_vanilla_rubric_reference"
)

# ── Build task list ──
TASKS=()
for model in "${MODELS[@]}"; do
    for entry in "${DATASETS[@]}"; do
        read -r ds paradigm prompt_csv <<< "$entry"
        [[ -n "$DATASET_FILTER" ]] && { IFS=',' read -ra dfs <<< "$DATASET_FILTER"; found=false; for d in "${dfs[@]}"; do [[ "$d" == "$ds" ]] && found=true; done; $found || continue; }
        IFS=',' read -ra prompts <<< "$prompt_csv"
        for pm in "${prompts[@]}"; do
            [[ -n "$PROMPT_FILTER" && "$pm" != "$PROMPT_FILTER" ]] && continue
            TASKS+=("$ds|$paradigm|$pm|$model")
        done
    done
done

total=${#TASKS[@]}
echo "======================================="
echo " Parallel Launcher"
echo " Models:  ${MODELS[*]}"
echo " Workers: $WORKERS"
echo " Tasks:   $total"
echo "======================================="

# ── Run function ──
run_task() {
    local entry="$1"
    IFS='|' read -r ds paradigm pm model <<< "$entry"
    metric_file="$BASE_DIR/outputs/reliability_scores/$model/$ds/$pm.json"
    judge_file="$BASE_DIR/outputs/judge_results/$model/$ds/$pm.jsonl"

    if [[ -f "$metric_file" && -s "$metric_file" ]]; then
        echo "  [OK] $ds/$pm/$model"
        return 0
    fi

    if [[ ! -f "$judge_file" || ! -s "$judge_file" ]]; then
        echo "  [JUDGE] $ds/$pm/$model"
        mkdir -p "$(dirname "$judge_file")"
        "$PYTHON" "$BASE_DIR/src/evaluation/run_judge.py" "$ds" "$paradigm" "$model" --prompt "$pm" --workers 4 > /dev/null 2>&1
    fi

    if [[ -f "$judge_file" && -s "$judge_file" ]]; then
        echo "  [METRICS] $ds/$pm/$model"
        mkdir -p "$(dirname "$metric_file")"
        "$PYTHON" "$BASE_DIR/src/evaluation/compute_reliability.py" "$ds" "$paradigm" "$model" --prompt "$pm" > /dev/null 2>&1
    fi
    echo "  [DONE] $ds/$pm/$model"
}

# ── Parallel dispatch ──
running=0
completed=0
declare -A job_task

_next_task_index=0
for ((i=0; i<total; i++)); do
    # Wait if at worker limit
    while [[ "$(jobs -r | wc -l)" -ge "$WORKERS" ]]; do
        sleep 2
    done

    run_task "${TASKS[$i]}" &
    job_task[$!]="${TASKS[$i]}"
    completed=$((completed + 1))
    echo "  → [$completed/$total] ${TASKS[$i]}"
done

wait
echo ""
echo "All done! ($total tasks)"
