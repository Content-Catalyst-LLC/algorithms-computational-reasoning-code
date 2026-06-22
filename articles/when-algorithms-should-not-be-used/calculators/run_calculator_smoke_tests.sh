#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/non_use_pressure_calculator.py" \
  --stakes 0.94 \
  --irreversibility 0.78 \
  --governance-weakness 0.56 \
  --proxy-illegitimacy 0.70 > "$OUT/non_use_pressure_smoke.txt"

python3 "$ROOT/calculators/python/responsible_use_readiness_calculator.py" \
  --target-legitimacy 0.42 \
  --data-legitimacy 0.48 \
  --contestability 0.40 \
  --human-judgment 0.46 \
  --governance-capacity 0.44 \
  --repairability 0.38 > "$OUT/responsible_use_readiness_smoke.txt"

python3 "$ROOT/calculators/python/repairability_calculator.py" \
  --detection 0.40 \
  --correction 0.38 \
  --remedy 0.34 \
  --recurrence-prevention 0.40 > "$OUT/repairability_smoke.txt"

python3 "$ROOT/calculators/python/refusal_threshold_calculator.py" \
  --non-use-pressure 0.745 \
  --responsible-readiness 0.43 > "$OUT/refusal_threshold_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/non_use_score.R" 0.42 0.48 0.40 0.46 0.44 0.38 0.94 0.78 0.70 > "$OUT/non_use_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/non_use_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
