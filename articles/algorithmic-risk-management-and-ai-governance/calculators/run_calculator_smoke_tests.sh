#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/inherent_risk_calculator.py" \
  --severity 0.92 \
  --likelihood 0.44 \
  --detectability 0.42 > "$OUT/inherent_risk_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --ownership 0.60 \
  --documentation 0.62 \
  --monitoring 0.58 \
  --contestability 0.52 \
  --remediation 0.46 \
  --stop-authority 0.50 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/residual_risk_calculator.py" \
  --inherent-risk 0.234784 \
  --control-effectiveness 0.48 > "$OUT/residual_risk_smoke.txt"

python3 "$ROOT/calculators/python/control_effectiveness_calculator.py" \
  --prevention 0.46 \
  --detection 0.50 \
  --mitigation 0.48 \
  --response 0.52 > "$OUT/control_effectiveness_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/risk_governance_score.R" 0.92 0.44 0.42 0.60 0.62 0.58 0.52 0.46 0.50 0.48 > "$OUT/risk_governance_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/risk_governance_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
