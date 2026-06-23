#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/hiring_score_calculator.py" \
  --job-relevance 0.82 --evidence-quality 0.74 --experience-fit 0.68 --accessibility-support 0.70 > "$OUT/hiring_score_smoke.txt"

python3 "$ROOT/calculators/python/scheduling_coverage_calculator.py" \
  --scheduled-hours 420 --demand-hours 390 > "$OUT/scheduling_coverage_smoke.txt"

python3 "$ROOT/calculators/python/productivity_metric_calculator.py" \
  --quantity 0.82 --quality 0.76 --reliability 0.80 --context-penalty 0.30 > "$OUT/productivity_metric_smoke.txt"

python3 "$ROOT/calculators/python/workload_burden_calculator.py" \
  --pace 0.84 --hours 0.72 --fatigue 0.70 --schedule-volatility 0.78 > "$OUT/workload_burden_smoke.txt"

python3 "$ROOT/calculators/python/governance_readiness_calculator.py" \
  --fairness-readiness 0.58 --privacy-readiness 0.66 --contestability 0.52 --safety-readiness 0.70 --human-review 0.60 --monitoring 0.58 --governance 0.56 > "$OUT/governance_readiness_smoke.txt"

python3 "$ROOT/calculators/python/workplace_algorithm_risk_calculator.py" \
  --impact-score 0.80 --fairness-readiness 0.58 --privacy-readiness 0.66 --contestability 0.52 --governance-readiness 0.60 > "$OUT/workplace_algorithm_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/workplace_algorithm_score.R" 0.88 0.72 0.58 0.66 0.52 0.70 0.60 0.58 0.56 > "$OUT/workplace_algorithm_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/workplace_algorithm_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
