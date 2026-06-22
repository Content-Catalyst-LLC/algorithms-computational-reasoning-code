#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/delegation_readiness_calculator.py" \
  --evidence-quality 0.62 \
  --validation 0.58 \
  --reversibility 0.46 \
  --contestability 0.52 \
  --governance 0.60 \
  --human-review 0.58 > "$OUT/delegation_readiness_smoke.txt"

python3 "$ROOT/calculators/python/delegation_risk_calculator.py" \
  --stakes 0.92 \
  --delegation-readiness 0.56 > "$OUT/delegation_risk_smoke.txt"

python3 "$ROOT/calculators/python/automation_reliance_calculator.py" \
  --automated-final-actions 760 \
  --total-decisions 1000 > "$OUT/automation_reliance_smoke.txt"

python3 "$ROOT/calculators/python/reversibility_calculator.py" \
  --detection 0.50 \
  --correction 0.45 \
  --remedy 0.40 \
  --recurrence-prevention 0.49 > "$OUT/reversibility_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/delegation_score.R" 0.62 0.58 0.46 0.52 0.60 0.58 760 1000 0.92 > "$OUT/delegation_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/delegation_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
