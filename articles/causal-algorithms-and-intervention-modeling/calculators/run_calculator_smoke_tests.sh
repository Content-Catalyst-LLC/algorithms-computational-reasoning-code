#!/usr/bin/env bash
set -euo pipefail
mkdir -p calculators/outputs
python3 calculators/python/intervention_effect_calculator.py --baseline-outcome 0.42 --intervention-outcome 0.57 > calculators/outputs/intervention_effect_smoke.txt
python3 calculators/python/net_benefit_calculator.py --effect 0.14 --implementation-cost 0.20 --governance-risk 0.08 > calculators/outputs/net_benefit_smoke.txt
python3 calculators/python/threshold_policy_calculator.py --score 0.53 --baseline-threshold 0.55 --new-threshold 0.50 > calculators/outputs/threshold_policy_smoke.txt
python3 calculators/python/weighted_policy_score_calculator.py --effect 0.18 --equity 0.60 --feasibility 0.70 --cost 0.25 > calculators/outputs/weighted_policy_score_smoke.txt
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/intervention_effect_calculator.R 0.42 0.57 > calculators/outputs/r_intervention_effect_smoke.txt
else
  echo "Rscript not available; skipped R calculator smoke test." > calculators/outputs/r_intervention_effect_smoke.txt
fi
echo "calculator smoke tests complete" > calculators/outputs/calculator_smoke_summary.txt
cat calculators/outputs/calculator_smoke_summary.txt
