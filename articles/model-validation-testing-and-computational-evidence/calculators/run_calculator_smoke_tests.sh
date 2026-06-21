#!/usr/bin/env bash
set -Eeuo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/calculators/outputs"
mkdir -p "$OUT_DIR"

if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT_DIR/calculators/python/model_calculator.py" > "$OUT_DIR/python_calculator_output.txt"
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT_DIR/calculators/r/model_calculator.R" > "$OUT_DIR/r_calculator_output.txt"
fi

echo "calculator smoke tests complete"
