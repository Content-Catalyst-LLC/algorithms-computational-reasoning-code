#!/usr/bin/env bash
set -Eeuo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT_DIR/python/model_calculator.py"
else
  echo "python3 not found; skipping Python calculator"
fi

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT_DIR/r/model_calculator.R"
else
  echo "Rscript not found; skipping R calculator"
fi
