from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Reset a toy state to initial condition after a cycle.")
parser.add_argument("--current-state", type=float, required=True)
parser.add_argument("--initial-state", type=float, default=0.0)
parser.add_argument("--reset", choices=["true", "false"], required=True)
args = parser.parse_args()

state = args.initial_state if args.reset == "true" else args.current_state
print(f"state={state:.6f}")
