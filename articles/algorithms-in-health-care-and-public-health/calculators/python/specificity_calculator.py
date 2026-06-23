from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute specificity = TN / (TN + FP).")
parser.add_argument("--tn", type=float, required=True)
parser.add_argument("--fp", type=float, required=True)
args = parser.parse_args()

denominator = args.tn + args.fp
if denominator <= 0:
    raise SystemExit("tn + fp must be positive")
score = args.tn / denominator
print(f"specificity={score:.6f}")
