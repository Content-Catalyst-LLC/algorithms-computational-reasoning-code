from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for a rule-governed algebraic theme.")
parser.add_argument("--classification", type=float, required=True)
parser.add_argument("--transformation", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--demonstration", type=float, required=True)
parser.add_argument("--practical-use", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.classification +
    args.transformation +
    args.representation +
    args.demonstration +
    args.practical_use +
    args.transmission +
    args.modern_resonance
) / 7.0
print(f"algebraic_procedure_score={score:.6f}")
