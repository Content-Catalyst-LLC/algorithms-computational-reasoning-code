#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/art_score_calculator.py" \
  --algorithm-analysis 0.98 --exposition 0.98 --mathematical-rigor 0.98 --historical-depth 0.94 --implementation-relevance 0.94 --typography-relevance 0.88 --literate-programming 0.90 --pedagogy 0.98 --maintainability 0.92 --governance-caution 0.90 > "$OUT/art_score_smoke.txt"

python3 "$ROOT/calculators/python/growth_rate_calculator.py" \
  --n 1000 > "$OUT/growth_rate_smoke.txt"

python3 "$ROOT/calculators/python/comparison_sort_lower_bound.py" \
  --n 16 > "$OUT/comparison_sort_lower_bound_smoke.txt"

python3 "$ROOT/calculators/python/runtime_comparison_helper.py" \
  --sizes 10,100,1000 > "$OUT/runtime_comparison_smoke.txt"

python3 "$ROOT/calculators/python/literate_programming_split_helper.py" \
  --module "search_algorithm" > "$OUT/literate_programming_split_smoke.txt"

python3 "$ROOT/calculators/python/tex_clarity_helper.py" \
  --notation 0.9 --layout 0.85 --consistency 0.95 --reproducibility 0.9 > "$OUT/tex_clarity_smoke.txt"

python3 "$ROOT/calculators/python/documentation_score_calculator.py" \
  --purpose 0.9 --assumptions 0.8 --complexity 0.85 --examples 0.9 --tests 0.8 > "$OUT/documentation_score_smoke.txt"

python3 "$ROOT/calculators/python/ai_code_review_caution_calculator.py" \
  --claim "Generated code is understood and no analysis needed" > "$OUT/ai_code_review_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/art_score.R" 0.98 0.98 0.98 0.94 0.94 0.88 0.90 0.98 0.92 0.90 > "$OUT/art_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/art_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
