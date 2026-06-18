#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/parallel_speedup_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/concurrency_risk_score_calculator.py --output-dir outputs/json
