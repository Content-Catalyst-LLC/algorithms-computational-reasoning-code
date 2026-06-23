from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compare n log n and n^2 costs for selected n.")
parser.add_argument("--sizes", type=str, default="10,100,1000,10000")
args = parser.parse_args()

for item in args.sizes.split(","):
    n = int(item.strip())
    print(f"n={n}, n_log2_n={n*math.log2(n):.6f}, n_squared={n*n}")
