#!/usr/bin/env bash
set -euo pipefail
ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ARTICLE_DIR}"
python3 calculators/python/linear_programming_calculator.py
python3 calculators/python/convex_quadratic_calculator.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/convex_quadratic_calculator.R
else
  echo "[WARN] Rscript unavailable; skipping R calculator smoke test."
fi
