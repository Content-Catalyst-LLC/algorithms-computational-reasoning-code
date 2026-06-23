from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for a verbal procedure theme.")
parser.add_argument("--procedural-clarity", type=float, required=True)
parser.add_argument("--representation-dependence", type=float, required=True)
parser.add_argument("--pedagogical-value", type=float, required=True)
parser.add_argument("--transmission-importance", type=float, required=True)
parser.add_argument("--practical-use", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.procedural_clarity +
    args.representation_dependence +
    args.pedagogical_value +
    args.transmission_importance +
    args.practical_use +
    args.modern_resonance
) / 6.0
print(f"verbal_procedure_score={score:.6f}")
