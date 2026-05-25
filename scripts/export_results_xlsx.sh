#!/bin/bash
# Export reliability results to xlsx.
# Usage:
#   bash scripts/export_results_xlsx.sh
#   bash scripts/export_results_xlsx.sh outputs/my_summary.xlsx
#   bash scripts/export_results_xlsx.sh --models gpt-4o-mini qwen3-32b

PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

"$PYTHON" "$BASE_DIR/src/evaluation/export_results_xlsx.py" "$@"
