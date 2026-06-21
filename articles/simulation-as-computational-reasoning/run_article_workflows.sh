#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
python3 python/simulation_as_computational_reasoning_audit.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript r/simulation_as_computational_reasoning_summary.R
else
  echo "Rscript not found; skipping R summary."
fi
python3 calculators/python/simulation_calculator.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/simulation_calculator.R
fi
