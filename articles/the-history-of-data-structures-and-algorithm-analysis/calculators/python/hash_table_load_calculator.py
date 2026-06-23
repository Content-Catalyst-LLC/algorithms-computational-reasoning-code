from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate hash-table load factor and rough performance-risk status.")
parser.add_argument("--items", type=int, required=True)
parser.add_argument("--buckets", type=int, required=True)
args = parser.parse_args()

if args.buckets <= 0:
    raise SystemExit("buckets must be positive")
load = args.items / args.buckets
if load <= 0.70:
    status = "low_load"
elif load <= 1.00:
    status = "moderate_load"
else:
    status = "high_collision_risk"
print(f"load_factor={load:.6f}")
print(f"status={status}")
