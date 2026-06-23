#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/review_score_calculator.py" --formalization-intensity 0.90 --abstraction-risk 0.92 --representation-risk 0.94 --delegation-level 0.88 --opacity 0.82 --optimization-pressure 0.88 --contestability-need 0.96 --institutional-consequence 0.96 --human-judgment-requirement 0.94 --governance-urgency 0.98 > "$OUT/review_score_smoke.txt"
python3 "$ROOT/calculators/python/formalization_risk_calculator.py" --context-loss 0.8 --label-ambiguity 0.7 --proxy-risk 0.9 --decision-severity 0.95 > "$OUT/formalization_risk_smoke.txt"
python3 "$ROOT/calculators/python/delegation_risk_calculator.py" --decision-severity 0.95 --automation-level 0.95 --opacity 0.80 > "$OUT/delegation_risk_smoke.txt"
python3 "$ROOT/calculators/python/goodhart_pressure_calculator.py" --metric-stakes 0.9 --optimization-pressure 0.95 --proxy-gap 0.8 --monitoring-strength 0.4 > "$OUT/goodhart_pressure_smoke.txt"
python3 "$ROOT/calculators/python/contestability_need_calculator.py" --decision-severity 0.95 --error-impact 0.9 --opacity 0.8 --affected-person-access 0.3 > "$OUT/contestability_need_smoke.txt"
python3 "$ROOT/calculators/python/explanation_fit_calculator.py" --affected-person-fit 0.4 --developer-fit 0.8 --regulator-fit 0.6 --institution-fit 0.7 > "$OUT/explanation_fit_smoke.txt"
python3 "$ROOT/calculators/python/representation_loss_calculator.py" --omitted-context 0.8 --measurement-error 0.5 --proxy-distance 0.7 --temporal-drift 0.4 > "$OUT/representation_loss_smoke.txt"
python3 "$ROOT/calculators/python/ai_output_governance_calculator.py" --claim "AI output is always correct and no human review needed" > "$OUT/ai_output_governance_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/review_score.R" 0.90 0.92 0.94 0.88 0.82 0.88 0.96 0.96 0.94 0.98 > "$OUT/review_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/review_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
