#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/sliding_window_calculator.py --items A,B,A,C,A,D --window-size 3 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/streaming_queue_pressure_calculator.py --arrival-rate 90 --processing-rate 100 --output-dir outputs/json
