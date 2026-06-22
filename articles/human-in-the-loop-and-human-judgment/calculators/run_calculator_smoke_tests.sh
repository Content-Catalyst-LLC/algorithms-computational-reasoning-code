#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/review_capacity_calculator.py" \
  --time 0.56 \
  --information 0.62 \
  --authority 0.58 \
  --training 0.60 \
  --protection 0.48 > "$OUT/review_capacity_smoke.txt"

python3 "$ROOT/calculators/python/reliance_calculator.py" \
  --accepted-recommendations 920 \
  --total-recommendations 1000 > "$OUT/reliance_smoke.txt"

python3 "$ROOT/calculators/python/override_rate_calculator.py" \
  --overrides 18 \
  --reviewed-cases 1000 > "$OUT/override_rate_smoke.txt"

python3 "$ROOT/calculators/python/review_risk_calculator.py" \
  --stakes 0.88 \
  --judgment-capacity 0.555 > "$OUT/review_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/human_review_score.R" 0.56 0.62 0.58 0.60 0.48 920 1000 18 1000 0.54 0.52 0.60 0.88 > "$OUT/human_review_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/human_review_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
