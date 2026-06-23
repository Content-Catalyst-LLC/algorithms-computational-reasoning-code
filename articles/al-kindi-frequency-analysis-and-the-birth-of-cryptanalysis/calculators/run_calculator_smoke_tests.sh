#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/frequency_table_calculator.py" \
  --text "THIS IS A TOY CLASSICAL CIPHER EXAMPLE" > "$OUT/frequency_table_smoke.csv"

python3 "$ROOT/calculators/python/relative_frequency_calculator.py" \
  --count 7 --total 40 > "$OUT/relative_frequency_smoke.txt"

python3 "$ROOT/calculators/python/caesar_demo_calculator.py" \
  --text "HELLO" --shift 3 --mode encrypt > "$OUT/caesar_encrypt_smoke.txt"

python3 "$ROOT/calculators/python/caesar_demo_calculator.py" \
  --text "KHOOR" --shift 3 --mode decrypt > "$OUT/caesar_decrypt_smoke.txt"

python3 "$ROOT/calculators/python/substitution_apply_calculator.py" \
  --text "ab cab" --mapping "a=x,b=y,c=z" > "$OUT/substitution_apply_smoke.txt"

python3 "$ROOT/calculators/python/hypothesis_score_calculator.py" \
  --observed "e,t,a,o,i" --expected "e,t,a,i,o" --top-k 5 > "$OUT/hypothesis_score_smoke.txt"

python3 "$ROOT/calculators/python/sample_size_warning_calculator.py" \
  --text "SHORT TOY TEXT" --minimum 100 > "$OUT/sample_size_warning_smoke.txt"

python3 "$ROOT/calculators/python/cryptanalysis_score_calculator.py" \
  --linguistic-evidence 0.96 --counting-procedure 0.98 --inferential-structure 0.90 --cryptanalytic-relevance 0.94 --historical-significance 0.94 --ethical-caution 0.82 --modern-resonance 0.94 > "$OUT/cryptanalysis_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/cryptanalysis_score.R" 0.96 0.98 0.90 0.94 0.94 0.82 0.94 > "$OUT/cryptanalysis_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/cryptanalysis_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
