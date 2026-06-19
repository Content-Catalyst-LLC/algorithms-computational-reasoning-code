#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/platform_dependency_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/platform_switching_api_visibility_calculator.py --output-dir outputs/json
