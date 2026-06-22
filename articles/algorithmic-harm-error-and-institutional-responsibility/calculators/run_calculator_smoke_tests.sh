#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/harm_risk_calculator.py" \
  --error-likelihood 0.34 \
  --severity 0.92 \
  --exposure 0.78 \
  --contestability 0.42 > "$OUT/harm_risk_smoke.txt"

python3 "$ROOT/calculators/python/responsibility_capacity_calculator.py" \
  --ownership 0.48 \
  --monitoring 0.45 \
  --appeals 0.40 \
  --repair 0.35 \
  --governance 0.50 > "$OUT/responsibility_capacity_smoke.txt"

python3 "$ROOT/calculators/python/remediation_gap_calculator.py" \
  --severity 0.92 \
  --repair 0.35 > "$OUT/remediation_gap_smoke.txt"

python3 "$ROOT/calculators/python/harm_escalation_trigger.py" \
  --harm-risk 0.1411 \
  --responsibility-capacity 0.436 > "$OUT/harm_escalation_trigger_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/harm_responsibility_score.R" 0.34 0.92 0.78 0.42 0.48 0.45 0.40 0.35 0.50 > "$OUT/harm_responsibility_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/harm_responsibility_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
