from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Apply sin(x) + x^2 over comma-separated x values.")
parser.add_argument("--values", type=str, required=True)
args = parser.parse_args()

values = [float(x.strip()) for x in args.values.split(",") if x.strip()]
for i, x in enumerate(values, start=1):
    y = math.sin(x) + x * x
    print(f"i={i}, x={x:.6f}, y={y:.6f}")
