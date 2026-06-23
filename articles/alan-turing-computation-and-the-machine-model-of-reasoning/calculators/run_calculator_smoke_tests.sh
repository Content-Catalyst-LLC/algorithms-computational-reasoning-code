#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/reasoning_score_calculator.py" \
  --formalization 0.98 --machine-abstraction 0.98 --symbolic-representation 0.96 --universality 0.86 --decidability 0.90 --limit-awareness 0.92 --reasoning-relevance 0.96 --ai-relevance 0.82 --governance-caution 0.86 --modern-resonance 0.98 > "$OUT/reasoning_score_smoke.txt"

python3 "$ROOT/calculators/python/turing_transition_simulator.py" \
  --tape 111_ --max-steps 20 > "$OUT/turing_transition_smoke.txt"

python3 "$ROOT/calculators/python/unary_increment_machine.py" \
  --tape 111_ > "$OUT/unary_increment_smoke.txt"

python3 "$ROOT/calculators/python/halting_trace_calculator.py" \
  --program countdown --n 5 --max-steps 20 > "$OUT/halting_trace_smoke.txt"

python3 "$ROOT/calculators/python/decidability_scope_helper.py" \
  --problem halting_problem > "$OUT/decidability_scope_smoke.txt"

python3 "$ROOT/calculators/python/universal_description_calculator.py" \
  --name unary_increment > "$OUT/universal_description_smoke.json"

python3 "$ROOT/calculators/python/imitation_game_evaluator.py" \
  --has-controlled-setting true --has-human-judges true --has-clear-task true --has-failure-analysis true --has-scope-limits true > "$OUT/imitation_game_smoke.txt"

python3 "$ROOT/calculators/python/ai_overclaim_caution_calculator.py" \
  --claim "Turing proved machines think and AI decides everything" > "$OUT/ai_overclaim_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/turing_reasoning_score.R" 0.98 0.98 0.96 0.86 0.90 0.92 0.96 0.82 0.86 0.98 > "$OUT/turing_reasoning_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/turing_reasoning_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
