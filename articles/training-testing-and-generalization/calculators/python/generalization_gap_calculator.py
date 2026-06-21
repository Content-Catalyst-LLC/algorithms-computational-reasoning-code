from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Calculate a generalization gap between training and held-out metrics.")
parser.add_argument("--train-metric", type=float, required=True)
parser.add_argument("--test-metric", type=float, required=True)
parser.add_argument("--higher-is-better", action="store_true")
args = parser.parse_args()
gap = args.train_metric - args.test_metric if args.higher_is_better else args.test_metric - args.train_metric
print(f"train_metric={args.train_metric:.6f}")
print(f"test_metric={args.test_metric:.6f}")
print(f"generalization_gap={gap:.6f}")
