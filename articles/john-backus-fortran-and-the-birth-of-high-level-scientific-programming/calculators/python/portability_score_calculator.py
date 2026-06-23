from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate portability as supported compilers divided by target systems.")
parser.add_argument("--supported-compilers", type=float, required=True)
parser.add_argument("--target-systems", type=float, required=True)
args = parser.parse_args()

if args.target_systems <= 0:
    raise SystemExit("target systems must be positive")
score = max(0.0, min(1.0, args.supported_compilers / args.target_systems))
print(f"portability_score={score:.6f}")
