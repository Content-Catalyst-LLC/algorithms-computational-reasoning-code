#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/selection_gap_calculator.py" \
  --rates 0.46 0.31 0.37 > "$OUT/selection_gap_smoke.txt"

python3 "$ROOT/calculators/python/representation_gap_calculator.py" \
  --data-share 0.28 \
  --deployment-share 0.36 > "$OUT/representation_gap_smoke.txt"

python3 "$ROOT/calculators/python/label_gap_calculator.py" \
  --label-positive-rate 0.33 \
  --verified-positive-rate 0.43 > "$OUT/label_gap_smoke.txt"

python3 "$ROOT/calculators/python/historical_risk_calculator.py" \
  --provenance-risk 0.66 \
  --measurement-weakness 0.58 \
  --proxy-risk 0.62 \
  --remediation 0.42 > "$OUT/historical_risk_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/bias_history_score.R" 0.28 0.36 0.33 0.43 0.66 0.58 0.62 0.42 > "$OUT/bias_history_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/bias_history_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
