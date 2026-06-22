#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/contestability_score_calculator.py" \
  --notice 0.70 \
  --reasons 0.62 \
  --evidence-access 0.48 \
  --human-review 0.55 \
  --correction 0.52 \
  --remedy 0.44 > "$OUT/contestability_score_smoke.txt"

python3 "$ROOT/calculators/python/procedural_risk_calculator.py" \
  --stakes 0.94 \
  --contestability 0.551667 > "$OUT/procedural_risk_smoke.txt"

python3 "$ROOT/calculators/python/appeal_burden_calculator.py" \
  --time-burden 0.80 \
  --form-complexity 0.70 \
  --language-difficulty 0.60 \
  --accessibility-support 0.20 > "$OUT/appeal_burden_smoke.txt"

python3 "$ROOT/calculators/python/due_process_review_trigger.py" \
  --stakes 0.94 \
  --contestability 0.551667 > "$OUT/due_process_review_trigger_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/contestability_summary_score.R" 0.94 0.70 0.62 0.48 0.55 0.52 0.44 > "$OUT/contestability_summary_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/contestability_summary_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
