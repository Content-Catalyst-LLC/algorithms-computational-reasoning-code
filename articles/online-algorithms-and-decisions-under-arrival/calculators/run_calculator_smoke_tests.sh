#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/ski_rental_calculator.py --rent-cost 10 --buy-cost 50 --days 8 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/queue_pressure_calculator.py --arrival-rate 95 --service-rate 100 --output-dir outputs/json
