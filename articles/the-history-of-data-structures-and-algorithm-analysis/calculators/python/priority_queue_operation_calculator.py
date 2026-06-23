from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Estimate heap priority-queue operation cost.")
parser.add_argument("--n", type=int, required=True)
args = parser.parse_args()

if args.n <= 0:
    raise SystemExit("n must be positive")
print(f"heap_insert_or_extract_cost_log2={math.ceil(math.log2(args.n + 1))}")
