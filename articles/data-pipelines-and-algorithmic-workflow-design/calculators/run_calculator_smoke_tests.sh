#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/pipeline_quality_score_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/freshness_and_validation_calculator.py --output-dir outputs/json
