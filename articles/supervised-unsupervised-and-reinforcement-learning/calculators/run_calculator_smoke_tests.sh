#!/usr/bin/env bash
set -euo pipefail
mkdir -p calculators/outputs
python3 calculators/python/classification_metrics_calculator.py --tp 42 --fp 8 --tn 37 --fn 13 > calculators/outputs/classification_metrics_smoke.txt
python3 calculators/python/generalization_gap_calculator.py --train-metric 0.82 --test-metric 0.74 > calculators/outputs/generalization_gap_smoke.txt
python3 calculators/python/cluster_assignment_calculator.py --x 0.44 --y 0.61 > calculators/outputs/cluster_assignment_smoke.txt
python3 calculators/python/expected_reward_calculator.py --reward-probability 0.54 --reward-value 1 --cost 0.08 > calculators/outputs/expected_reward_smoke.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/classification_metrics_calculator.R 42 8 37 13 > calculators/outputs/r_classification_metrics_smoke.txt
else
  echo "Rscript not found; skipping R calculator smoke test." > calculators/outputs/r_classification_metrics_smoke.txt
fi
echo "Calculator smoke tests passed."
