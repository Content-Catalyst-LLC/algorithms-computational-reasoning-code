from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a synthetic climate band from latitude.")
parser.add_argument("--latitude", type=float, required=True)
args = parser.parse_args()

lat = args.latitude
if not -90 <= lat <= 90:
    raise SystemExit("latitude must be between -90 and 90")

abs_lat = abs(lat)
if abs_lat < 23.5:
    band = "tropical"
elif abs_lat < 45:
    band = "subtropical_mid_latitude"
elif abs_lat < 66.5:
    band = "temperate_high_latitude"
else:
    band = "polar"

print(f"climate_band={band}")
