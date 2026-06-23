from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Simulate simple negative feedback toward a target.")
parser.add_argument("--initial", type=float, required=True)
parser.add_argument("--target", type=float, required=True)
parser.add_argument("--gain", type=float, default=0.2)
parser.add_argument("--steps", type=int, default=10)
args = parser.parse_args()

x = args.initial
trace = []
for t in range(args.steps):
    error = x - args.target
    x = x - args.gain * error
    trace.append({"t": t + 1, "state": round(x, 6), "error": round(error, 6)})
print("final_state=" + str(round(x, 6)))
print("trace=" + str(trace))
