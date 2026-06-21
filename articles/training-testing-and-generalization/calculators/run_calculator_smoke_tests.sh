#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
python3 calculators/python/train_test_split_calculator.py --n 1000 --train 0.7 --validation 0.15 > calculators/outputs/train_test_split_example.txt
python3 calculators/python/generalization_gap_calculator.py --train-metric 0.88 --test-metric 0.81 --higher-is-better > calculators/outputs/generalization_gap_example.txt
python3 calculators/python/confusion_metrics_calculator.py --tp 45 --tn 38 --fp 9 --fn 8 > calculators/outputs/confusion_metrics_example.txt
python3 calculators/python/cross_validation_summary_calculator.py --scores 0.81,0.79,0.83,0.80,0.82 > calculators/outputs/cross_validation_summary_example.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/generalization_gap_calculator.R 0.88 0.81 > calculators/outputs/r_generalization_gap_example.txt
else
  echo "Rscript not available; skipped R calculator." > calculators/outputs/r_generalization_gap_example.txt
fi
echo "Calculator smoke tests complete."
