from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Distribute a total by relative weights. Educational only; not legal advice.")
parser.add_argument("--total", type=float, required=True)
parser.add_argument("--weights", type=str, required=True, help="Comma-separated positive weights, e.g. 2,1,1")
args = parser.parse_args()

weights = [float(x.strip()) for x in args.weights.split(",") if x.strip()]
if not weights or any(w <= 0 for w in weights):
    raise SystemExit("weights must be comma-separated positive numbers")
weight_sum = sum(weights)
for idx, weight in enumerate(weights, start=1):
    share = args.total * weight / weight_sum
    print(f"share_{idx}={share:.6f}")
print(f"check_total={sum(args.total * w / weight_sum for w in weights):.6f}")
