#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/evolutionary_search_quality_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/population_diversity_calculator.py --output-dir outputs/json
