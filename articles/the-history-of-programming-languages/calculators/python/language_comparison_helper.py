from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare two language traditions using history scores.")
parser.add_argument("--first", type=str, required=True)
parser.add_argument("--first-score", type=float, required=True)
parser.add_argument("--second", type=str, required=True)
parser.add_argument("--second-score", type=float, required=True)
args = parser.parse_args()

diff = args.first_score - args.second_score
print(f"first={args.first}")
print(f"second={args.second}")
print(f"score_difference_first_minus_second={diff:.6f}")
print("note=scores are interpretive teaching values, not empirical rankings")
