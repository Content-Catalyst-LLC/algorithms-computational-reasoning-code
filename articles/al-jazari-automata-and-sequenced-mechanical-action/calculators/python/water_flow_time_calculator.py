from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Conceptual water flow time: time = volume / flow_rate.")
parser.add_argument("--volume", type=float, required=True)
parser.add_argument("--flow-rate", type=float, required=True)
args = parser.parse_args()

if args.volume < 0:
    raise SystemExit("volume must be nonnegative")
if args.flow_rate <= 0:
    raise SystemExit("flow-rate must be positive")
print(f"flow_time={args.volume / args.flow_rate:.6f}")
