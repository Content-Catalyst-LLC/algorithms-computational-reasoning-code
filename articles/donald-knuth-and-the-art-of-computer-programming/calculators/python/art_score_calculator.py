from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Knuth algorithmic art.")
for name in [
    "algorithm-analysis", "exposition", "mathematical-rigor", "historical-depth",
    "implementation-relevance", "typography-relevance", "literate-programming",
    "pedagogy", "maintainability", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.algorithm_analysis +
    args.exposition +
    args.mathematical_rigor +
    args.historical_depth +
    args.implementation_relevance +
    args.typography_relevance +
    args.literate_programming +
    args.pedagogy +
    args.maintainability +
    args.governance_caution
) / 10.0
print(f"art_score={score:.6f}")
