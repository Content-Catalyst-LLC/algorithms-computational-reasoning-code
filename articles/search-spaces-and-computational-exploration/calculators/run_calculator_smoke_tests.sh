#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/search_space_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/search_coverage_pruning_calculator.py --output-dir outputs/json
