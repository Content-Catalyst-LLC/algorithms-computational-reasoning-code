#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/place_value_calculator.py" \
  --digit 7 --base 10 --position 3 > "$OUT/place_value_smoke.txt"

python3 "$ROOT/calculators/python/algebra_balance_calculator.py" \
  --left 5 --right 9 --add 3 > "$OUT/algebra_balance_smoke.txt"

python3 "$ROOT/calculators/python/equation_type_classifier.py" \
  --degree 2 > "$OUT/equation_type_smoke.txt"

python3 "$ROOT/calculators/python/table_interpolation_calculator.py" \
  --x0 10 --y0 100 --x1 20 --y1 140 --x 15 > "$OUT/table_interpolation_smoke.txt"

python3 "$ROOT/calculators/python/procedural_legacy_score_calculator.py" \
  --procedure 0.94 --representation 0.96 --transmission 0.92 --application 0.90 --modern-resonance 0.94 > "$OUT/procedural_legacy_score_smoke.txt"

python3 "$ROOT/calculators/python/transmission_weight_calculator.py" \
  --languages 0.95 --teaching 0.90 --manuscript 0.86 --practical-use 0.82 > "$OUT/transmission_weight_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/procedural_legacy_score.R" 0.94 0.96 0.92 0.90 0.94 > "$OUT/procedural_legacy_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/procedural_legacy_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
