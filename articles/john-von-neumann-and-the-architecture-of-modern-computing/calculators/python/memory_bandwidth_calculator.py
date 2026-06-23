from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate transfer time from bytes and bandwidth.")
parser.add_argument("--bytes", type=float, required=True)
parser.add_argument("--gb-per-second", type=float, required=True)
args = parser.parse_args()

if args.gb_per_second <= 0:
    raise SystemExit("bandwidth must be positive")

seconds = args.bytes / (args.gb_per_second * 1_000_000_000)
print(f"transfer_seconds={seconds:.9f}")
print(f"transfer_milliseconds={seconds * 1000:.6f}")
