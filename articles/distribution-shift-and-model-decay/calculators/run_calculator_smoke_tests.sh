#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/performance_decay_calculator.py" \
  --baseline 0.86 \
  --current 0.76 > "$OUT/performance_decay_smoke.txt"

python3 "$ROOT/calculators/python/drift_trigger_calculator.py" \
  --drift 0.31 \
  --threshold 0.25 > "$OUT/drift_trigger_smoke.txt"

python3 "$ROOT/calculators/python/calibration_gap_calculator.py" \
  --accuracy 0.76 \
  --confidence 0.90 > "$OUT/calibration_gap_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/decay_risk_score.R" 0.31 0.16 0.10 0.14 0.15 0.11 > "$OUT/decay_risk_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/decay_risk_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
