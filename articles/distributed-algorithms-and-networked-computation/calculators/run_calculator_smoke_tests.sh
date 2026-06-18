#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/quorum_fault_tolerance_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/distributed_latency_calculator.py --output-dir outputs/json
