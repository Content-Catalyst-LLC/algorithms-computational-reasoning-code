#!/usr/bin/env bash
set -euo pipefail
ARTICLE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ARTICLE_ROOT"
python3 calculators/python/hash_verification_calculator.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/hash_verification_calculator.R
else
  printf 'Skipping R calculator; Rscript not found.\n'
fi
