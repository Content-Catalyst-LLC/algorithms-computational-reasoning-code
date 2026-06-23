#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/balance_equation_calculator.py" \
  --left 5 --right 9 --add 3 > "$OUT/balance_equation_smoke.txt"

python3 "$ROOT/calculators/python/cancel_common_term_calculator.py" \
  --left 17 --right 23 --common 5 > "$OUT/cancel_common_term_smoke.txt"

python3 "$ROOT/calculators/python/equation_type_classifier.py" \
  --degree 2 > "$OUT/equation_type_smoke.txt"

python3 "$ROOT/calculators/python/complete_square_calculator.py" \
  --b 6 > "$OUT/complete_square_smoke.txt"

python3 "$ROOT/calculators/python/unknown_check_calculator.py" \
  --a 3 --b 2 --c 17 --x 5 > "$OUT/unknown_check_smoke.txt"

python3 "$ROOT/calculators/python/algebraic_procedure_score_calculator.py" \
  --classification 0.82 --transformation 0.94 --representation 0.84 --demonstration 0.78 --practical-use 0.84 --transmission 0.90 --modern-resonance 0.92 > "$OUT/algebraic_procedure_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/algebraic_procedure_score.R" 0.82 0.94 0.84 0.78 0.84 0.90 0.92 > "$OUT/algebraic_procedure_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/algebraic_procedure_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
