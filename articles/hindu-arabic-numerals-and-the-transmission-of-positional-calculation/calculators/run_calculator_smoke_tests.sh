#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/place_value_calculator.py" \
  --digit 7 --base 10 --position 3 > "$OUT/place_value_smoke.txt"

python3 "$ROOT/calculators/python/positional_expansion_calculator.py" \
  --number 2057 > "$OUT/positional_expansion_smoke.txt"

python3 "$ROOT/calculators/python/carry_step_calculator.py" \
  --local-sum 17 --base 10 > "$OUT/carry_step_smoke.txt"

python3 "$ROOT/calculators/python/borrow_step_calculator.py" \
  --upper-digit 4 --lower-digit 2 --base 10 > "$OUT/borrow_step_smoke.txt"

python3 "$ROOT/calculators/python/base_conversion_calculator.py" \
  --number 42 --base 2 > "$OUT/base_conversion_smoke.txt"

python3 "$ROOT/calculators/python/zero_role_classifier.py" \
  --context placeholder > "$OUT/zero_role_smoke.txt"

python3 "$ROOT/calculators/python/positional_score_calculator.py" \
  --representation 0.98 --procedure 0.94 --transmission 0.88 --practical-use 0.92 --pedagogy 0.92 --modern-resonance 0.96 > "$OUT/positional_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/positional_score.R" 0.98 0.94 0.88 0.92 0.92 0.96 > "$OUT/positional_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/positional_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
