from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate explanation quality for algorithmic code.")
parser.add_argument("--purpose", type=float, required=True)
parser.add_argument("--assumptions", type=float, required=True)
parser.add_argument("--complexity", type=float, required=True)
parser.add_argument("--examples", type=float, required=True)
parser.add_argument("--tests", type=float, required=True)
args = parser.parse_args()

score = (args.purpose + args.assumptions + args.complexity + args.examples + args.tests) / 5.0
print(f"documentation_score={score:.6f}")
