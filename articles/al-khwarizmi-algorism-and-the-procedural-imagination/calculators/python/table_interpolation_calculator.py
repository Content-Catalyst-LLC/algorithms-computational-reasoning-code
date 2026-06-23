from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Linear interpolation between two tabular values.")
parser.add_argument("--x0", type=float, required=True)
parser.add_argument("--y0", type=float, required=True)
parser.add_argument("--x1", type=float, required=True)
parser.add_argument("--y1", type=float, required=True)
parser.add_argument("--x", type=float, required=True)
args = parser.parse_args()

if args.x1 == args.x0:
    raise SystemExit("x0 and x1 must differ")
t = (args.x - args.x0) / (args.x1 - args.x0)
y = args.y0 + t * (args.y1 - args.y0)
print(f"interpolated_y={y:.6f}")
