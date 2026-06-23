#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/architecture_score_calculator.py" \
  --stored-program 0.98 --memory-organization 0.96 --control-structure 0.94 --program-as-data 0.98 --implementation-influence 0.96 --bottleneck-awareness 0.82 --collaboration-context 0.86 --software-relevance 0.98 --ai-infrastructure 0.90 --governance-caution 0.88 > "$OUT/architecture_score_smoke.txt"

python3 "$ROOT/calculators/python/fetch_execute_cycle.py" \
  --program "LOAD 2,ADD 3,STORE 0,HALT" > "$OUT/fetch_execute_smoke.txt"

python3 "$ROOT/calculators/python/memory_bandwidth_calculator.py" \
  --bytes 1000000000 --gb-per-second 50 > "$OUT/memory_bandwidth_smoke.txt"

python3 "$ROOT/calculators/python/bottleneck_calculator.py" \
  --compute-ops-per-sec 1000000000000 --bytes-per-op 16 --memory-gb-per-sec 50 > "$OUT/bottleneck_smoke.txt"

python3 "$ROOT/calculators/python/program_as_data_classifier.py" \
  --case compiler > "$OUT/program_as_data_smoke.txt"

python3 "$ROOT/calculators/python/branch_trace_calculator.py" \
  --n 3 > "$OUT/branch_trace_smoke.txt"

python3 "$ROOT/calculators/python/locality_score_calculator.py" \
  --addresses 1,2,3,3,3,4,4,4 > "$OUT/locality_score_smoke.txt"

python3 "$ROOT/calculators/python/architecture_governance_caution_calculator.py" \
  --claim "Architecture is irrelevant and no logs needed" > "$OUT/architecture_governance_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/architecture_score.R" 0.98 0.96 0.94 0.98 0.96 0.82 0.86 0.98 0.90 0.88 > "$OUT/architecture_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/architecture_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
