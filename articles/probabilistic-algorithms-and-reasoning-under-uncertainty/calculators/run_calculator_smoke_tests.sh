#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/calculators/python/model_calculator.py" > "$OUT/python_probability_calculator_output.json"
  echo "Python calculator smoke test wrote $OUT/python_probability_calculator_output.json"
else
  echo "python3 not found; skipping Python calculator smoke test"
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/model_calculator.R" > "$OUT/r_probability_calculator_output.txt"
  echo "R calculator smoke test wrote $OUT/r_probability_calculator_output.txt"
else
  echo "Rscript not found; skipping R calculator smoke test"
fi
