from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute context-adjusted productivity metric.")
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--quality", type=float, required=True)
parser.add_argument("--reliability", type=float, required=True)
parser.add_argument("--context-penalty", type=float, default=0.0)
parser.add_argument("--weights", type=str, default="0.35,0.35,0.20,0.10")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")
w = [item / total for item in weights]
score = w[0] * args.quantity + w[1] * args.quality + w[2] * args.reliability - w[3] * args.context_penalty
print(f"productivity_metric={score:.6f}")
