from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for a procedural legacy theme.")
parser.add_argument("--procedure", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--application", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (args.procedure + args.representation + args.transmission + args.application + args.modern_resonance) / 5.0
print(f"procedural_legacy_score={score:.6f}")
