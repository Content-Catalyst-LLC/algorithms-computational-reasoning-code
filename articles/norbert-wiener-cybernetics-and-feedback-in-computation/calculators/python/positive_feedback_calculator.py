from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Simulate simple positive feedback amplification.")
parser.add_argument("--initial", type=float, required=True)
parser.add_argument("--rate", type=float, default=0.1)
parser.add_argument("--steps", type=int, default=10)
args = parser.parse_args()

x = args.initial
trace = []
for t in range(args.steps):
    x = (1 + args.rate) * x
    trace.append({"t": t + 1, "state": round(x, 6)})
print("final_state=" + str(round(x, 6)))
print("trace=" + str(trace))
