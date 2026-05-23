#!/bin/bash
# LLM-as-Judge evaluation script
# Usage: run_judge.sh <dataset> <paradigm> <model> [--prompt MODE] [--workers N] [--max-records N]
#   Checkpoint resume built-in — automatically skips completed results
#
# Arguments:
#   dataset   Dataset name (deepresearch_bench / realdr / surge / wp_bench)
#   paradigm  Judge paradigm (pointwise / pairwise / listwise)
#   model     Judge model (e.g. gpt-4o-mini)
#   --prompt  Prompt mode (default: vanilla)
#
# Examples:
#   bash scripts/run_judge.sh deepresearch_bench pointwise gpt-4o-mini --prompt vanilla
#   bash scripts/run_judge.sh realdr pointwise gpt-4o-mini --workers 8
#   bash scripts/run_judge.sh surge listwise gpt-4o-mini --max-records 5

PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

DATASET=${1:?Usage: run_judge.sh <dataset> <paradigm> <model> [--prompt MODE] [--workers N] [--max-records N]}
PARADIGM=${2:?Missing paradigm argument (pointwise/pairwise/listwise)}
MODEL=${3:?Missing model argument}
shift 3 2>/dev/null || true

# Filter out legacy --resume flag (checkpoint resume is built-in)
FILTERED_ARGS=()
for arg in "$@"; do
    [ "$arg" = "--resume" ] && continue
    FILTERED_ARGS+=("$arg")
done
set -- "${FILTERED_ARGS[@]}"

echo "========================================"
echo "LLM-as-Judge Evaluation"
echo "  Dataset:   $DATASET"
echo "  Paradigm:  $PARADIGM"
echo "  Model:     $MODEL"
echo "========================================"

"$PYTHON" "$SCRIPT_DIR/../src/evaluation/run_judge.py" "$DATASET" "$PARADIGM" "$MODEL" "$@"
