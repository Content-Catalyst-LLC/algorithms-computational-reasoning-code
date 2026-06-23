#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/place_value_calculator.py" \
  --digit 7 --base 10 --position 3 > "$OUT/place_value_smoke.txt"

python3 "$ROOT/calculators/python/algebra_balance_calculator.py" \
  --left 5 --right 9 --add 3 > "$OUT/algebra_balance_smoke.txt"

python3 "$ROOT/calculators/python/table_interpolation_calculator.py" \
  --x0 10 --y0 100 --x1 20 --y1 140 --x 15 > "$OUT/table_interpolation_smoke.txt"

python3 "$ROOT/calculators/python/frequency_distance_calculator.py" \
  --observed "0.12,0.08,0.05" --expected "0.10,0.09,0.06" > "$OUT/frequency_distance_smoke.txt"

python3 "$ROOT/calculators/python/inheritance_share_normalizer.py" \
  --shares "1/2,1/3,1/6" > "$OUT/inheritance_share_smoke.txt"

python3 "$ROOT/calculators/python/historical_significance_calculator.py" \
  --procedural 0.92 --transmission 0.96 --practical 0.88 --representation 0.94 --modern 0.96 > "$OUT/historical_significance_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/historical_significance_score.R" 0.92 0.96 0.88 0.94 0.96 > "$OUT/historical_significance_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/historical_significance_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
