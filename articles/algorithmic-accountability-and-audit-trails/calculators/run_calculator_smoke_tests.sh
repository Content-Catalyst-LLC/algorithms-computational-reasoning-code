#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/audit_completeness_calculator.py" \
  --required-records 12 \
  --available-records 9 > "$OUT/audit_completeness_smoke.txt"

python3 "$ROOT/calculators/python/accountability_capacity_calculator.py" \
  --documentation 0.72 \
  --provenance 0.68 \
  --reviewability 0.64 \
  --contestability 0.58 \
  --remediation 0.52 \
  --governance 0.66 > "$OUT/accountability_capacity_smoke.txt"

python3 "$ROOT/calculators/python/reconstruction_risk_calculator.py" \
  --stakes 0.90 \
  --audit-completeness 0.75 > "$OUT/reconstruction_risk_smoke.txt"

python3 "$ROOT/calculators/python/incident_recurrence_calculator.py" \
  --repeat-incidents 3 \
  --total-incidents 12 > "$OUT/incident_recurrence_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/accountability_score.R" 12 9 0.72 0.68 0.64 0.58 0.52 0.66 0.90 > "$OUT/accountability_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/accountability_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
