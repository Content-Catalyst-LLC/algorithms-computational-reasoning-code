from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for mechanical procedure.")
parser.add_argument("--mechanical-structure", type=float, required=True)
parser.add_argument("--procedural-sequence", type=float, required=True)
parser.add_argument("--conditional-control", type=float, required=True)
parser.add_argument("--hidden-state", type=float, required=True)
parser.add_argument("--feedback-potential", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--ethical-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.mechanical_structure +
    args.procedural_sequence +
    args.conditional_control +
    args.hidden_state +
    args.feedback_potential +
    args.historical_significance +
    args.ethical_caution +
    args.modern_resonance
) / 8.0
print(f"mechanical_score={score:.6f}")
