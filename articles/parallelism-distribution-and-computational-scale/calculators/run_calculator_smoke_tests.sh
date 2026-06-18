#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/speedup_calculator.py --serial-fraction 0.10 --processors 16 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/distributed_capacity_calculator.py --workers 8 --service-rate 100 --overhead-rate 0.05 --output-dir outputs/json
