from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute scenario stress loss.")
parser.add_argument("--exposure", type=float, required=True)
parser.add_argument("--shock", type=float, required=True, help="Negative shock magnitude as positive fraction")
parser.add_argument("--recovery", type=float, default=0.0, help="Recovery fraction")
args = parser.parse_args()

loss = args.exposure * args.shock * (1.0 - args.recovery)
print(f"stress_loss={loss:.6f}")
