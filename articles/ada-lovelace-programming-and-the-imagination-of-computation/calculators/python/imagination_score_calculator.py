from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Lovelace computation imagination.")
parser.add_argument("--programming-structure", type=float, required=True)
parser.add_argument("--symbolic-generality", type=float, required=True)
parser.add_argument("--machine-orientation", type=float, required=True)
parser.add_argument("--mathematical-grounding", type=float, required=True)
parser.add_argument("--imaginative-reach", type=float, required=True)
parser.add_argument("--limit-awareness", type=float, required=True)
parser.add_argument("--collaboration", type=float, required=True)
parser.add_argument("--authorship", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
parser.add_argument("--ai-caution", type=float, required=True)
args = parser.parse_args()

score = (
    args.programming_structure +
    args.symbolic_generality +
    args.machine_orientation +
    args.mathematical_grounding +
    args.imaginative_reach +
    args.limit_awareness +
    args.collaboration +
    args.authorship +
    args.modern_resonance +
    args.ai_caution
) / 10.0
print(f"imagination_score={score:.6f}")
