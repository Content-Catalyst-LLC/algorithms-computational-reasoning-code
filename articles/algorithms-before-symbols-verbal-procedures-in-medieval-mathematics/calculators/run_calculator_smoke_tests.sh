#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/instruction_sequence_counter.py" \
  --procedure "take the number; double it; add the adjustment; check the result" > "$OUT/instruction_sequence_smoke.txt"

python3 "$ROOT/calculators/python/problem_classification_calculator.py" \
  --domain algebra > "$OUT/problem_classification_smoke.txt"

python3 "$ROOT/calculators/python/worked_example_trace_calculator.py" \
  --input 5 --adjustment 3 --target 13 > "$OUT/worked_example_trace_smoke.txt"

python3 "$ROOT/calculators/python/table_interpolation_calculator.py" \
  --x0 10 --y0 100 --x1 20 --y1 140 --x 15 > "$OUT/table_interpolation_smoke.txt"

python3 "$ROOT/calculators/python/symbolic_compression_calculator.py" \
  --verbal "take the thing and multiply it by itself" --symbolic "x^2" > "$OUT/symbolic_compression_smoke.txt"

python3 "$ROOT/calculators/python/verbal_procedure_score_calculator.py" \
  --procedural-clarity 0.90 --representation-dependence 0.86 --pedagogical-value 0.88 --transmission-importance 0.90 --practical-use 0.82 --modern-resonance 0.88 > "$OUT/verbal_procedure_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/verbal_procedure_score.R" 0.90 0.86 0.88 0.90 0.82 0.88 > "$OUT/verbal_procedure_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/verbal_procedure_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
