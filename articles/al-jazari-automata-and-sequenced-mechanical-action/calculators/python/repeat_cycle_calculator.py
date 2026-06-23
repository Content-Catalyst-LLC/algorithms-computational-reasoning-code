from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute repeated-cycle output count.")
parser.add_argument("--cycles", type=int, required=True)
parser.add_argument("--outputs-per-cycle", type=int, required=True)
args = parser.parse_args()

if args.cycles < 0 or args.outputs_per_cycle < 0:
    raise SystemExit("cycles and outputs-per-cycle must be nonnegative")
print(f"total_outputs={args.cycles * args.outputs_per_cycle}")
