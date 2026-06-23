from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Demonstrate assignment substitution for weakest preconditions.")
parser.add_argument("--variable", type=str, required=True)
parser.add_argument("--expression", type=str, required=True)
parser.add_argument("--postcondition", type=str, required=True)
args = parser.parse_args()

precondition = args.postcondition.replace(args.variable, f"({args.expression})")
print(f"assignment={args.variable} := {args.expression}")
print(f"postcondition={args.postcondition}")
print(f"substitution_precondition={precondition}")
print("note=syntactic teaching helper only")
