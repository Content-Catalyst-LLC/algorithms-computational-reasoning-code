#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/threshold_action_calculator.py" \
  --level 7.5 --threshold 5.0 > "$OUT/threshold_action_smoke.txt"

python3 "$ROOT/calculators/python/flow_time_calculator.py" \
  --volume 100 --flow-rate 4 > "$OUT/flow_time_smoke.txt"

python3 "$ROOT/calculators/python/valve_gate_calculator.py" \
  --input-flow 12 --valve-open true > "$OUT/valve_gate_smoke.txt"

python3 "$ROOT/calculators/python/reservoir_volume_calculator.py" \
  --length 2 --width 3 --height 4 > "$OUT/reservoir_volume_smoke.txt"

python3 "$ROOT/calculators/python/pressure_difference_calculator.py" \
  --height 2 > "$OUT/pressure_difference_smoke.txt"

python3 "$ROOT/calculators/python/state_transition_calculator.py" \
  --state 10 --input 3 --constraint 1 > "$OUT/state_transition_smoke.txt"

python3 "$ROOT/calculators/python/mechanical_score_calculator.py" \
  --mechanical-structure 0.96 --procedural-sequence 0.90 --conditional-control 0.88 --hidden-state 0.90 --feedback-potential 0.84 --historical-significance 0.94 --ethical-caution 0.82 --modern-resonance 0.94 > "$OUT/mechanical_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/mechanical_score.R" 0.96 0.90 0.88 0.90 0.84 0.94 0.82 0.94 > "$OUT/mechanical_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/mechanical_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
