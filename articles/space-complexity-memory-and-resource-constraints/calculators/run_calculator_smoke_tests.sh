#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/graph_storage_calculator.py --vertices 1000 --edges 5000 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/memory_budget_calculator.py --n 10000 --budget 1000000 --output-dir outputs/json
