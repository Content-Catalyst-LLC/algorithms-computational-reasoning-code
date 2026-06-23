from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for al-Khwārizmī and algorithmic method.")
parser.add_argument("--arithmetic-method", type=float, required=True)
parser.add_argument("--algebraic-procedure", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--transformation", type=float, required=True)
parser.add_argument("--proof-relation", type=float, required=True)
parser.add_argument("--transmission", type=float, required=True)
parser.add_argument("--etymology", type=float, required=True)
parser.add_argument("--institutional-adoption", type=float, required=True)
parser.add_argument("--historiographic-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.arithmetic_method +
    args.algebraic_procedure +
    args.representation +
    args.transformation +
    args.proof_relation +
    args.transmission +
    args.etymology +
    args.institutional_adoption +
    args.historiographic_caution +
    args.modern_resonance
) / 10.0
print(f"method_score={score:.6f}")
