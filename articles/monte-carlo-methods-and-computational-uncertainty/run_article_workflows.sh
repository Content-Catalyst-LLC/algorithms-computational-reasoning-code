#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
python3 python/monte_carlo_methods_computational_uncertainty_audit.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript r/monte_carlo_methods_computational_uncertainty_summary.R
else
  echo "Rscript not found; skipping R summary workflow."
fi
bash calculators/run_calculator_smoke_tests.sh
