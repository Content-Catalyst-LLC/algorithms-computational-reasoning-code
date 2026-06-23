from __future__ import annotations

import argparse

SYNTHETIC_TABLE = {
    0: 0.0,
    10: 1.2,
    20: 2.8,
    30: 4.5,
    40: 6.1,
}

parser = argparse.ArgumentParser(description="Retrieve a value from a small synthetic astronomical-style table.")
parser.add_argument("--argument", type=int, required=True)
args = parser.parse_args()

if args.argument not in SYNTHETIC_TABLE:
    raise SystemExit(f"argument not found; available={sorted(SYNTHETIC_TABLE)}")
print(f"value={SYNTHETIC_TABLE[args.argument]:.6f}")
