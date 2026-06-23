from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy valve gate: pass flow only if valve is open.")
parser.add_argument("--input-flow", type=float, required=True)
parser.add_argument("--valve-open", choices=["true", "false"], required=True)
args = parser.parse_args()

if args.input_flow < 0:
    raise SystemExit("input-flow must be nonnegative")
output = args.input_flow if args.valve_open == "true" else 0.0
print(f"output_flow={output:.6f}")
