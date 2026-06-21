#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if command -v python3 >/dev/null 2>&1; then
  python3 python/numerical_methods_algorithmic_approximation_audit.py
else
  echo "python3 not found; skipping Python workflow."
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript r/numerical_methods_algorithmic_approximation_summary.R
else
  echo "Rscript not found; skipping R workflow."
fi

bash calculators/run_calculator_smoke_tests.sh
