#!/bin/bash
# Entry point for length sensitivity analysis.
# Usage: bash scripts/length_sensitivity.sh qwen3-max vanilla [--adaptive]

cd "$(dirname "$0")/.."
python -m src.length_analysis.length_sensitivity "$@"
