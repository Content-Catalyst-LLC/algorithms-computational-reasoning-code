#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p outputs/logs

if command -v python3 >/dev/null 2>&1; then
  python3 python/uncertainty_quantification_computational_workflows_audit.py > outputs/logs/python_workflow.log
  python3 calculators/python/model_calculator.py --mode ensemble --runs 100 --threshold 0.62 > outputs/logs/python_calculator.log
else
  echo "python3 not found; skipping Python smoke tests." | tee outputs/logs/python_workflow.log
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript r/uncertainty_quantification_computational_workflows_summary.R > outputs/logs/r_workflow.log
  Rscript calculators/r/model_calculator.R ensemble 100 0.62 > outputs/logs/r_calculator.log
else
  echo "Rscript not found; skipping R smoke tests." | tee outputs/logs/r_workflow.log
fi

echo "All available smoke tests complete."
