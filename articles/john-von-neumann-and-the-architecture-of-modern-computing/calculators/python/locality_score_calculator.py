from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate locality from repeated memory addresses.")
parser.add_argument("--addresses", type=str, required=True, help="Comma-separated addresses")
args = parser.parse_args()

addresses = [x.strip() for x in args.addresses.split(",") if x.strip()]
if not addresses:
    raise SystemExit("provide at least one address")
unique = len(set(addresses))
score = 1.0 - ((unique - 1) / max(len(addresses) - 1, 1))
print(f"access_count={len(addresses)}")
print(f"unique_addresses={unique}")
print(f"locality_score={score:.6f}")
