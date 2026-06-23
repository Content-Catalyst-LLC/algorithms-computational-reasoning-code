#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/unknown_score_calculator.py" \
  --unknown-representation 0.98 --procedural-transformation 0.94 --abstraction 0.96 --proof-relation 0.88 --translation-continuity 0.90 --practical-grounding 0.92 --philosophical-depth 0.96 --historical-significance 0.98 --ethical-caution 0.86 --modern-resonance 0.98 > "$OUT/unknown_score_smoke.txt"

python3 "$ROOT/calculators/python/equation_case_classifier.py" \
  --square 1 --root 10 --number 39 > "$OUT/equation_case_smoke.txt"

python3 "$ROOT/calculators/python/square_completion_calculator.py" \
  --b 10 --c 39 > "$OUT/square_completion_smoke.txt"

python3 "$ROOT/calculators/python/solution_verification_calculator.py" \
  --x 3 --b 10 --c 39 > "$OUT/solution_verification_smoke.txt"

python3 "$ROOT/calculators/python/translation_continuity_calculator.py" \
  --has-arabic true --has-latin true --has-vernacular true --has-symbolic true > "$OUT/translation_continuity_smoke.txt"

python3 "$ROOT/calculators/python/variable_transition_calculator.py" \
  --named true --symbolic true --ranges-over-values true --shapes-family false > "$OUT/variable_transition_smoke.txt"

python3 "$ROOT/calculators/python/origin_story_caution_calculator.py" \
  --phrase "No symbols so no abstraction" > "$OUT/origin_story_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/unknown_variable_score.R" 0.98 0.94 0.96 0.88 0.90 0.92 0.96 0.98 0.86 0.98 > "$OUT/unknown_variable_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/unknown_variable_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
