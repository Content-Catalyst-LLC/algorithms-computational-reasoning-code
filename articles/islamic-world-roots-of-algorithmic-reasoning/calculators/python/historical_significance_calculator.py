from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for a historical algorithmic-reasoning theme.")
parser.add_argument("--procedural", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--practical", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--modern", type=float, required=True)
args = parser.parse_args()

score = (args.procedural + args.transmission + args.practical + args.representation + args.modern) / 5.0
print(f"historical_significance_score={score:.6f}")
