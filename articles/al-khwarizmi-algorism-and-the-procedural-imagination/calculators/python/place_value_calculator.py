from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute positional place-value contribution.")
parser.add_argument("--digit", type=int, required=True)
parser.add_argument("--base", type=int, default=10)
parser.add_argument("--position", type=int, required=True, help="Zero-indexed position from the right.")
args = parser.parse_args()

if args.base <= 1:
    raise SystemExit("base must be greater than 1")
if not (0 <= args.digit < args.base):
    raise SystemExit("digit must satisfy 0 <= digit < base")
value = args.digit * (args.base ** args.position)
print(f"place_value={value}")
