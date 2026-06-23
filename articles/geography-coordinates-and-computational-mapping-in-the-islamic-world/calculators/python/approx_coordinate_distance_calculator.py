from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Approximate distance between nearby coordinates using equirectangular approximation.")
parser.add_argument("--lat1", type=float, required=True)
parser.add_argument("--lon1", type=float, required=True)
parser.add_argument("--lat2", type=float, required=True)
parser.add_argument("--lon2", type=float, required=True)
parser.add_argument("--radius-km", type=float, default=6371.0)
args = parser.parse_args()

phi1 = math.radians(args.lat1)
phi2 = math.radians(args.lat2)
dphi = math.radians(args.lat2 - args.lat1)
dlambda = math.radians(args.lon2 - args.lon1)
phi_bar = (phi1 + phi2) / 2.0
distance = args.radius_km * math.sqrt(dphi**2 + (math.cos(phi_bar) * dlambda)**2)
print(f"approx_distance_km={distance:.6f}")
