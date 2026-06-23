from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute next synthetic cycle marker from date number, cycle length, and adjustment.")
parser.add_argument("--date", type=float, required=True)
parser.add_argument("--cycle-length", type=float, required=True)
parser.add_argument("--adjustment", type=float, default=0.0)
args = parser.parse_args()

if args.cycle_length <= 0:
    raise SystemExit("cycle length must be positive")
next_date = args.date + args.cycle_length + args.adjustment
print(f"next_date={next_date:.6f}")
