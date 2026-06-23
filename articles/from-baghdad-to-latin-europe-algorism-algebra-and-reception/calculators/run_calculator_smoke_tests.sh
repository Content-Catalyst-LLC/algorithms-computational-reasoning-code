#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/place_value_calculator.py" \
  --digits 1,2,3,0 > "$OUT/place_value_smoke.txt"

python3 "$ROOT/calculators/python/carrying_calculator.py" \
  --a 8 --b 7 > "$OUT/carrying_smoke.txt"

python3 "$ROOT/calculators/python/borrowing_calculator.py" \
  --minuend 52 --subtrahend 28 > "$OUT/borrowing_smoke.txt"

python3 "$ROOT/calculators/python/algebra_case_calculator.py" \
  --a 1 --b 10 --c 39 > "$OUT/algebra_case_smoke.txt"

python3 "$ROOT/calculators/python/reception_score_calculator.py" \
  --procedural-portability 0.98 --notation-change 0.98 --translation-pathway 0.92 --teaching-value 0.96 --practical-utility 0.96 --institutional-adoption 0.92 --trust-verification 0.90 --historical-significance 0.98 --ethical-caution 0.84 --modern-resonance 0.98 > "$OUT/reception_score_smoke.txt"

python3 "$ROOT/calculators/python/trust_verification_calculator.py" \
  --checks true --teaching true --adoption true --auditability true --practical-use true > "$OUT/trust_verification_smoke.txt"

python3 "$ROOT/calculators/python/adoption_stage_calculator.py" \
  --use 0.90 --teaching 0.90 --institution 0.80 --trust 0.85 > "$OUT/adoption_stage_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/reception_score.R" 0.98 0.98 0.92 0.96 0.96 0.92 0.90 0.98 0.84 0.98 > "$OUT/reception_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/reception_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
