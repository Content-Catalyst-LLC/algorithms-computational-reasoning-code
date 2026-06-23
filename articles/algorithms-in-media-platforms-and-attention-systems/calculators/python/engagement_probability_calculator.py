from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compute a simple logistic engagement probability.")
parser.add_argument("--linear-score", type=float, required=True)
args = parser.parse_args()

probability = 1.0 / (1.0 + math.exp(-args.linear_score))
print(f"engagement_probability={probability:.6f}")
