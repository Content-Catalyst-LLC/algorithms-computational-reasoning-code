#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/graph_path_score_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/hybrid_retrieval_score_calculator.py --output-dir outputs/json
