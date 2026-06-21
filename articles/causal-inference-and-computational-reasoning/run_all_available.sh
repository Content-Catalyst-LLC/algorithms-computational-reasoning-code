#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$ROOT/outputs/logs"
if command -v python3 >/dev/null 2>&1; then
  python3 "$ROOT/python/causal_inference_computational_reasoning_audit.py" | tee "$ROOT/outputs/logs/python_workflow.log"
else
  echo "python3 not found; skipping Python workflow" | tee "$ROOT/outputs/logs/python_workflow.log"
fi
if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/r/causal_inference_computational_reasoning_summary.R" | tee "$ROOT/outputs/logs/r_workflow.log"
else
  echo "Rscript not found; skipping R workflow" | tee "$ROOT/outputs/logs/r_workflow.log"
fi
bash "$ROOT/calculators/run_calculator_smoke_tests.sh" | tee "$ROOT/outputs/logs/calculator_smoke.log" || true
