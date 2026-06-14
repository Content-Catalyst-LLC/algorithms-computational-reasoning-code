#!/usr/bin/env bash
set -euo pipefail

echo "Running Algorithms & Computational Reasoning smoke test..."

required_dirs=(
  articles python r julia sql haskell rust go c cpp fortran java typescript prolog racket docs data outputs notebooks tests canvas shared
)

for d in "${required_dirs[@]}"; do
  if [[ ! -d "$d" ]]; then
    echo "Missing directory: $d" >&2
    exit 1
  fi
done

article_count=$(find articles -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
echo "Article folders: $article_count"

if [[ "$article_count" -lt 100 ]]; then
  echo "Expected at least 100 article folders." >&2
  exit 1
fi

python3 scripts/validate_article_manifest.py

echo "Smoke test complete."
