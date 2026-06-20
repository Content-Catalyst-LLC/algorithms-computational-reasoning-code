#!/usr/bin/env bash
set -euo pipefail

ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ARTICLE_DIR}"

python3 calculators/threshold_classifier_calculator.py --score 0.72 --threshold 0.50
python3 calculators/confusion_matrix_calculator.py --csv data/classification_cases.csv --threshold 0.50

echo "[OK] calculator smoke tests passed"
