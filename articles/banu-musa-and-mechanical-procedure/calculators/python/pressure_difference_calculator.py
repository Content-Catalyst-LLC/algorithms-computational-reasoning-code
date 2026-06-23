from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Basic hydrostatic pressure difference concept: delta_p = density * gravity * height.")
parser.add_argument("--density", type=float, default=1000.0)
parser.add_argument("--gravity", type=float, default=9.81)
parser.add_argument("--height", type=float, required=True)
args = parser.parse_args()

if args.density < 0 or args.gravity < 0 or args.height < 0:
    raise SystemExit("density, gravity, and height must be nonnegative")
delta_p = args.density * args.gravity * args.height
print(f"pressure_difference={delta_p:.6f}")
