#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/calculators/outputs"
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/calculators/python/causal_effect_calculator.py" --treated-mean 0.62 --control-mean 0.41 > "$ROOT/calculators/outputs/python_smoke.txt"
fi
if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/causal_effect_calculator.R" --treated-mean=0.62 --control-mean=0.41 > "$ROOT/calculators/outputs/r_smoke.txt"
fi
