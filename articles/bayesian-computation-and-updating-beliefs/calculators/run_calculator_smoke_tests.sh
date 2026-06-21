#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT_DIR/calculators/outputs"
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT_DIR/calculators/python/bayesian_calculator.py" --alpha 2 --beta 2 --successes 113 --failures 72 --threshold 0.60 --output "$ROOT_DIR/calculators/outputs/python_bayesian_calculator_output.json"
else
  echo "python3 not found; skipping Python calculator."
fi
if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT_DIR/calculators/r/bayesian_calculator.R" --alpha=2 --beta=2 --successes=113 --failures=72 --threshold=0.60
else
  echo "Rscript not found; skipping R calculator."
fi
