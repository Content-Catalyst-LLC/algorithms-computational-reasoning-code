#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/python/probabilistic_algorithms_reasoning_under_uncertainty_audit.py"
test -f "$ROOT/outputs/tables/probabilistic_algorithm_audit_summary.csv"
bash "$ROOT/calculators/run_calculator_smoke_tests.sh"
echo "Smoke tests complete."
