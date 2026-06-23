from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute trapezoid area from bases and height.")
parser.add_argument("--base-a", type=float, required=True)
parser.add_argument("--base-b", type=float, required=True)
parser.add_argument("--height", type=float, required=True)
args = parser.parse_args()

if args.base_a < 0 or args.base_b < 0 or args.height < 0:
    raise SystemExit("dimensions must be nonnegative")
area = ((args.base_a + args.base_b) * args.height) / 2.0
print(f"area={area:.6f}")
