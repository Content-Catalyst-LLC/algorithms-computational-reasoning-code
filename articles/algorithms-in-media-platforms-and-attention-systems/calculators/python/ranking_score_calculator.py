from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute a platform ranking score.")
parser.add_argument("--relevance", type=float, required=True)
parser.add_argument("--engagement", type=float, required=True)
parser.add_argument("--freshness", type=float, required=True)
parser.add_argument("--risk", type=float, required=True)
parser.add_argument("--weights", type=str, default="0.40,0.30,0.20,0.10")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain exactly four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")

w = [item / total for item in weights]
score = w[0] * args.relevance + w[1] * args.engagement + w[2] * args.freshness - w[3] * args.risk
print(f"ranking_score={score:.6f}")
