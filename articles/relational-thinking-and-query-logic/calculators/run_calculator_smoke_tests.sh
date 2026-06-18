#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/query_logic_score_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/join_risk_calculator.py --output-dir outputs/json
