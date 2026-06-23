#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/trade_price_calculator.py" \
  --quantity 12 --unit-price 3.5 > "$OUT/trade_price_smoke.txt"

python3 "$ROOT/calculators/python/currency_exchange_calculator.py" \
  --amount 100 --rate 1.25 > "$OUT/currency_exchange_smoke.txt"

python3 "$ROOT/calculators/python/inheritance_share_calculator.py" \
  --total 1200 --weights 2,1,1 > "$OUT/inheritance_share_smoke.txt"

python3 "$ROOT/calculators/python/survey_rectangle_area_calculator.py" \
  --length 30 --width 12 > "$OUT/rectangle_area_smoke.txt"

python3 "$ROOT/calculators/python/survey_trapezoid_area_calculator.py" \
  --base-a 10 --base-b 14 --height 7 > "$OUT/trapezoid_area_smoke.txt"

python3 "$ROOT/calculators/python/unit_conversion_calculator.py" \
  --quantity 15 --factor 2.5 > "$OUT/unit_conversion_smoke.txt"

python3 "$ROOT/calculators/python/ledger_balance_checker.py" \
  --debits 100,25 --credits 80,45 > "$OUT/ledger_balance_smoke.txt"

python3 "$ROOT/calculators/python/practical_score_calculator.py" \
  --procedure 0.92 --representation 0.86 --institutional-importance 0.94 --verification 0.88 --transmission 0.86 --modern-resonance 0.90 > "$OUT/practical_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/practical_score.R" 0.92 0.86 0.94 0.88 0.86 0.90 > "$OUT/practical_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/practical_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
