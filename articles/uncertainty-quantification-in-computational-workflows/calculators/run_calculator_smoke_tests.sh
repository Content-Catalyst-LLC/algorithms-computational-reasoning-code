#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p calculators/outputs

if command -v python3 >/dev/null 2>&1; then
  python3 calculators/python/model_calculator.py --mode ensemble --runs 100 --threshold 0.62 > calculators/outputs/python_calculator_stdout.txt
else
  echo "python3 not found; skipping Python calculator smoke test." > calculators/outputs/python_calculator_stdout.txt
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/model_calculator.R ensemble 100 0.62 > calculators/outputs/r_calculator_stdout.txt
else
  echo "Rscript not found; skipping R calculator smoke test." > calculators/outputs/r_calculator_stdout.txt
fi

echo "Calculator smoke tests complete."
