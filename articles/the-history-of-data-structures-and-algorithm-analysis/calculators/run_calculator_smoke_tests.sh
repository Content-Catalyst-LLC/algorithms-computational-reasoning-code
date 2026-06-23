#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/history_score_calculator.py" \
  --representation-centrality 0.96 --operation-clarity 0.92 --memory-awareness 0.98 --time-analysis 0.88 --space-analysis 0.96 --scale-sensitivity 0.90 --abstraction-maturity 0.82 --systems-relevance 0.96 --historical-influence 0.98 --governance-caution 0.86 > "$OUT/history_score_smoke.txt"

python3 "$ROOT/calculators/python/growth_rate_calculator.py" \
  --n 1000 > "$OUT/growth_rate_smoke.txt"

python3 "$ROOT/calculators/python/binary_search_steps_calculator.py" \
  --n 100 > "$OUT/binary_search_steps_smoke.txt"

python3 "$ROOT/calculators/python/graph_memory_calculator.py" \
  --nodes 1000 --edges 4000 > "$OUT/graph_memory_smoke.txt"

python3 "$ROOT/calculators/python/hash_table_load_calculator.py" \
  --items 750 --buckets 1000 > "$OUT/hash_table_load_smoke.txt"

python3 "$ROOT/calculators/python/amortized_array_append_calculator.py" \
  --appends 100 > "$OUT/amortized_array_append_smoke.txt"

python3 "$ROOT/calculators/python/priority_queue_operation_calculator.py" \
  --n 1000 > "$OUT/priority_queue_operation_smoke.txt"

python3 "$ROOT/calculators/python/ai_structure_audit_calculator.py" \
  --claim "Embeddings are neutral and no provenance needed" > "$OUT/ai_structure_audit_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/history_score.R" 0.96 0.92 0.98 0.88 0.96 0.90 0.82 0.96 0.98 0.86 > "$OUT/history_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/history_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
