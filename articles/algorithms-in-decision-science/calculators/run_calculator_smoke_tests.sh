#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/expected_value_calculator.py" \
  --probability 0.82 \
  --benefit-if-act 0.88 \
  --cost-if-act 0.30 > "$OUT/expected_value_smoke.txt"

python3 "$ROOT/calculators/python/expected_loss_calculator.py" \
  --probability 0.82 \
  --loss-if-miss 0.92 > "$OUT/expected_loss_smoke.txt"

python3 "$ROOT/calculators/python/threshold_action_calculator.py" \
  --score 0.82 \
  --threshold 0.70 > "$OUT/threshold_action_smoke.txt"

python3 "$ROOT/calculators/python/decision_readiness_calculator.py" \
  --calibration 0.78 \
  --uncertainty-communication 0.74 \
  --human-review 0.82 \
  --contestability 0.70 \
  --governance 0.76 > "$OUT/decision_readiness_smoke.txt"

python3 "$ROOT/calculators/python/multi_criteria_score_calculator.py" \
  --effectiveness 0.82 \
  --equity 0.70 \
  --feasibility 0.78 \
  --reversibility 0.66 \
  --legitimacy 0.74 > "$OUT/multi_criteria_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/decision_score.R" 0.82 0.88 0.30 0.92 0.78 0.74 0.82 0.70 0.76 0.70 > "$OUT/decision_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/decision_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
