#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/overreliance_gap_calculator.py" \
  --acceptance 0.93 \
  --quality 0.71 > "$OUT/overreliance_gap_smoke.txt"

python3 "$ROOT/calculators/python/trust_calibration_calculator.py" \
  --reliance 0.93 \
  --quality 0.71 > "$OUT/trust_calibration_smoke.txt"

python3 "$ROOT/calculators/python/oversight_risk_calculator.py" \
  --acceptance 0.93 \
  --quality 0.71 \
  --uncertainty 0.29 \
  --review-time 0.7 \
  --override-friction 0.72 \
  --appeal-pathway 1 > "$OUT/oversight_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/reliance_quality_gap.R" 0.93 0.71 > "$OUT/reliance_quality_gap_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/reliance_quality_gap_smoke.txt"
fi

echo "Calculator smoke tests complete."
