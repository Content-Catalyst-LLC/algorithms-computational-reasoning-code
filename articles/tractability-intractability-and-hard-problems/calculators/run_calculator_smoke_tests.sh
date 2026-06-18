#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/search_space_calculator.py --n 20 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/tractability_budget_calculator.py --n 30 --budget 1000000 --output-dir outputs/json
