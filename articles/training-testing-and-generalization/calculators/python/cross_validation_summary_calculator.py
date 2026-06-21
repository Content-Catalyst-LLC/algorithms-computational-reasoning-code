from __future__ import annotations
import argparse
from statistics import mean, pstdev
parser = argparse.ArgumentParser(description="Summarize cross-validation fold scores.")
parser.add_argument("--scores", required=True, help="Comma-separated fold scores, e.g. 0.81,0.79,0.83")
args = parser.parse_args()
values = [float(item.strip()) for item in args.scores.split(',') if item.strip()]
if not values: raise SystemExit("provide at least one score")
print(f"folds={len(values)}")
print(f"mean={mean(values):.6f}")
print(f"population_sd={pstdev(values):.6f}")
print(f"min={min(values):.6f}")
print(f"max={max(values):.6f}")
