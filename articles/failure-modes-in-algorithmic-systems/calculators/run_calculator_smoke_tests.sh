#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/failure_risk_calculator.py" \
  --likelihood 0.42 --severity 0.86 --detectability 0.38 --controllability 0.44 \
  > "$OUT/failure_risk_smoke.txt"

python3 "$ROOT/calculators/python/failure_priority_calculator.py" \
  --likelihood 0.42 --severity 0.86 --detectability 0.38 \
  > "$OUT/failure_priority_smoke.txt"

python3 "$ROOT/calculators/python/resilience_capacity_calculator.py" \
  --monitoring 0.42 --fallback 0.36 --rollback 0.50 --escalation 0.46 --repair 0.40 \
  > "$OUT/resilience_capacity_smoke.txt"

python3 "$ROOT/calculators/python/failure_escalation_trigger.py" \
  --failure-risk 0.1254 --resilience 0.428 \
  > "$OUT/failure_escalation_trigger_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/failure_mode_score.R" 0.42 0.86 0.38 0.44 0.42 0.36 0.50 0.46 0.40 > "$OUT/failure_mode_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/failure_mode_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
