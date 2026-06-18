#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/ranking_signal_score_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/precision_at_k_calculator.py --output-dir outputs/json
