#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/optimization_objective_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/constraint_penalty_tradeoff_calculator.py --output-dir outputs/json
