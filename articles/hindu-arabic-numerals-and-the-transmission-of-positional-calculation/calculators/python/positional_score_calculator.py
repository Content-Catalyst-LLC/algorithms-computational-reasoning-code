from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for a positional calculation theme.")
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--procedure", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--practical-use", type=float, required=True)
parser.add_argument("--pedagogy", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.representation +
    args.procedure +
    args.transmission +
    args.practical_use +
    args.pedagogy +
    args.modern_resonance
) / 6.0
print(f"positional_score={score:.6f}")
