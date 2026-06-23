#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/history_score_calculator.py" \
  --procedural-explicitness 0.98 --representation 0.94 --proof-correctness 0.92 --portability 0.98 --mechanization 0.54 --formalization 0.84 --programmability 0.42 --institutional-adoption 0.94 --governance-relevance 0.72 --modern-resonance 0.98 > "$OUT/history_score_smoke.txt"

python3 "$ROOT/calculators/python/timeline_layer_classifier.py" \
  --mechanization 0.98 --formalization 0.94 --programmability 0.98 --governance 0.88 > "$OUT/timeline_layer_smoke.txt"

python3 "$ROOT/calculators/python/procedure_feature_score.py" \
  --has-input true --has-steps true --has-conditions true --has-iteration true --has-termination true --has-verification true > "$OUT/procedure_feature_score_smoke.txt"

python3 "$ROOT/calculators/python/complexity_growth_calculator.py" \
  --n 16 > "$OUT/complexity_growth_smoke.txt"

python3 "$ROOT/calculators/python/computability_status_helper.py" \
  --problem halting_problem > "$OUT/computability_status_smoke.txt"

python3 "$ROOT/calculators/python/governance_relevance_calculator.py" \
  --has-audit true --has-contestability true --has-harm true --has-transparency true --has-human-judgment true > "$OUT/governance_relevance_smoke.txt"

python3 "$ROOT/calculators/python/algorithm_ancestor_caution_calculator.py" \
  --claim "The ancient tablet was a database and the scribe wrote code" > "$OUT/algorithm_ancestor_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/history_score.R" 0.98 0.94 0.92 0.98 0.54 0.84 0.42 0.94 0.72 0.98 > "$OUT/history_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/history_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
