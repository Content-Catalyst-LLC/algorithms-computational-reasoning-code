#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/method_score_calculator.py" \
  --arithmetic-method 0.98 --algebraic-procedure 0.76 --representation 0.98 --transformation 0.88 --proof-relation 0.78 --transmission 0.98 --etymology 0.98 --institutional-adoption 0.94 --historiographic-caution 0.92 --modern-resonance 0.98 > "$OUT/method_score_smoke.txt"

python3 "$ROOT/calculators/python/place_value_calculator.py" \
  --digits 1,2,3,0 > "$OUT/place_value_smoke.txt"

python3 "$ROOT/calculators/python/carrying_calculator.py" \
  --a 8 --b 7 --base 10 > "$OUT/carrying_smoke.txt"

python3 "$ROOT/calculators/python/equation_case_classifier.py" \
  --square 1 --root 10 --number 39 > "$OUT/equation_case_smoke.txt"

python3 "$ROOT/calculators/python/restoration_balancing_calculator.py" \
  --left-roots 12 --right-roots 5 --left-numbers 3 --right-numbers 31 > "$OUT/restoration_balancing_smoke.txt"

python3 "$ROOT/calculators/python/solution_verification_calculator.py" \
  --x 3 --b 10 --c 39 > "$OUT/solution_verification_smoke.txt"

python3 "$ROOT/calculators/python/etymology_scope_calculator.py" \
  --term algorism > "$OUT/etymology_scope_smoke.txt"

python3 "$ROOT/calculators/python/myth_caution_calculator.py" \
  --claim "Al-Khwarizmi invented all algorithms and was the first computer scientist" > "$OUT/myth_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/khwarizmi_method_score.R" 0.98 0.76 0.98 0.88 0.78 0.98 0.98 0.94 0.92 0.98 > "$OUT/khwarizmi_method_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/khwarizmi_method_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
