#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/classification_metrics_calculator.py" \
  --tp 42 --tn 38 --fp 7 --fn 13 > "$OUT/classification_metrics_smoke.txt"

python3 "$ROOT/calculators/python/calibration_gap_calculator.py" \
  --accuracy 0.80 --confidence 0.92 > "$OUT/calibration_gap_smoke.txt"

python3 "$ROOT/calculators/python/benchmark_saturation_calculator.py" \
  --score 0.94 --threshold 0.90 > "$OUT/benchmark_saturation_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/evaluation_risk_score.R" 0.18 0.12 > "$OUT/evaluation_risk_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/evaluation_risk_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
