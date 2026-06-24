#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/threshold_unit_calculator.py" \
  --inputs 1,1 --weights 1,1 --threshold 2 > "$OUT/threshold_unit_smoke.txt"

python3 "$ROOT/calculators/python/and_gate_threshold_calculator.py" \
  --x1 1 --x2 1 > "$OUT/and_gate_smoke.txt"

python3 "$ROOT/calculators/python/or_gate_threshold_calculator.py" \
  --x1 1 --x2 0 > "$OUT/or_gate_smoke.txt"

python3 "$ROOT/calculators/python/neural_logic_score_calculator.py" \
  --logical-clarity 0.96 --neural-abstraction 0.94 --computational-relevance 0.96 --cybernetic-connection 0.86 --ai-lineage 0.96 --biological-caution 0.94 --historical-influence 0.98 --interpretability 0.94 --formal-tractability 0.98 --responsible-use-relevance 0.90 > "$OUT/neural_logic_score_smoke.txt"

python3 "$ROOT/calculators/python/biological_caution_calculator.py" \
  --simplification 0.9 --biological-complexity 0.95 --anthropomorphic-language 0.7 --scope-statement 0.85 > "$OUT/biological_caution_smoke.txt"

python3 "$ROOT/calculators/python/ai_lineage_boundary_calculator.py" \
  --claim "McCulloch and Pitts invented deep learning" > "$OUT/ai_lineage_boundary_smoke.txt"

python3 "$ROOT/calculators/python/network_state_update_calculator.py" \
  --x1 1 --x2 0 --threshold 1 > "$OUT/network_state_update_smoke.txt"

python3 "$ROOT/calculators/python/responsible_abstraction_calculator.py" \
  --formal-clarity 0.95 --stated-limits 0.9 --historical-care 0.95 > "$OUT/responsible_abstraction_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/neural_logic_score.R" 0.96 0.94 0.96 0.86 0.96 0.94 0.98 0.94 0.98 0.90 > "$OUT/neural_logic_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/neural_logic_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
