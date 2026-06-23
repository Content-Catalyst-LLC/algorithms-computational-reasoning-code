from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute Shannon entropy in bits from comma-separated probabilities.")
parser.add_argument("--probabilities", type=str, required=True)
args = parser.parse_args()

probs = [float(x.strip()) for x in args.probabilities.split(",") if x.strip()]
if any(p < 0 for p in probs):
    raise SystemExit("probabilities must be nonnegative")
total = sum(probs)
if total <= 0:
    raise SystemExit("probabilities must sum to a positive value")
probs = [p / total for p in probs]
entropy = -sum(p * math.log2(p) for p in probs if p > 0)
print(f"entropy_bits={entropy:.9f}")
