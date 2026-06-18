#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/growth_rate_calculator.py --n 1000 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/scalability_threshold_calculator.py --budget 1000000 --output-dir outputs/json
