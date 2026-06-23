from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute rectangle area.")
parser.add_argument("--length", type=float, required=True)
parser.add_argument("--width", type=float, required=True)
args = parser.parse_args()

if args.length < 0 or args.width < 0:
    raise SystemExit("dimensions must be nonnegative")
area = args.length * args.width
print(f"area={area:.6f}")
