#!/usr/bin/env bash
set -euo pipefail

ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ARTICLE_DIR"

printf '\n==> Running Python reproducible workflow audit\n'
python3 python/computational_experiments_reproducible_workflows_audit.py

if command -v Rscript >/dev/null 2>&1; then
  printf '\n==> Running R workflow summary\n'
  Rscript r/computational_experiments_reproducible_workflows_summary.R
else
  printf '\n==> Rscript not found; skipping R summary.\n'
fi

printf '\n==> Running Python calculator smoke test\n'
python3 calculators/python/workflow_calculator.py --std-dev 10 --samples 1000 > outputs/json/python_calculator_smoke_test.json

if command -v Rscript >/dev/null 2>&1; then
  printf '\n==> Running R calculator smoke test\n'
  Rscript calculators/r/workflow_calculator.R > outputs/logs/r_calculator_smoke_test.log
fi

printf '\n==> Article workflows complete.\n'
