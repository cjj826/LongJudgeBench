#!/bin/bash
# Run full experiment — iterate all dataset × prompt combinations for given models.
# Self-contained: calls src/evaluation/run_judge.py and compute_reliability.py directly.
#
# Usage:
#   bash scripts/run_all.sh                                          # default models
#   bash scripts/run_all.sh --model gpt-4o-mini                      # single model
#   bash scripts/run_all.sh --model qwen3-32b --model deepseek-v4-flash  # multiple
#   bash scripts/run_all.sh --model qwen3-32b --prompt vanilla       # specific prompt
#
# Checks reliability_scores/ for completion — re-run is safe.

PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

# ── Available models (overridable via --model) ──
DEFAULT_MODELS=("qwen3-32b" "qwen3-32b-nothinking" "deepseek-v4-flash")
MODELS=()
PROMPT_FILTER=""

# Parse args
while [[ $# -gt 0 ]]; do
    case "$1" in
        --model) MODELS+=("$2"); shift 2 ;;
        --prompt) PROMPT_FILTER="$2"; shift 2 ;;
        *) echo "Unknown: $1"; exit 1 ;;
    esac
done
[[ ${#MODELS[@]} -eq 0 ]] && MODELS=("${DEFAULT_MODELS[@]}")

# ── Dataset definitions: (name paradigm prompt_list) ──
DATASETS=(
    "deepresearch_bench pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "realdr pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "verify_bench_hard pointwise vanilla,vanilla_reference,vanilla_rubric,vanilla_rubric_reference"
    "wp_bench pairwise vanilla,vanilla_rubric"
    "ma pairwise insights_vanilla,insights_vanilla_rubric,insights_vanilla_reference,insights_vanilla_rubric_reference,structure_vanilla,structure_vanilla_rubric,structure_vanilla_reference,structure_vanilla_rubric_reference"
    "surge listwise structure_vanilla,structure_vanilla_rubric,structure_vanilla_reference,structure_vanilla_rubric_reference,content_vanilla,content_vanilla_rubric,content_vanilla_reference,content_vanilla_rubric_reference"
)

echo "======================================="
echo " LongJudgeBench — Full Experiment"
echo " Models:  ${MODELS[*]}"
echo "======================================="
echo ""

for model in "${MODELS[@]}"; do
    for entry in "${DATASETS[@]}"; do
        read -r ds paradigm prompt_csv <<< "$entry"
        IFS=',' read -ra prompts <<< "$prompt_csv"

        for pm in "${prompts[@]}"; do
            [[ -n "$PROMPT_FILTER" && "$pm" != "$PROMPT_FILTER" ]] && continue

            metric_file="$BASE_DIR/outputs/reliability_scores/$model/$ds/$pm.json"
            judge_file="$BASE_DIR/outputs/judge_results/$model/$ds/$pm.jsonl"

            # ── Check if metrics already exist → skip ──
            if [[ -f "$metric_file" && -s "$metric_file" ]]; then
                echo "  [OK] $ds / $pm / $model  (metrics exist, skipping)"
                continue
            fi

            # ── Judge phase ──
            judge_done=false
            if [[ -f "$judge_file" && -s "$judge_file" ]]; then
                # File exists, only run metrics
                echo "  [METRICS] $ds / $pm / $model"
            else
                echo "  [JUDGE] $ds / $pm / $model"
                mkdir -p "$(dirname "$judge_file")"
                "$PYTHON" "$BASE_DIR/src/evaluation/run_judge.py" "$ds" "$paradigm" "$model" --prompt "$pm" --workers 4
                if [[ -f "$judge_file" && -s "$judge_file" ]]; then
                    judge_done=true
                fi
            fi

            # ── Metrics phase ──
            if [[ -f "$judge_file" && -s "$judge_file" ]]; then
                echo "  [METRICS] $ds / $pm / $model"
                mkdir -p "$(dirname "$metric_file")"
                "$PYTHON" "$BASE_DIR/src/evaluation/compute_reliability.py" "$ds" "$paradigm" "$model" --prompt "$pm"
            fi
        done
    done
done

echo ""
echo "Done!"
