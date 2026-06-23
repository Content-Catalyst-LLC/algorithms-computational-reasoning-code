from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Estimate maximum binary-search halving steps for n sorted items.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n <= 0:
    print("binary_search_steps=0")
else:
    print(f"binary_search_steps={math.ceil(math.log2(args.n + 1))}")
