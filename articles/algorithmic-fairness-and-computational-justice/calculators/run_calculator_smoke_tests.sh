#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/selection_gap_calculator.py" \
  --rates 0.42 0.31 0.36 > "$OUT/selection_gap_smoke.txt"

python3 "$ROOT/calculators/python/error_rate_calculator.py" \
  --tp 260 \
  --fp 160 \
  --fn 140 \
  --tn 440 > "$OUT/error_rate_smoke.txt"

python3 "$ROOT/calculators/python/calibration_gap_calculator.py" \
  --mean-score 0.61 \
  --observed-rate 0.49 > "$OUT/calibration_gap_smoke.txt"

python3 "$ROOT/calculators/python/justice_capacity_calculator.py" \
  --fairness-evidence 0.78 \
  --measurement-validity 0.58 \
  --contestability 0.44 \
  --remediation 0.42 > "$OUT/justice_capacity_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/fairness_justice_score.R" 420 1000 260 160 140 440 0.62 0.58 0.72 0.66 0.60 > "$OUT/fairness_justice_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/fairness_justice_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
