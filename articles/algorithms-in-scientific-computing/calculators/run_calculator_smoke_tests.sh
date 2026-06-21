#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

python3 calculators/python/scientific_computing_calculator.py

if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/scientific_computing_calculator.R
else
  echo "Rscript not found; skipping R calculator smoke test."
fi

test -f calculators/outputs/scientific_computing_calculator_results.json
echo "Calculator smoke tests complete."
