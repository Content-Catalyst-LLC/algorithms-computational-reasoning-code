#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/future_risk_calculator.py" \
  --institutional-consequence 0.94 --uncertainty 0.86 --automation-level 0.94 --opacity 0.88 --contestability-need 0.94 --human-judgment-requirement 0.98 --failure-severity 0.92 > "$OUT/future_risk_smoke.txt"

python3 "$ROOT/calculators/python/readiness_calculator.py" \
  --technical-capability 0.92 --governance-maturity 0.58 --deployment-readiness 0.56 > "$OUT/readiness_smoke.txt"

python3 "$ROOT/calculators/python/automation_risk_calculator.py" \
  --stakes 0.95 --opacity 0.85 --delegation 0.90 --irreversibility 0.80 > "$OUT/automation_risk_smoke.txt"

python3 "$ROOT/calculators/python/meaningful_review_calculator.py" \
  --authority 0.8 --time 0.6 --evidence 0.7 --training 0.8 --override-power 0.9 > "$OUT/meaningful_review_smoke.txt"

python3 "$ROOT/calculators/python/no_go_calculator.py" \
  --high-opacity --no-appeal --no-governance > "$OUT/no_go_smoke.txt"

python3 "$ROOT/calculators/python/computational_literacy_calculator.py" \
  --data 0.8 --algorithms 0.8 --statistics 0.7 --systems 0.7 --ai-limits 0.9 --governance 0.8 > "$OUT/computational_literacy_smoke.txt"

python3 "$ROOT/calculators/python/ai_agent_boundary_calculator.py" \
  --claim "full autonomy no approval and no audit trail" > "$OUT/ai_agent_boundary_smoke.txt"

python3 "$ROOT/calculators/python/generated_code_governance_calculator.py" \
  --claim "ship generated code directly with no tests needed and no security review" > "$OUT/generated_code_governance_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/future_risk_score.R" 0.94 0.86 0.94 0.88 0.94 0.98 0.92 > "$OUT/future_risk_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/future_risk_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
