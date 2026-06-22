#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/explanation_quality_calculator.py" \
  --faithfulness 0.70 \
  --stability 0.74 \
  --understandability 0.62 \
  --actionability 0.58 \
  --uncertainty 0.46 > "$OUT/explanation_quality_smoke.txt"

python3 "$ROOT/calculators/python/transparency_capacity_calculator.py" \
  --documentation 0.68 \
  --governance 0.60 \
  --uncertainty 0.46 > "$OUT/transparency_capacity_smoke.txt"

python3 "$ROOT/calculators/python/accountability_capacity_calculator.py" \
  --explanation-quality 0.62 \
  --transparency-capacity 0.58 \
  --contestability 0.55 \
  --governance 0.60 > "$OUT/accountability_capacity_smoke.txt"

python3 "$ROOT/calculators/python/explanation_risk_calculator.py" \
  --stakes 0.88 \
  --accountability-capacity 0.5875 > "$OUT/explanation_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/explanation_audit_score.R" 0.70 0.74 0.62 0.58 0.46 0.68 0.55 0.60 0.88 > "$OUT/explanation_audit_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/explanation_audit_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
