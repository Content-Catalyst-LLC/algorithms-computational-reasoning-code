#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"
PYTHONPATH=python python3 python/calculators/graph_search_calculator.py --edge-csv data/synthetic_graph_edges.csv --output-dir outputs/json
PYTHONPATH=python python3 python/calculators/graph_density_calculator.py --edge-csv data/synthetic_graph_edges.csv --output-dir outputs/json
