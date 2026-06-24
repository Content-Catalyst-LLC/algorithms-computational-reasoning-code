from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Compute a binary threshold-unit output.")
parser.add_argument("--inputs", required=True, help="Comma-separated binary inputs, e.g. 1,0,1")
parser.add_argument("--weights", required=True, help="Comma-separated integer weights, e.g. 1,1,1")
parser.add_argument("--threshold", type=int, required=True)
args = parser.parse_args()

inputs = [int(x.strip()) for x in args.inputs.split(",") if x.strip()]
weights = [int(w.strip()) for w in args.weights.split(",") if w.strip()]
if len(inputs) != len(weights):
    raise SystemExit("inputs and weights must have the same length")
total = sum(x * w for x, w in zip(inputs, weights))
output = 1 if total >= args.threshold else 0
print(f"weighted_sum={total}")
print(f"threshold={args.threshold}")
print(f"output={output}")
