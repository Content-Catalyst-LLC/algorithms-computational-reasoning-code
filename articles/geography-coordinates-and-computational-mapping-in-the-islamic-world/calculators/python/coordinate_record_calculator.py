from __future__ import annotations

import argparse
import json

parser = argparse.ArgumentParser(description="Create a structured synthetic place-coordinate record.")
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--lat", type=float, required=True)
parser.add_argument("--lon", type=float, required=True)
parser.add_argument("--region", type=str, default="unspecified")
parser.add_argument("--feature-type", type=str, default="place")
args = parser.parse_args()

record = {
    "name": args.name,
    "latitude": args.lat,
    "longitude": args.lon,
    "region": args.region,
    "feature_type": args.feature_type,
}
print(json.dumps(record, indent=2, sort_keys=True))
