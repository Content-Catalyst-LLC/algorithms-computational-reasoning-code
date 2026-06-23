#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/event_trigger_calculator.py" \
  --value 12 --trigger 10 > "$OUT/event_trigger_smoke.txt"

python3 "$ROOT/calculators/python/cycle_time_calculator.py" \
  --stages 2,3.5,4 > "$OUT/cycle_time_smoke.txt"

python3 "$ROOT/calculators/python/cam_schedule_calculator.py" \
  --angle 91 --activation-angle 90 --tolerance 3 > "$OUT/cam_schedule_smoke.txt"

python3 "$ROOT/calculators/python/repeat_cycle_calculator.py" \
  --cycles 6 --outputs-per-cycle 2 > "$OUT/repeat_cycle_smoke.txt"

python3 "$ROOT/calculators/python/water_flow_time_calculator.py" \
  --volume 100 --flow-rate 5 > "$OUT/water_flow_time_smoke.txt"

python3 "$ROOT/calculators/python/reset_state_calculator.py" \
  --current-state 9 --initial-state 0 --reset true > "$OUT/reset_state_smoke.txt"

python3 "$ROOT/calculators/python/sequenced_action_score_calculator.py" \
  --sequence-structure 0.98 --timing-control 0.98 --mechanical-embodiment 0.94 --conditional-action 0.90 --repeatability 0.94 --documentation-quality 0.92 --historical-significance 0.96 --ethical-caution 0.82 --modern-resonance 0.96 > "$OUT/sequenced_action_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/sequenced_action_score.R" 0.98 0.98 0.94 0.90 0.94 0.92 0.96 0.82 0.96 > "$OUT/sequenced_action_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/sequenced_action_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
