#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/humanization_score_calculator.py" \
  --compiler-centrality 0.98 --human-readability 0.96 --portability 0.92 --documentation 0.90 --standards 0.88 --debugging 0.86 --business-relevance 0.88 --institutional-scale 0.92 --abstraction 0.98 --governance-caution 0.90 > "$OUT/humanization_score_smoke.txt"

python3 "$ROOT/calculators/python/compiler_pipeline_helper.py" \
  --source "ADD PAYROLL-TOTAL TO TAX-BASE" > "$OUT/compiler_pipeline_smoke.txt"

python3 "$ROOT/calculators/python/portability_score_calculator.py" \
  --supported-targets 4 --desired-targets 5 > "$OUT/portability_score_smoke.txt"

python3 "$ROOT/calculators/python/diagnostic_quality_calculator.py" \
  --clarity 0.9 --location 0.8 --explanation 0.85 --fix-hint 0.7 > "$OUT/diagnostic_quality_smoke.txt"

python3 "$ROOT/calculators/python/standards_conformance_helper.py" \
  --has-spec --has-tests --has-validation --has-documentation > "$OUT/standards_conformance_smoke.txt"

python3 "$ROOT/calculators/python/maintenance_burden_calculator.py" \
  --lines-of-code 50000 --readability 0.7 --documentation 0.8 --test-coverage 0.75 > "$OUT/maintenance_burden_smoke.txt"

python3 "$ROOT/calculators/python/ai_code_generation_caution_calculator.py" \
  --claim "AI is just a compiler and no tests needed" > "$OUT/ai_code_generation_caution_smoke.txt"

python3 "$ROOT/calculators/python/translation_trust_calculator.py" \
  --specification 0.9 --tests 0.85 --diagnostics 0.8 --human-review 0.9 > "$OUT/translation_trust_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/humanization_score.R" 0.98 0.96 0.92 0.90 0.88 0.86 0.88 0.92 0.98 0.90 > "$OUT/humanization_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/humanization_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
