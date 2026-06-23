#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/cybernetic_score_calculator.py" \
  --feedback-centrality 0.98 --control-relevance 0.96 --communication-relevance 0.94 --prediction-relevance 0.86 --stability-relevance 0.96 --amplification-risk 0.90 --automation-ethics 0.92 --ai-relevance 0.96 --institutional-relevance 0.92 --governance-caution 0.96 > "$OUT/cybernetic_score_smoke.txt"

python3 "$ROOT/calculators/python/negative_feedback_calculator.py" \
  --initial 10 --target 0 --gain 0.2 --steps 5 > "$OUT/negative_feedback_smoke.txt"

python3 "$ROOT/calculators/python/positive_feedback_calculator.py" \
  --initial 1 --rate 0.1 --steps 5 > "$OUT/positive_feedback_smoke.txt"

python3 "$ROOT/calculators/python/control_error_calculator.py" \
  --target 5 --observed 3 --gain 0.5 > "$OUT/control_error_smoke.txt"

python3 "$ROOT/calculators/python/delay_effect_helper.py" \
  --delayed-observed 2 --current-state 4 --target 5 > "$OUT/delay_effect_smoke.txt"

python3 "$ROOT/calculators/python/platform_feedback_loop_calculator.py" \
  --initial-visibility 100 --engagement-rate 0.2 --ranking-gain 0.5 --steps 5 > "$OUT/platform_feedback_loop_smoke.txt"

python3 "$ROOT/calculators/python/rl_reward_caution_calculator.py" \
  --claim "Maximize reward means ethical and no human oversight needed" > "$OUT/rl_reward_caution_smoke.txt"

python3 "$ROOT/calculators/python/feedback_governance_caution_calculator.py" \
  --claim "Feedback is always good and model governance is enough" > "$OUT/feedback_governance_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/feedback_score.R" 0.98 0.96 0.94 0.86 0.96 0.90 0.92 0.96 0.92 0.96 > "$OUT/feedback_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/feedback_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
