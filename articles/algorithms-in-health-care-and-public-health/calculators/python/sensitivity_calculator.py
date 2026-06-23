from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute sensitivity = TP / (TP + FN).")
parser.add_argument("--tp", type=float, required=True)
parser.add_argument("--fn", type=float, required=True)
args = parser.parse_args()

denominator = args.tp + args.fn
if denominator <= 0:
    raise SystemExit("tp + fn must be positive")
score = args.tp / denominator
print(f"sensitivity={score:.6f}")
