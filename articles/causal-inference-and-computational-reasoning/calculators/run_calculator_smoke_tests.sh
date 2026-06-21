#!/usr/bin/env bash
set -euo pipefail

ARTICLE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ARTICLE_ROOT/calculators/outputs"
mkdir -p "$OUT_DIR"

python3 "$ARTICLE_ROOT/calculators/python/causal_effect_calculator.py" \
  --treated-mean 0.64 --control-mean 0.47 > "$OUT_DIR/causal_effect_calculator.txt"

grep -q "difference=0.170000" "$OUT_DIR/causal_effect_calculator.txt"

python3 "$ARTICLE_ROOT/calculators/python/difference_in_differences_calculator.py" \
  --treated-pre 0.30 --treated-post 0.52 --control-pre 0.28 --control-post 0.36 > "$OUT_DIR/difference_in_differences_calculator.txt"

grep -q "did_estimate=0.140000" "$OUT_DIR/difference_in_differences_calculator.txt"

python3 "$ARTICLE_ROOT/calculators/python/sensitivity_bias_calculator.py" \
  --effect 0.18 --bias 0.05 > "$OUT_DIR/sensitivity_bias_calculator.txt"

grep -q "bias_adjusted_effect=0.130000" "$OUT_DIR/sensitivity_bias_calculator.txt"

if [ ! -f "$ARTICLE_ROOT/outputs/tables/synthetic_causal_observations.csv" ]; then
  python3 "$ARTICLE_ROOT/python/causal_inference_audit_workflow.py" > "$OUT_DIR/workflow_for_ipw.log"
fi

python3 "$ARTICLE_ROOT/calculators/python/ipw_effect_calculator.py" \
  --csv "$ARTICLE_ROOT/outputs/tables/synthetic_causal_observations.csv" > "$OUT_DIR/ipw_effect_calculator.txt"

grep -q "ipw_effect=" "$OUT_DIR/ipw_effect_calculator.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ARTICLE_ROOT/calculators/r/causal_effect_calculator.R" 0.64 0.47 > "$OUT_DIR/r_causal_effect_calculator.txt"
  grep -q "difference=0.170000" "$OUT_DIR/r_causal_effect_calculator.txt"
else
  echo "Rscript not found; skipped R calculator smoke test." > "$OUT_DIR/r_causal_effect_calculator_skipped.txt"
fi

echo "Calculator smoke tests passed."
