#!/bin/bash
# Export reliability results to xlsx.
# Self-contained: calls the compute pipeline's JSON output and generates an Excel summary.
#
# Usage:
#   bash scripts/export_results_xlsx.sh                                          # default path
#   bash scripts/export_results_xlsx.sh outputs/my_summary.xlsx                   # custom path
#   bash scripts/export_results_xlsx.sh outputs/summary.xlsx --models gpt-4o-mini

PYTHON=${PYTHON:-python3}
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

if [[ "$1" == "--models" || "$1" == "" ]]; then
    "$PYTHON" "$SCRIPT_DIR/export_results_xlsx.py" "$@"
else
    OUTPUT="${1:-$BASE_DIR/outputs/reliability_summary.xlsx}"
    shift 2>/dev/null || true
    "$PYTHON" "$SCRIPT_DIR/export_results_xlsx.py" "$OUTPUT" "$@"
fi
