from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Convert real-world distance to map distance under representative fraction scale.")
parser.add_argument("--real-distance-km", type=float, required=True)
parser.add_argument("--scale-denominator", type=float, required=True, help="For 1:1000000, pass 1000000")
args = parser.parse_args()

if args.real_distance_km < 0:
    raise SystemExit("real distance must be nonnegative")
if args.scale_denominator <= 0:
    raise SystemExit("scale denominator must be positive")

real_cm = args.real_distance_km * 100000.0
map_cm = real_cm / args.scale_denominator
print(f"map_distance_cm={map_cm:.6f}")
