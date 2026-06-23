from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for sequenced mechanical action.")
parser.add_argument("--sequence-structure", type=float, required=True)
parser.add_argument("--timing-control", type=float, required=True)
parser.add_argument("--mechanical-embodiment", type=float, required=True)
parser.add_argument("--conditional-action", type=float, required=True)
parser.add_argument("--repeatability", type=float, required=True)
parser.add_argument("--documentation-quality", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--ethical-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.sequence_structure +
    args.timing_control +
    args.mechanical_embodiment +
    args.conditional_action +
    args.repeatability +
    args.documentation_quality +
    args.historical_significance +
    args.ethical_caution +
    args.modern_resonance
) / 9.0
print(f"sequenced_action_score={score:.6f}")
