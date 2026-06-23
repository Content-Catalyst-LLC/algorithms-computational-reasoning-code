from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score technical vocabulary mapping coverage.")
parser.add_argument("--mapped-terms", type=float, required=True)
parser.add_argument("--total-terms", type=float, required=True)
args = parser.parse_args()

if args.total_terms <= 0:
    raise SystemExit("total-terms must be positive")
score = args.mapped_terms / args.total_terms
print(f"vocabulary_mapping_coverage={score:.6f}")
