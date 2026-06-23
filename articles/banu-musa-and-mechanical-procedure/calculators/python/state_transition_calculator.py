from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy mechanical state transition: next_state = state + input - constraint.")
parser.add_argument("--state", type=float, required=True)
parser.add_argument("--input", type=float, required=True)
parser.add_argument("--constraint", type=float, default=0.0)
args = parser.parse_args()

next_state = args.state + args.input - args.constraint
print(f"next_state={next_state:.6f}")
