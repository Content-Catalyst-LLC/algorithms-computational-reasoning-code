#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
mkdir -p calculators/outputs

python3 calculators/python/model_calculator.py pi --samples=1000 --seed=42 > calculators/outputs/python_pi_smoke.txt
python3 calculators/python/model_calculator.py threshold --samples=1000 --seed=42 --threshold=1250000 > calculators/outputs/python_threshold_smoke.txt

if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/model_calculator.R pi --samples=1000 --seed=42 > calculators/outputs/r_pi_smoke.txt
  Rscript calculators/r/model_calculator.R threshold --samples=1000 --seed=42 --threshold=1250000 > calculators/outputs/r_threshold_smoke.txt
else
  echo "Rscript not found; skipping R calculator smoke tests." > calculators/outputs/r_smoke_skipped.txt
fi

echo "Calculator smoke tests complete."
