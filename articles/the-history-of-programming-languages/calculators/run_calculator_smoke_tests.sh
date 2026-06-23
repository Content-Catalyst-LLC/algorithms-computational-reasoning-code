#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/history_score_calculator.py" \
  --abstraction 0.82 --performance-orientation 0.96 --readability 0.76 --formal-specification 0.78 --ecosystem-depth 0.92 --domain-fit 0.98 --safety-orientation 0.48 --institutional-adoption 0.96 --historical-influence 0.98 --governance-caution 0.90 > "$OUT/history_score_smoke.txt"

python3 "$ROOT/calculators/python/paradigm_classifier.py" \
  --description "Fortran arrays numerical scientific simulation compiler" > "$OUT/paradigm_classifier_smoke.txt"

python3 "$ROOT/calculators/python/ecosystem_score_calculator.py" \
  --compiler-or-interpreter 0.9 --standard-library 0.85 --package-manager 0.8 --documentation 0.9 --community 0.85 --institutional-use 0.95 > "$OUT/ecosystem_score_smoke.txt"

python3 "$ROOT/calculators/python/type_safety_score_calculator.py" \
  --static-checking 0.9 --runtime-checking 0.7 --memory-safety 0.95 --concurrency-safety 0.85 --tooling 0.8 > "$OUT/type_safety_score_smoke.txt"

python3 "$ROOT/calculators/python/translation_risk_calculator.py" \
  --source-ambiguity 0.2 --translator-risk 0.3 --runtime-risk 0.2 --dependency-risk 0.4 --test-coverage-gap 0.5 > "$OUT/translation_risk_smoke.txt"

python3 "$ROOT/calculators/python/dependency_governance_calculator.py" \
  --unmaintained-packages 2 --total-packages 10 --unpinned-packages 3 > "$OUT/dependency_governance_smoke.txt"

python3 "$ROOT/calculators/python/ai_language_layer_caution_calculator.py" \
  --claim "AI replaces programming languages and generated code needs no tests" > "$OUT/ai_language_layer_caution_smoke.txt"

python3 "$ROOT/calculators/python/language_comparison_helper.py" \
  --first fortran --first-score 0.872 --second rust --second-score 0.896 > "$OUT/language_comparison_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/history_score.R" 0.82 0.96 0.76 0.78 0.92 0.98 0.48 0.96 0.98 0.90 > "$OUT/history_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/history_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
