from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for practical calculation.")
parser.add_argument("--procedure", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--institutional-importance", type=float, required=True)
parser.add_argument("--verification", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.procedure +
    args.representation +
    args.institutional_importance +
    args.verification +
    args.transmission +
    args.modern_resonance
) / 6.0
print(f"practical_score={score:.6f}")
