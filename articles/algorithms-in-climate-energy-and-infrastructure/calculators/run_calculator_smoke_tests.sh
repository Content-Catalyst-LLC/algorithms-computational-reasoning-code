#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/infrastructure_risk_calculator.py" \
  --hazard 0.80 --exposure 0.75 --vulnerability 0.60 > "$OUT/infrastructure_risk_smoke.txt"

python3 "$ROOT/calculators/python/grid_balance_calculator.py" \
  --supply 4200 --storage 350 --imports 150 --demand 4300 --exports 100 --losses 120 > "$OUT/grid_balance_smoke.txt"

python3 "$ROOT/calculators/python/maintenance_priority_calculator.py" \
  --condition 0.82 --criticality 0.90 --consequence 0.78 --equity 0.70 > "$OUT/maintenance_priority_smoke.txt"

python3 "$ROOT/calculators/python/avoided_loss_calculator.py" \
  --loss-without 12500000 --loss-with 4800000 > "$OUT/avoided_loss_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --equity-readiness 0.62 --validation-readiness 0.74 --monitoring-readiness 0.78 --governance-readiness 0.66 --maintenance-readiness 0.70 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/resilience_risk_calculator.py" \
  --impact-score 0.82 --equity-readiness 0.62 --validation-readiness 0.74 --governance-score 0.70 > "$OUT/resilience_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/infrastructure_algorithm_score.R" 0.82 0.72 0.92 0.62 0.74 0.78 0.66 0.70 > "$OUT/infrastructure_algorithm_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/infrastructure_algorithm_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
