from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify rough algorithm-history layer from dimension scores.")
parser.add_argument("--mechanization", type=float, required=True)
parser.add_argument("--formalization", type=float, required=True)
parser.add_argument("--programmability", type=float, required=True)
parser.add_argument("--governance", type=float, required=True)
args = parser.parse_args()

if args.governance >= 0.90:
    layer = "ai_platforms_and_governance"
elif args.programmability >= 0.90 and args.mechanization >= 0.90:
    layer = "electronic_or_programmable_computation"
elif args.formalization >= 0.90 and args.programmability >= 0.80:
    layer = "logic_computability_formal_algorithm"
elif args.mechanization >= 0.75:
    layer = "mechanical_or_instrumental_computation"
elif args.formalization >= 0.75:
    layer = "symbolic_or_demonstrated_procedure"
else:
    layer = "worked_or_practical_procedure"
print(f"timeline_layer={layer}")
