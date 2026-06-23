from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute predicted value as mean value plus correction.")
parser.add_argument("--mean-value", type=float, required=True)
parser.add_argument("--correction", type=float, required=True)
args = parser.parse_args()

predicted = args.mean_value + args.correction
print(f"predicted={predicted:.6f}")
