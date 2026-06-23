from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute a simple public-value score.")
parser.add_argument("--effectiveness", type=float, required=True)
parser.add_argument("--equity", type=float, required=True)
parser.add_argument("--accountability", type=float, required=True)
parser.add_argument("--harm", type=float, required=True)
parser.add_argument("--weights", type=str, default="0.35,0.30,0.25,0.10")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain exactly four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")
w = [item / total for item in weights]
score = w[0] * args.effectiveness + w[1] * args.equity + w[2] * args.accountability - w[3] * args.harm
print(f"public_value_score={score:.6f}")
