from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute weighted maintenance priority.")
parser.add_argument("--condition", type=float, required=True)
parser.add_argument("--criticality", type=float, required=True)
parser.add_argument("--consequence", type=float, required=True)
parser.add_argument("--equity", type=float, required=True)
parser.add_argument("--weights", type=str, default="0.30,0.30,0.25,0.15")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")
w = [item / total for item in weights]
priority = w[0] * args.condition + w[1] * args.criticality + w[2] * args.consequence + w[3] * args.equity
print(f"maintenance_priority={priority:.6f}")
