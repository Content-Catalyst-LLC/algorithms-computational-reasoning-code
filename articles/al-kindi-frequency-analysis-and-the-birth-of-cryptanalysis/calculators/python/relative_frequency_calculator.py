from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute relative frequency as count divided by total.")
parser.add_argument("--count", type=float, required=True)
parser.add_argument("--total", type=float, required=True)
args = parser.parse_args()

if args.total <= 0:
    raise SystemExit("total must be positive")
freq = args.count / args.total
print(f"relative_frequency={freq:.6f}")
