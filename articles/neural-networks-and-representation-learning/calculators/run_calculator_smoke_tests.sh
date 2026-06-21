#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/calculators/outputs"
mkdir -p "$OUT_DIR"

python3 "$ROOT_DIR/calculators/python/representation_score_calculator.py" --x1 0.5 --x2 -0.2 --x3 0.7 > "$OUT_DIR/representation_score_smoke.txt"
python3 "$ROOT_DIR/calculators/python/generalization_gap_calculator.py" --train-loss 0.42 --test-loss 0.53 > "$OUT_DIR/generalization_gap_smoke.txt"
python3 "$ROOT_DIR/calculators/python/embedding_similarity_calculator.py" --left "0.6,0.2,0.1" --right "0.5,0.25,0.12" > "$OUT_DIR/embedding_similarity_smoke.txt"
python3 "$ROOT_DIR/calculators/python/gradient_update_calculator.py" --theta 0.4 --gradient -0.25 --learning-rate 0.1 > "$OUT_DIR/gradient_update_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT_DIR/calculators/r/representation_score_calculator.R" 0.5 -0.2 0.7 0.0 > "$OUT_DIR/r_representation_score_smoke.txt"
else
  echo "Rscript not found; skipped R calculator smoke test." > "$OUT_DIR/r_representation_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
