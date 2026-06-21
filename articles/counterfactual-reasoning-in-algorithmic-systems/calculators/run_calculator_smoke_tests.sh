#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"
python3 "$ROOT/calculators/python/threshold_flip_calculator.py" --score 0.58 --threshold 0.62 --feature-weight 1.2 > "$OUT/threshold_flip.txt"
python3 "$ROOT/calculators/python/recourse_distance_calculator.py" --current 0.48 --target 0.70 --unit-cost 0.75 > "$OUT/recourse_distance.txt"
python3 "$ROOT/calculators/python/counterfactual_contrast_calculator.py" --original-score 0.57 --counterfactual-score 0.65 --threshold 0.62 > "$OUT/counterfactual_contrast.txt"
python3 "$ROOT/calculators/python/feasibility_score_calculator.py" --delta 0.20 --unit-cost 0.75 --feasibility 0.80 > "$OUT/feasibility_score.txt"
if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/counterfactual_calculator.R" 0.57 0.65 0.62 > "$OUT/r_counterfactual_contrast.txt"
fi
echo "Counterfactual calculator smoke tests complete."
