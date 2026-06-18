#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/randomized_algorithm_quality_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/monte_carlo_sample_size_calculator.py --output-dir outputs/json
