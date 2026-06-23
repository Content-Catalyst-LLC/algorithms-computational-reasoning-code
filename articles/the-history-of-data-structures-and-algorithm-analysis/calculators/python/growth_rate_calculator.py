from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compare common algorithmic growth rates.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n <= 0:
    raise SystemExit("n must be positive")
n = args.n
print(f"n={n}")
print(f"O(1)={1}")
print(f"O(log2 n)={math.log2(n):.6f}")
print(f"O(n)={n}")
print(f"O(n log2 n)={n * math.log2(n):.6f}")
print(f"O(n^2)={n * n}")
