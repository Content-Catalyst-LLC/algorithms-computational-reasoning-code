#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/efficiency_gain_calculator.py --baseline-cost 100 --optimized-cost 64 --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/understanding_tradeoff_calculator.py --efficiency-gain 0.36 --understanding-before 0.82 --understanding-after 0.68 --output-dir outputs/json
