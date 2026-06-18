#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/precision_recall_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/search_architecture_score_calculator.py --output-dir outputs/json
