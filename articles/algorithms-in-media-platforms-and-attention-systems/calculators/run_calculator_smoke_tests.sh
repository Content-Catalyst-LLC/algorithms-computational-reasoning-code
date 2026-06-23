#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/ranking_score_calculator.py" \
  --relevance 0.82 --engagement 0.90 --freshness 0.72 --risk 0.28 > "$OUT/ranking_score_smoke.txt"

python3 "$ROOT/calculators/python/engagement_probability_calculator.py" \
  --linear-score 1.25 > "$OUT/engagement_probability_smoke.txt"

python3 "$ROOT/calculators/python/attention_risk_calculator.py" \
  --engagement-pressure 0.92 --creator-impact 0.88 --public-knowledge-impact 0.78 --user-control 0.44 --contestability 0.42 > "$OUT/attention_risk_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --transparency 0.48 --contestability 0.42 --moderation-readiness 0.66 --user-control 0.44 --governance 0.54 --monitoring 0.60 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/platform_risk_calculator.py" \
  --attention-risk 0.744 --governance-readiness 0.523333 > "$OUT/platform_risk_smoke.txt"

python3 "$ROOT/calculators/python/moderation_threshold_calculator.py" \
  --harm-score 0.62 --review-threshold 0.50 --remove-threshold 0.85 > "$OUT/moderation_threshold_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/attention_system_score.R" 0.92 0.48 0.42 0.66 0.88 0.78 0.44 0.54 0.60 > "$OUT/attention_system_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/attention_system_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
