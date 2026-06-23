#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/table_lookup_calculator.py" \
  --argument 20 > "$OUT/table_lookup_smoke.txt"

python3 "$ROOT/calculators/python/linear_interpolation_calculator.py" \
  --x0 10 --y0 1.2 --x1 20 --y1 2.8 --x 15 > "$OUT/linear_interpolation_smoke.txt"

python3 "$ROOT/calculators/python/mean_plus_correction_calculator.py" \
  --mean-value 12.5 --correction -0.3 > "$OUT/mean_plus_correction_smoke.txt"

python3 "$ROOT/calculators/python/cycle_next_date_calculator.py" \
  --date 100 --cycle-length 29.5 --adjustment 0.2 > "$OUT/cycle_next_date_smoke.txt"

python3 "$ROOT/calculators/python/calendar_offset_calculator.py" \
  --start-day 100 --end-day 365 > "$OUT/calendar_offset_smoke.txt"

python3 "$ROOT/calculators/python/prediction_error_calculator.py" \
  --predicted 12.2 --observed 12.4 > "$OUT/prediction_error_smoke.txt"

python3 "$ROOT/calculators/python/prediction_score_calculator.py" \
  --table-structure 0.98 --procedural-clarity 0.90 --predictive-function 0.92 --institutional-use 0.86 --correction-awareness 0.86 --transmission-importance 0.90 --modern-resonance 0.94 > "$OUT/prediction_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/prediction_score.R" 0.98 0.90 0.92 0.86 0.86 0.90 0.94 > "$OUT/prediction_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/prediction_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
