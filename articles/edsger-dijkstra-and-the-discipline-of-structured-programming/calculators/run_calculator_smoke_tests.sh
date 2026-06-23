#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/discipline_score_calculator.py" \
  --structured-control 0.98 --correctness 0.94 --invariants 0.90 --proof-relevance 0.92 --formal-methods 0.88 --readability 0.98 --maintainability 0.96 --algorithmic-relevance 0.90 --system-design 0.88 --governance-caution 0.92 > "$OUT/discipline_score_smoke.txt"

python3 "$ROOT/calculators/python/invariant_check_helper.py" \
  --trace 1,2,3,4 --lower 0 --upper 10 > "$OUT/invariant_check_smoke.txt"

python3 "$ROOT/calculators/python/weakest_precondition_assignment.py" \
  --variable x --expression "y+1" --postcondition "x > 0" > "$OUT/weakest_precondition_smoke.txt"

python3 "$ROOT/calculators/python/dijkstra_shortest_path_calculator.py" \
  --edges "A,B,4;A,C,2;C,B,1;B,D,5;C,D,8;D,E,2;C,E,10" --source A > "$OUT/dijkstra_shortest_path_smoke.txt"

python3 "$ROOT/calculators/python/control_flow_complexity_calculator.py" \
  --decisions 7 > "$OUT/control_flow_complexity_smoke.txt"

python3 "$ROOT/calculators/python/loop_termination_helper.py" \
  --variant-values 10,8,5,1,0 > "$OUT/loop_termination_smoke.txt"

python3 "$ROOT/calculators/python/proof_obligation_helper.py" \
  --loop-name "sum_loop" > "$OUT/proof_obligation_smoke.txt"

python3 "$ROOT/calculators/python/ai_generated_code_caution_calculator.py" \
  --claim "It runs so it is correct and generated code needs no review" > "$OUT/ai_generated_code_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/discipline_score.R" 0.98 0.94 0.90 0.92 0.88 0.98 0.96 0.90 0.88 0.92 > "$OUT/discipline_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/discipline_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
