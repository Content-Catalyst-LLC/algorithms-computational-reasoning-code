from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score technical-presentation clarity from notation, layout, consistency, and reproducibility.")
parser.add_argument("--notation", type=float, required=True)
parser.add_argument("--layout", type=float, required=True)
parser.add_argument("--consistency", type=float, required=True)
parser.add_argument("--reproducibility", type=float, required=True)
args = parser.parse_args()

score = (args.notation + args.layout + args.consistency + args.reproducibility) / 4.0
print(f"technical_presentation_clarity={score:.6f}")
