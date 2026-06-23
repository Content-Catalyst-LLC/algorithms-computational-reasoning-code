#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/imagination_score_calculator.py" \
  --programming-structure 0.98 --symbolic-generality 0.86 --machine-orientation 0.98 --mathematical-grounding 0.94 --imaginative-reach 0.86 --limit-awareness 0.76 --collaboration 0.92 --authorship 0.90 --modern-resonance 0.98 --ai-caution 0.82 > "$OUT/imagination_score_smoke.txt"

python3 "$ROOT/calculators/python/bernoulli_number_calculator.py" \
  --n 8 > "$OUT/bernoulli_number_smoke.txt"

python3 "$ROOT/calculators/python/operation_sequence_calculator.py" \
  --operations multiply,subtract,store,repeat > "$OUT/operation_sequence_smoke.txt"

python3 "$ROOT/calculators/python/symbolic_generality_calculator.py" \
  --has-representation true --has-relations true --has-operations true --has-patterns true --has-outputs true > "$OUT/symbolic_generality_smoke.txt"

python3 "$ROOT/calculators/python/machine_limit_calculator.py" \
  --claim "The machine independently understands and originates on its own" > "$OUT/machine_limit_smoke.txt"

python3 "$ROOT/calculators/python/authorship_credit_calculator.py" \
  --has-translation true --has-notes true --has-interpretation true --has-collaboration true --has-procedure true > "$OUT/authorship_credit_smoke.txt"

python3 "$ROOT/calculators/python/lovelace_myth_caution_calculator.py" \
  --claim "Ada was only a translator and wrote modern code" > "$OUT/lovelace_myth_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/lovelace_imagination_score.R" 0.98 0.86 0.98 0.94 0.86 0.76 0.92 0.90 0.98 0.82 > "$OUT/lovelace_imagination_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/lovelace_imagination_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
