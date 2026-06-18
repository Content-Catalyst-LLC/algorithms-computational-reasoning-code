#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/certificate_verifier_calculator.py --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/complexity_class_claim_calculator.py --output-dir outputs/json
