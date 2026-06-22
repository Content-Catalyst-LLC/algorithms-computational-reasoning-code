#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/documentation_completeness_calculator.py" \
  --completed-fields 11 \
  --required-fields 16 > "$OUT/documentation_completeness_smoke.txt"

python3 "$ROOT/calculators/python/documentation_quality_calculator.py" \
  --accuracy 0.62 \
  --completeness 0.6875 \
  --specificity 0.58 \
  --timeliness 0.50 \
  --accessibility 0.56 \
  --actionability 0.52 > "$OUT/documentation_quality_smoke.txt"

python3 "$ROOT/calculators/python/documentation_risk_calculator.py" \
  --stakes 0.92 \
  --documentation-quality 0.577917 > "$OUT/documentation_risk_smoke.txt"

python3 "$ROOT/calculators/python/freshness_calculator.py" \
  --days-since-update 45 \
  --required-review-interval 90 > "$OUT/freshness_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/documentation_score.R" 16 11 0.62 0.58 0.50 0.56 0.52 1 1 1 0 1 0.92 > "$OUT/documentation_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/documentation_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
