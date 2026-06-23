from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute weighted learning recommendation score.")
parser.add_argument("--relevance", type=float, required=True)
parser.add_argument("--readiness", type=float, required=True)
parser.add_argument("--interest", type=float, required=True)
parser.add_argument("--support", type=float, required=True)
parser.add_argument("--weights", type=str, default="0.35,0.25,0.20,0.20")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")
w = [item / total for item in weights]
score = w[0] * args.relevance + w[1] * args.readiness + w[2] * args.interest + w[3] * args.support
print(f"recommendation_score={score:.6f}")
