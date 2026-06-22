#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/calculators/outputs"
mkdir -p "$OUT"

python3 "$ROOT/calculators/python/metadata_completeness_calculator.py" \
  --present-fields 11 \
  --required-fields 12 > "$OUT/metadata_completeness_smoke.txt"

python3 "$ROOT/calculators/python/architecture_readiness_calculator.py" \
  --metadata 0.92 \
  --taxonomy 0.88 \
  --search 0.86 \
  --link 0.90 \
  --recommendation 0.82 \
  --provenance 0.86 \
  --editorial-review 0.90 > "$OUT/architecture_readiness_smoke.txt"

python3 "$ROOT/calculators/python/maintenance_risk_calculator.py" \
  --metadata 0.92 \
  --link-quality 0.90 \
  --freshness 0.84 \
  --provenance 0.86 > "$OUT/maintenance_risk_smoke.txt"

python3 "$ROOT/calculators/python/weighted_relevance_calculator.py" \
  --text-match 0.80 \
  --semantic-similarity 0.88 \
  --authority 0.78 \
  --freshness 0.74 > "$OUT/weighted_relevance_smoke.txt"

python3 "$ROOT/calculators/python/cosine_similarity_calculator.py" \
  --x "1,2,3" \
  --y "1,2,4" > "$OUT/cosine_similarity_smoke.txt"

python3 "$ROOT/calculators/python/link_recommendation_calculator.py" \
  --semantic-similarity 0.86 \
  --prerequisite-value 0.74 \
  --graph-navigation-value 0.82 > "$OUT/link_recommendation_smoke.txt"

if command -v Rscript >/dev/null 2>&1; then
  Rscript "$ROOT/calculators/r/knowledge_architecture_score.R" 0.92 0.88 0.86 0.90 0.82 0.86 0.84 0.90 > "$OUT/knowledge_architecture_score_smoke.txt"
else
  echo "Rscript not available; skipped R calculator." > "$OUT/knowledge_architecture_score_smoke.txt"
fi

echo "Calculator smoke tests complete."
