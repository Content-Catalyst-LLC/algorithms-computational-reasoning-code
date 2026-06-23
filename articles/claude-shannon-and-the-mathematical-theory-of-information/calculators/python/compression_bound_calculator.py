from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Estimate entropy lower bound for expected lossless compression length.")
parser.add_argument("--probabilities", type=str, required=True)
parser.add_argument("--symbols", type=int, required=True)
args = parser.parse_args()

probs = [float(x.strip()) for x in args.probabilities.split(",") if x.strip()]
total = sum(probs)
probs = [p / total for p in probs]
h = -sum(p * math.log2(p) for p in probs if p > 0)
lower_bound = args.symbols * h
print(f"entropy_bits_per_symbol={h:.9f}")
print(f"lower_bound_bits_for_sequence={lower_bound:.6f}")
