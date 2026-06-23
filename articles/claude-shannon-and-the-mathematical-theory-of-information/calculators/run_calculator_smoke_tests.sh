#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/entropy_calculator.py" \
  --probabilities 0.5,0.5 > "$OUT/entropy_smoke.txt"

python3 "$ROOT/calculators/python/information_content_calculator.py" \
  --probability 0.125 > "$OUT/information_content_smoke.txt"

python3 "$ROOT/calculators/python/mutual_information_2x2_calculator.py" \
  --p00 0.4 --p01 0.1 --p10 0.1 --p11 0.4 > "$OUT/mutual_information_smoke.txt"

python3 "$ROOT/calculators/python/channel_capacity_awgn_calculator.py" \
  --bandwidth-hz 1000000 --snr 10 > "$OUT/channel_capacity_smoke.txt"

python3 "$ROOT/calculators/python/compression_bound_calculator.py" \
  --probabilities 0.5,0.25,0.25 --symbols 1000 > "$OUT/compression_bound_smoke.txt"

python3 "$ROOT/calculators/python/redundancy_calculator.py" \
  --alphabet-size 4 --observed-entropy 1.5 > "$OUT/redundancy_smoke.txt"

python3 "$ROOT/calculators/python/error_correction_overhead_calculator.py" \
  --payload-bits 1000 --encoded-bits 1250 > "$OUT/error_correction_overhead_smoke.txt"

python3 "$ROOT/calculators/python/semantic_boundary_caution_calculator.py" \
  --claim "High information means wisdom and entropy proves meaning" > "$OUT/semantic_boundary_caution_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/entropy_calculator.R" 0.5,0.5 > "$OUT/entropy_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/entropy_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
