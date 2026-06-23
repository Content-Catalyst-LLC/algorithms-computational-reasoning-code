#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/mastery_probability_calculator.py" \
  --prior 0.45 --evidence 0.78 --weight 0.60 > "$OUT/mastery_probability_smoke.txt"

python3 "$ROOT/calculators/python/alert_threshold_calculator.py" \
  --risk-score 0.82 --threshold 0.70 > "$OUT/alert_threshold_smoke.txt"

python3 "$ROOT/calculators/python/recommendation_score_calculator.py" \
  --relevance 0.90 --readiness 0.72 --interest 0.80 --support 0.65 > "$OUT/recommendation_score_smoke.txt"

python3 "$ROOT/calculators/python/learning_gain_calculator.py" \
  --pretest 0.52 --posttest 0.78 > "$OUT/learning_gain_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --equity-readiness 0.62 --privacy-readiness 0.72 --pedagogical-validity 0.70 --human-review 0.66 --accessibility-readiness 0.68 --monitoring 0.64 --governance 0.62 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/learning_system_risk_calculator.py" \
  --impact-score 0.82 --equity-readiness 0.62 --pedagogical-validity 0.70 --governance-readiness 0.662857 > "$OUT/learning_system_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/learning_system_score.R" 0.78 0.86 0.62 0.72 0.70 0.66 0.68 0.64 0.62 > "$OUT/learning_system_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/learning_system_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
