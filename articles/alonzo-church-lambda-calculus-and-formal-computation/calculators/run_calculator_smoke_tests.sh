#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/formal_score_calculator.py" \
  --formalization 0.98 --functional-abstraction 0.98 --symbolic-transformation 0.98 --substitution 0.96 --reduction 0.96 --computability 0.96 --undecidability 0.86 --type-influence 0.88 --programming-relevance 0.98 --ai-caution 0.86 > "$OUT/formal_score_smoke.txt"

python3 "$ROOT/calculators/python/beta_reduction_calculator.py" \
  --pattern identity --argument y > "$OUT/beta_reduction_smoke.txt"

python3 "$ROOT/calculators/python/alpha_conversion_calculator.py" \
  --body x --old x --new y > "$OUT/alpha_conversion_smoke.txt"

python3 "$ROOT/calculators/python/church_numeral_calculator.py" \
  --n 3 > "$OUT/church_numeral_smoke.txt"

python3 "$ROOT/calculators/python/normal_form_helper.py" \
  --term "(λx. x) y" > "$OUT/normal_form_smoke.txt"

python3 "$ROOT/calculators/python/capture_risk_calculator.py" \
  --substitute-variable x --argument-free-vars y,z --body-binders y > "$OUT/capture_risk_smoke.txt"

python3 "$ROOT/calculators/python/decidability_scope_helper.py" \
  --problem entscheidungsproblem > "$OUT/decidability_scope_smoke.txt"

python3 "$ROOT/calculators/python/ai_formal_reasoning_caution_calculator.py" \
  --claim "AI proves everything and formal systems decide all truth" > "$OUT/ai_formal_reasoning_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/church_formal_score.R" 0.98 0.98 0.98 0.96 0.96 0.96 0.86 0.88 0.98 0.86 > "$OUT/church_formal_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/church_formal_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
