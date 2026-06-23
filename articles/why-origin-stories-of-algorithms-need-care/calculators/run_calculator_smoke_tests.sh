#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/origin_care_score_calculator.py" \
  --evidence-grounding 0.96 --scope-clarity 0.98 --anachronism-control 0.96 --network-awareness 0.88 --etymology-caution 0.98 --transmission-depth 0.90 --credit-distribution 0.90 --public-usefulness 0.96 --historical-significance 0.98 --modern-resonance 0.98 > "$OUT/origin_care_score_smoke.txt"

python3 "$ROOT/calculators/python/layer_confusion_calculator.py" \
  --claim "The name proves he therefore invented all algorithms" > "$OUT/layer_confusion_smoke.txt"

python3 "$ROOT/calculators/python/etymology_risk_calculator.py" \
  --claim "Al-Khwarizmi invented algorithms because the word comes from his name" > "$OUT/etymology_risk_smoke.txt"

python3 "$ROOT/calculators/python/anachronism_risk_calculator.py" \
  --claim "A medieval scholar wrote code and was the first computer scientist" > "$OUT/anachronism_risk_smoke.txt"

python3 "$ROOT/calculators/python/network_credit_calculator.py" \
  --has-translators true --has-scribes true --has-teachers true --has-users true --has-institutions true --has-tools true > "$OUT/network_credit_smoke.txt"

python3 "$ROOT/calculators/python/evidence_scope_calculator.py" \
  --has-evidence true --has-date-or-period true --has-scope true --has-uncertainty true --has-transmission true > "$OUT/evidence_scope_smoke.txt"

python3 "$ROOT/calculators/python/origin_story_rewrite_helper.py" \
  --claim-type khwarizmi_invented_algorithms > "$OUT/rewrite_helper_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/origin_care_score.R" 0.96 0.98 0.96 0.88 0.98 0.90 0.90 0.96 0.98 0.98 > "$OUT/origin_care_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/origin_care_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
