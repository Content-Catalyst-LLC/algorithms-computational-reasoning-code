#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/sensitivity_calculator.py" \
  --tp 86 --fn 14 > "$OUT/sensitivity_smoke.txt"

python3 "$ROOT/calculators/python/specificity_calculator.py" \
  --tn 180 --fp 20 > "$OUT/specificity_smoke.txt"

python3 "$ROOT/calculators/python/risk_threshold_calculator.py" \
  --risk-score 0.82 --threshold 0.70 > "$OUT/risk_threshold_smoke.txt"

python3 "$ROOT/calculators/python/sir_population_calculator.py" \
  --susceptible 98000 --infected 1500 --recovered 500 > "$OUT/sir_population_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --clinical-validation 0.70 --equity-readiness 0.58 --privacy-readiness 0.72 --human-review 0.66 --workflow-integration 0.62 --monitoring 0.64 --governance 0.60 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/health_algorithm_risk_calculator.py" \
  --impact-score 0.73 --clinical-validation 0.70 --equity-readiness 0.58 --governance-readiness 0.645714 > "$OUT/health_algorithm_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/health_algorithm_score.R" 0.92 0.54 0.70 0.58 0.72 0.66 0.62 0.64 0.60 > "$OUT/health_algorithm_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/health_algorithm_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
