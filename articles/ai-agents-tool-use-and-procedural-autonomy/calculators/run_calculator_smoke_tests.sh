#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/permission_gate_calculator.py" \
  --risk 0.85 \
  --approval-required 1 \
  --approved 0 \
  --threshold 0.65 > "$OUT/permission_gate_calculator_smoke.txt"

python3 "$ROOT/calculators/python/autonomy_level_calculator.py" \
  --blocked 2 \
  --escalated 1 \
  --actions 6 > "$OUT/autonomy_level_calculator_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/agent_risk_score.R" 0.70 0.80 > "$OUT/agent_risk_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/agent_risk_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
