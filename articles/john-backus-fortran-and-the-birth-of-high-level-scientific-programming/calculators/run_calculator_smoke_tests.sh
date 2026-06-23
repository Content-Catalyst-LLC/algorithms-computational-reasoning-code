#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/birth_score_calculator.py" \
  --high-level-language 0.98 --scientific-expression 0.98 --compiler-optimization 0.94 --numerical-relevance 0.96 --portability 0.90 --performance-credibility 0.96 --language-history 0.94 --formal-specification 0.84 --maintainability 0.90 --governance-caution 0.88 > "$OUT/birth_score_smoke.txt"

python3 "$ROOT/calculators/python/formula_translation_calculator.py" \
  --x 2 --a 2 --b -3 --c 1 > "$OUT/formula_translation_smoke.txt"

python3 "$ROOT/calculators/python/vector_loop_calculator.py" \
  --values "0,0.5,1,1.5,2" > "$OUT/vector_loop_smoke.txt"

python3 "$ROOT/calculators/python/portability_score_calculator.py" \
  --supported-compilers 4 --target-systems 5 > "$OUT/portability_score_smoke.txt"

python3 "$ROOT/calculators/python/performance_credibility_calculator.py" \
  --generated-runtime 1.12 --handcoded-runtime 1.0 > "$OUT/performance_credibility_smoke.txt"

python3 "$ROOT/calculators/python/translation_trust_calculator.py" \
  --readability 0.9 --correct-translation 0.85 --performance 0.9 --tests 0.8 --documentation 0.85 > "$OUT/translation_trust_smoke.txt"

python3 "$ROOT/calculators/python/bnf_rule_helper.py" \
  --nonterminal "expression" --alternatives "term | expression + term | expression - term" > "$OUT/bnf_rule_smoke.txt"

python3 "$ROOT/calculators/python/ai_scientific_code_caution_calculator.py" \
  --claim "Generated scientific code is automatically correct and no numerical review needed" > "$OUT/ai_scientific_code_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/birth_score.R" 0.98 0.98 0.94 0.96 0.90 0.96 0.94 0.84 0.90 0.88 > "$OUT/birth_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/birth_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
