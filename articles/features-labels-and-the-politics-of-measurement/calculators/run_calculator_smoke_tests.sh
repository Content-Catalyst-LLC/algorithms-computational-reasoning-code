#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT_DIR/calculators/outputs"
mkdir -p "$OUT_DIR"
python3 "$ROOT_DIR/calculators/python/confusion_metric_calculator.py" --tp 72 --fp 18 --tn 88 --fn 22 > "$OUT_DIR/confusion_metric_calculator.txt"
python3 "$ROOT_DIR/calculators/python/label_noise_impact_calculator.py" --sample-size 1000 --noise-rate 0.18 > "$OUT_DIR/label_noise_impact_calculator.txt"
python3 "$ROOT_DIR/calculators/python/proxy_weight_audit_calculator.py" --proxy-weight 0.42 --construct-weight 0.21 --missingness-rate 0.19 > "$OUT_DIR/proxy_weight_audit_calculator.txt"
if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT_DIR/calculators/r/measurement_error_calculator.R" 72 18 88 22 > "$OUT_DIR/r_measurement_error_calculator.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT_DIR/r_measurement_error_calculator.txt"
fi
echo "Calculator smoke tests complete."
