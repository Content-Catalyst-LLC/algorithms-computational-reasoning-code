from __future__ import annotations

import argparse
import math

parser = argparse.ArgumentParser(description="Compare maximum entropy with observed entropy.")
parser.add_argument("--alphabet-size", type=int, required=True)
parser.add_argument("--observed-entropy", type=float, required=True)
args = parser.parse_args()

if args.alphabet_size <= 1:
    raise SystemExit("alphabet size must be > 1")
max_entropy = math.log2(args.alphabet_size)
redundancy = max_entropy - args.observed_entropy
relative = redundancy / max_entropy
print(f"max_entropy_bits={max_entropy:.9f}")
print(f"redundancy_bits={redundancy:.9f}")
print(f"relative_redundancy={relative:.9f}")
