#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

printf '==> Running calculator smoke tests for Numerical Methods and Algorithmic Approximation\n'

if command -v python3 >/dev/null 2>&1; then
  python3 calculators/python/model_calculator.py > calculators/outputs/python_calculator_stdout.txt
else
  printf 'python3 not found; skipping Python calculator.\n'
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/model_calculator.R > calculators/outputs/r_calculator_stdout.txt
else
  printf 'Rscript not found; skipping R calculator.\n'
fi

printf '==> Calculator smoke tests complete.\n'
