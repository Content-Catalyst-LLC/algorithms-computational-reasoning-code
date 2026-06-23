from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute mutual information for a 2x2 joint distribution.")
parser.add_argument("--p00", type=float, required=True)
parser.add_argument("--p01", type=float, required=True)
parser.add_argument("--p10", type=float, required=True)
parser.add_argument("--p11", type=float, required=True)
args = parser.parse_args()

joint = [[args.p00, args.p01], [args.p10, args.p11]]
total = sum(sum(row) for row in joint)
if total <= 0:
    raise SystemExit("joint probabilities must sum positive")
joint = [[x / total for x in row] for row in joint]
px = [sum(joint[i][j] for j in range(2)) for i in range(2)]
py = [sum(joint[i][j] for i in range(2)) for j in range(2)]

mi = 0.0
for i in range(2):
    for j in range(2):
        p = joint[i][j]
        if p > 0:
            mi += p * math.log2(p / (px[i] * py[j]))
print(f"mutual_information_bits={mi:.9f}")
