#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/procedural_readiness_calculator.py" \
  --due-process 0.58 --transparency 0.52 --human-review 0.60 --appeal-readiness 0.54 > "$OUT/procedural_readiness_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --data-quality 0.66 --vendor-accountability 0.48 --monitoring 0.56 --procedural-readiness 0.56 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/public_algorithmic_risk_calculator.py" \
  --rights-impact 0.94 --governance-readiness 0.565 > "$OUT/public_algorithmic_risk_smoke.txt"

python3 "$ROOT/calculators/python/eligibility_rule_calculator.py" \
  --income 18000 --income-threshold 24000 --documents-complete true --residency-confirmed true > "$OUT/eligibility_rule_smoke.txt"

python3 "$ROOT/calculators/python/public_value_calculator.py" \
  --effectiveness 0.82 --equity 0.74 --accountability 0.70 --harm 0.22 > "$OUT/public_value_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/public_governance_score.R" 0.94 0.58 0.52 0.60 0.66 0.48 0.54 0.56 > "$OUT/public_governance_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/public_governance_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
