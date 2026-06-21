from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Calculate train/test/validation split counts.")
parser.add_argument("--n", type=int, required=True)
parser.add_argument("--train", type=float, default=0.70)
parser.add_argument("--validation", type=float, default=0.15)
args = parser.parse_args()
if args.n <= 0: raise SystemExit("n must be positive")
if args.train < 0 or args.validation < 0 or args.train + args.validation > 1: raise SystemExit("split proportions must sum to at most 1")
train_n = round(args.n * args.train)
validation_n = round(args.n * args.validation)
test_n = args.n - train_n - validation_n
print(f"n={args.n}")
print(f"train_n={train_n}")
print(f"validation_n={validation_n}")
print(f"test_n={test_n}")
