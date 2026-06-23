from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compare common asymptotic growth values for n.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

n = args.n
if n <= 0:
    raise SystemExit("n must be positive")

print(f"log2_n={math.log2(n):.6f}")
print(f"n={n}")
print(f"n_log2_n={n * math.log2(n):.6f}")
print(f"n_squared={n*n}")
print(f"two_to_n={2**n if n <= 30 else 'too_large_for_teaching_output'}")
