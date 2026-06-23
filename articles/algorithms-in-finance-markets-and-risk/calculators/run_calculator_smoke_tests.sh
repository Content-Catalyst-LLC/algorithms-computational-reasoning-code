#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/expected_loss_calculator.py" \
  --pd 0.035 --lgd 0.45 --ead 100000 > "$OUT/expected_loss_smoke.txt"

python3 "$ROOT/calculators/python/portfolio_return_calculator.py" \
  --weights "0.60,0.40" --returns "0.08,0.03" > "$OUT/portfolio_return_smoke.txt"

python3 "$ROOT/calculators/python/portfolio_variance_calculator.py" \
  --w1 0.60 --w2 0.40 --sigma1 0.18 --sigma2 0.07 --rho 0.25 > "$OUT/portfolio_variance_smoke.txt"

python3 "$ROOT/calculators/python/value_at_risk_calculator.py" \
  --portfolio-value 1000000 --volatility 0.025 --confidence 0.95 > "$OUT/value_at_risk_smoke.txt"

python3 "$ROOT/calculators/python/stress_loss_calculator.py" \
  --exposure 500000 --shock 0.18 --recovery 0.10 > "$OUT/stress_loss_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --transparency 0.58 --human-review 0.62 --validation 0.70 --monitoring 0.66 --governance 0.64 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/financial_algorithm_risk_calculator.py" \
  --model-risk 0.68 --impact-score 0.486667 --governance-readiness 0.64 > "$OUT/financial_algorithm_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/financial_algorithm_score.R" 0.34 0.92 0.68 0.58 0.62 0.70 0.66 0.64 0.20 > "$OUT/financial_algorithm_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/financial_algorithm_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
