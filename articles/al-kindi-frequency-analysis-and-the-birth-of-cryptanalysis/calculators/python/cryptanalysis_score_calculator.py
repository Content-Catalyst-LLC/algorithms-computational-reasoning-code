from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for frequency-analysis cryptanalysis.")
parser.add_argument("--linguistic-evidence", type=float, required=True)
parser.add_argument("--counting-procedure", type=float, required=True)
parser.add_argument("--inferential-structure", type=float, required=True)
parser.add_argument("--cryptanalytic-relevance", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--ethical-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.linguistic_evidence +
    args.counting_procedure +
    args.inferential_structure +
    args.cryptanalytic_relevance +
    args.historical_significance +
    args.ethical_caution +
    args.modern_resonance
) / 7.0
print(f"cryptanalysis_score={score:.6f}")
