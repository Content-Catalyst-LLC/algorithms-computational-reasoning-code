#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/feedback_risk_calculator.py" \
  --amplification 0.82 \
  --concentration 0.76 \
  --intervention 0.44 \
  --drift 0.28 \
  --recursive-data 0.31 > "$OUT/feedback_risk_smoke.txt"

python3 "$ROOT/calculators/python/drift_trigger_calculator.py" \
  --distance 0.34 \
  --threshold 0.25 > "$OUT/drift_trigger_smoke.txt"

python3 "$ROOT/calculators/python/amplification_factor_calculator.py" \
  --factor 1.18 > "$OUT/amplification_factor_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/feedback_pressure_score.R" 0.82 0.76 > "$OUT/feedback_pressure_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/feedback_pressure_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
