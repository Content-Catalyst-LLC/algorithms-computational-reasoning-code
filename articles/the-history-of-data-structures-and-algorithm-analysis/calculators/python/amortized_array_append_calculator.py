from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Estimate dynamic-array append cost under doubling capacity.")
parser.add_argument("--appends", type=int, required=True)
args = parser.parse_args()

if args.appends <= 0:
    raise SystemExit("appends must be positive")
copies = 0
capacity = 1
size = 0
for _ in range(args.appends):
    if size == capacity:
        copies += size
        capacity *= 2
    size += 1
total_cost = args.appends + copies
amortized = total_cost / args.appends
print(f"appends={args.appends}")
print(f"copy_cost={copies}")
print(f"total_cost={total_cost}")
print(f"amortized_cost={amortized:.6f}")
print(f"final_capacity={capacity}")
