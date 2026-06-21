#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 python/agent_based_algorithms_emergent_behavior_audit.py
if command -v Rscript >/dev/null 2>&1; then
  Rscript r/agent_based_algorithms_emergent_behavior_summary.R
else
  echo "Rscript not found; skipping R summary."
fi
python3 calculators/python/agent_based_calculator.py --agents 100 --threshold 0.5 --steps 30 --seed 7
if command -v Rscript >/dev/null 2>&1; then
  Rscript calculators/r/model_calculator.R 100 0.5 30 7 || true
fi
