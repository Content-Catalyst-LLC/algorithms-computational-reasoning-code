#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/proxy_gap_calculator.py" \
  --alignment 0.62 > "$OUT/proxy_gap_smoke.txt"

python3 "$ROOT/calculators/python/goodhart_risk_calculator.py" \
  --proxy-gap 0.38 \
  --pressure 0.88 \
  --gaming-risk 0.72 \
  --guardrails 1 > "$OUT/goodhart_risk_smoke.txt"

python3 "$ROOT/calculators/python/guardrail_sufficiency_calculator.py" \
  --guardrails 1 \
  --minimum 2 > "$OUT/guardrail_sufficiency_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/metric_pressure_score.R" 0.88 0.72 > "$OUT/metric_pressure_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/metric_pressure_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
