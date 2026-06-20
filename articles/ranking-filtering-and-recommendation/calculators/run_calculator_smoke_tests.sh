#!/usr/bin/env bash
set -euo pipefail
ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "${ARTICLE_DIR}/python/calculators/ranking_score_calculator.py" --text-match 0.92 --quality 0.88 --freshness 0.60 --diversity-bonus 0.35 --risk-penalty 0.04
python3 "${ARTICLE_DIR}/python/calculators/similarity_recommendation_calculator.py" --left 0.8,0.2,0.4 --right 0.7,0.3,0.5
