#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/coordinate_record_calculator.py" \
  --name "Synthetic City" --lat 33.3 --lon 44.4 --region "synthetic-region" --feature-type city > "$OUT/coordinate_record_smoke.json"

python3 "$ROOT/calculators/python/approx_coordinate_distance_calculator.py" \
  --lat1 33.3 --lon1 44.4 --lat2 34.0 --lon2 45.0 > "$OUT/approx_distance_smoke.txt"

python3 "$ROOT/calculators/python/route_distance_calculator.py" \
  --segments 12,20,7.5 > "$OUT/route_distance_smoke.txt"

python3 "$ROOT/calculators/python/bearing_calculator.py" \
  --lat1 33.3 --lon1 44.4 --lat2 21.4 --lon2 39.8 > "$OUT/bearing_smoke.txt"

python3 "$ROOT/calculators/python/climate_band_classifier.py" \
  --latitude 33.3 > "$OUT/climate_band_smoke.txt"

python3 "$ROOT/calculators/python/projection_scale_calculator.py" \
  --real-distance-km 100 --scale-denominator 1000000 > "$OUT/projection_scale_smoke.txt"

python3 "$ROOT/calculators/python/mapping_score_calculator.py" \
  --spatial-representation 0.98 --coordinate-structure 0.98 --procedural-clarity 0.88 --institutional-use 0.86 --correction-awareness 0.90 --transmission-importance 0.90 --modern-resonance 0.96 > "$OUT/mapping_score_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/mapping_score.R" 0.98 0.98 0.88 0.86 0.90 0.90 0.96 > "$OUT/mapping_score_r_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/mapping_score_r_smoke.txt"
fi

echo "Calculator smoke tests complete."
