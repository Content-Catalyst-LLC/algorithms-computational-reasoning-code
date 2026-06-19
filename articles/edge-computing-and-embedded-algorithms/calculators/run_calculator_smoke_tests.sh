#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/edge_response_deadline_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/battery_threshold_calculator.py --output-dir outputs/json
