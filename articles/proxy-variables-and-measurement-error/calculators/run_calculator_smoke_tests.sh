#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/proxy_validity_gap_calculator.py" \
  --validity 0.58 > "$OUT/proxy_validity_gap_smoke.txt"

python3 "$ROOT/calculators/python/measurement_risk_calculator.py" \
  --validity-gap 0.42 \
  --missingness 0.12 \
  --differential-error 0.24 \
  --label-error 0.08 > "$OUT/measurement_risk_smoke.txt"

python3 "$ROOT/calculators/python/misclassification_rates_calculator.py" \
  --tp 44 \
  --tn 39 \
  --fp 8 \
  --fn 9 > "$OUT/misclassification_rates_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/attenuation_factor.R" 1.0 0.25 > "$OUT/attenuation_factor_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/attenuation_factor_smoke.txt"
fi

echo "Calculator smoke tests complete."
