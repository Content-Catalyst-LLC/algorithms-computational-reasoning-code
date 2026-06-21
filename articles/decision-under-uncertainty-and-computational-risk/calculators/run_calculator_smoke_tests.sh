#!/usr/bin/env bash
set -euo pipefail
mkdir -p calculators/outputs
python3 calculators/python/expected_value_calculator.py --probability 0.42 --benefit 150 --loss 80 --cost 25 > calculators/outputs/expected_value.txt
python3 calculators/python/threshold_action_calculator.py --risk 0.52 --expected-value 11.5 > calculators/outputs/threshold_action.txt
python3 calculators/python/regret_calculator.py --chosen-value 8.5 --best-value 12.0 > calculators/outputs/regret.txt
python3 calculators/python/risk_score_calculator.py --probability 0.42 --severity 90 --uncertainty 0.15 > calculators/outputs/risk_score.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/expected_value_calculator.R 0.42 150 80 25 > calculators/outputs/r_expected_value.txt
fi
grep -q "expected_value=" calculators/outputs/expected_value.txt
grep -q "action=" calculators/outputs/threshold_action.txt
grep -q "regret=" calculators/outputs/regret.txt
grep -q "risk_score=" calculators/outputs/risk_score.txt
echo "Calculator smoke tests passed."
