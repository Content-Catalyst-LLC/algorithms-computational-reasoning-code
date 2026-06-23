from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify a concept on the path from unknown to variable.")
parser.add_argument("--named", choices=["true", "false"], required=True)
parser.add_argument("--symbolic", choices=["true", "false"], required=True)
parser.add_argument("--ranges-over-values", choices=["true", "false"], required=True)
parser.add_argument("--shapes-family", choices=["true", "false"], required=True)
args = parser.parse_args()

if args.shapes_family == "true":
    stage = "parameter_like"
elif args.ranges_over_values == "true":
    stage = "variable_like"
elif args.symbolic == "true":
    stage = "symbolic_unknown"
elif args.named == "true":
    stage = "named_unknown"
else:
    stage = "sought_unknown"
print(f"variable_transition_stage={stage}")
