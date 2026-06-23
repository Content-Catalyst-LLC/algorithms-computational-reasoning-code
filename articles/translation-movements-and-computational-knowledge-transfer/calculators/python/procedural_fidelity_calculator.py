from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average preservation of procedure components.")
parser.add_argument("--terms", type=float, required=True)
parser.add_argument("--steps", type=float, required=True)
parser.add_argument("--examples", type=float, required=True)
parser.add_argument("--diagrams", type=float, required=True)
parser.add_argument("--tables", type=float, required=True)
parser.add_argument("--context", type=float, required=True)
args = parser.parse_args()

score = (args.terms + args.steps + args.examples + args.diagrams + args.tables + args.context) / 6.0
print(f"procedural_fidelity={score:.6f}")
