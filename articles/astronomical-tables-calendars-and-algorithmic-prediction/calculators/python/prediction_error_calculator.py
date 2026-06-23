from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compare predicted and observed values.")
parser.add_argument("--predicted", type=float, required=True)
parser.add_argument("--observed", type=float, required=True)
args = parser.parse_args()

error = args.predicted - args.observed
absolute_error = abs(error)
print(f"error={error:.6f}")
print(f"absolute_error={absolute_error:.6f}")
