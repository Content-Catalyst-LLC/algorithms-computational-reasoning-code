from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute approximate initial bearing between two coordinate points.")
parser.add_argument("--lat1", type=float, required=True)
parser.add_argument("--lon1", type=float, required=True)
parser.add_argument("--lat2", type=float, required=True)
parser.add_argument("--lon2", type=float, required=True)
args = parser.parse_args()

lat1 = math.radians(args.lat1)
lat2 = math.radians(args.lat2)
dlon = math.radians(args.lon2 - args.lon1)
x = math.sin(dlon) * math.cos(lat2)
y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
bearing = (math.degrees(math.atan2(x, y)) + 360.0) % 360.0
print(f"bearing_degrees={bearing:.6f}")
