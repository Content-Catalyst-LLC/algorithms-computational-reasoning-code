#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/approximation_quality_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/optimality_gap_calculator.py --output-dir outputs/json
