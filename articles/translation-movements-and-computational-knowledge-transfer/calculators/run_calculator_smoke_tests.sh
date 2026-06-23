#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/procedural_fidelity_calculator.py" \
  --terms 1 --steps 1 --examples 0.8 --diagrams 0.9 --tables 0.9 --context 0.8 > "$OUT/procedural_fidelity_smoke.txt"

python3 "$ROOT/calculators/python/vocabulary_mapping_calculator.py" \
  --mapped-terms 18 --total-terms 20 > "$OUT/vocabulary_mapping_smoke.txt"

python3 "$ROOT/calculators/python/table_error_rate_calculator.py" \
  --mismatches 2 --checked-values 100 > "$OUT/table_error_rate_smoke.txt"

python3 "$ROOT/calculators/python/relay_depth_calculator.py" \
  --path "Greek>Syriac>Arabic>Latin" > "$OUT/relay_depth_smoke.txt"

python3 "$ROOT/calculators/python/knowledge_object_completeness_calculator.py" \
  --has-terms true --has-steps true --has-examples true --has-diagrams true --has-tables true --has-context true > "$OUT/knowledge_object_completeness_smoke.txt"

python3 "$ROOT/calculators/python/transfer_score_calculator.py" \
  --procedural-fidelity 0.98 --vocabulary-mapping 0.90 --diagram-table-preservation 0.94 --institutional-support 0.88 --error-control 0.94 --adaptation 0.90 --historical-significance 0.96 --ethical-caution 0.84 --modern-resonance 0.96 > "$OUT/transfer_score_smoke.txt"

python3 "$ROOT/calculators/python/origin_story_risk_calculator.py" \
  --phrase "They only preserved Greek knowledge" > "$OUT/origin_story_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/transfer_score.R" 0.98 0.90 0.94 0.88 0.94 0.90 0.96 0.84 0.96 > "$OUT/transfer_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/transfer_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
