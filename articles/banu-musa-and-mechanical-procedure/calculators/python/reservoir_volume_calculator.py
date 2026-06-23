from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Simple rectangular reservoir volume.")
parser.add_argument("--length", type=float, required=True)
parser.add_argument("--width", type=float, required=True)
parser.add_argument("--height", type=float, required=True)
args = parser.parse_args()

if args.length < 0 or args.width < 0 or args.height < 0:
    raise SystemExit("dimensions must be nonnegative")
volume = args.length * args.width * args.height
print(f"reservoir_volume={volume:.6f}")
