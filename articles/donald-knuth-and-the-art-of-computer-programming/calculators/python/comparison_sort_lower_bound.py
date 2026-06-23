from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute log2(n!) lower-bound intuition for comparison sorting.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n < 0:
    raise SystemExit("n must be nonnegative")

value = math.log2(math.factorial(args.n)) if args.n > 1 else 0.0
print(f"log2_factorial_lower_bound={value:.6f}")
