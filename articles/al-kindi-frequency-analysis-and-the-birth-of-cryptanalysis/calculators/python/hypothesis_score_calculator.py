from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score overlap between observed and expected symbol rankings.")
parser.add_argument("--observed", type=str, required=True, help="Comma-separated observed ranking, e.g. x,m,w")
parser.add_argument("--expected", type=str, required=True, help="Comma-separated expected ranking, e.g. e,t,a")
parser.add_argument("--top-k", type=int, default=5)
args = parser.parse_args()

observed = [x.strip().lower() for x in args.observed.split(",") if x.strip()]
expected = [x.strip().lower() for x in args.expected.split(",") if x.strip()]
k = max(1, args.top_k)

observed_top = set(observed[:k])
expected_top = set(expected[:k])
score = len(observed_top & expected_top) / max(1, len(observed_top | expected_top))
print(f"ranking_overlap_score={score:.6f}")
