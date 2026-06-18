#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/response_time_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/throughput_utilization_calculator.py --output-dir outputs/json
