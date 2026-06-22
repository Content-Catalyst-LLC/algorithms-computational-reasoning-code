#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/stock_flow_calculator.py" \
  --current-stock 100 \
  --inflow 12 \
  --outflow 7 > "$OUT/stock_flow_smoke.txt"

python3 "$ROOT/calculators/python/feedback_update_calculator.py" \
  --state 50 \
  --intervention 3 \
  --feedback-rate 0.04 \
  --decay-rate 0.01 > "$OUT/feedback_update_smoke.txt"

python3 "$ROOT/calculators/python/system_vulnerability_calculator.py" \
  --feedback-strength 0.72 \
  --network-dependency 0.68 \
  --scenario-uncertainty 0.54 \
  --resilience 0.62 > "$OUT/system_vulnerability_smoke.txt"

python3 "$ROOT/calculators/python/model_readiness_calculator.py" \
  --calibration 0.70 \
  --documentation 0.74 \
  --governance 0.70 \
  --resilience 0.62 > "$OUT/model_readiness_smoke.txt"

python3 "$ROOT/calculators/python/sensitivity_calculator.py" \
  --baseline-output 100 \
  --changed-output 112 \
  --baseline-parameter 10 \
  --changed-parameter 11 > "$OUT/sensitivity_smoke.txt"

python3 "$ROOT/calculators/python/resilience_calculator.py" \
  --post-shock-performance 60 \
  --recovery-performance 85 \
  --baseline-performance 100 > "$OUT/resilience_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/systems_model_score.R" 0.72 0.68 0.54 0.62 0.70 0.74 0.70 0.76 > "$OUT/systems_model_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/systems_model_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
