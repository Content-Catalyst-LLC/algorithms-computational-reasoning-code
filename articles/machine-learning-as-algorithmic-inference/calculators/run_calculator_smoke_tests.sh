#!/usr/bin/env bash
set -euo pipefail
mkdir -p calculators/outputs
python3 calculators/python/threshold_confusion_calculator.py --tp 80 --fp 25 --tn 140 --fn 35 > calculators/outputs/threshold_confusion_smoke.txt
python3 calculators/python/expected_prediction_value_calculator.py --score 0.72 --benefit 10 --harm 4 > calculators/outputs/expected_prediction_value_smoke.txt
python3 calculators/python/train_test_gap_calculator.py --train-metric 0.84 --test-metric 0.76 > calculators/outputs/train_test_gap_smoke.txt
python3 calculators/python/calibration_gap_calculator.py --average-score 0.62 --observed-rate 0.55 > calculators/outputs/calibration_gap_smoke.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/threshold_confusion_calculator.R 80 25 140 35 > calculators/outputs/r_threshold_confusion_smoke.txt
fi
echo "Calculator smoke tests passed."
