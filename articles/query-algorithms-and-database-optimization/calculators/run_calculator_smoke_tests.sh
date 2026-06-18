#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/query_cost_estimator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/index_tradeoff_calculator.py --output-dir outputs/json
