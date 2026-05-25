#!/bin/bash
# Entry point for exporting length sensitivity results to xlsx.
# Usage: bash scripts/export_length_sensitivity.sh

cd "$(dirname "$0")/.."
python -m src.length_analysis.export_length_sensitivity "$@"
