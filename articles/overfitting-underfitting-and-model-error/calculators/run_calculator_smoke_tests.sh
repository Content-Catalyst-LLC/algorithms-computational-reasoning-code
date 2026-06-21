#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
mkdir -p calculators/outputs
python3 calculators/python/generalization_gap_calculator.py --train-error 0.04 --test-error 0.09 > calculators/outputs/generalization_gap_smoke.txt
python3 calculators/python/bias_variance_error_calculator.py --bias 0.20 --variance 0.04 --irreducible 0.02 > calculators/outputs/bias_variance_smoke.txt
python3 calculators/python/regularization_review_calculator.py --unregularized-test-error 0.13 --regularized-test-error 0.09 > calculators/outputs/regularization_review_smoke.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/model_error_calculator.R 0.04 0.09 > calculators/outputs/r_model_error_smoke.txt
else
  echo "Rscript not available; skipped R calculator." > calculators/outputs/r_model_error_smoke.txt
fi
echo "calculator smoke tests complete"
