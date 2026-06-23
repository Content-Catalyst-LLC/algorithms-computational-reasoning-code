from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for algorism, algebra, and reception.")
parser.add_argument("--procedural-portability", type=float, required=True)
parser.add_argument("--notation-change", type=float, required=True)
parser.add_argument("--translation-pathway", type=float, required=True)
parser.add_argument("--teaching-value", type=float, required=True)
parser.add_argument("--practical-utility", type=float, required=True)
parser.add_argument("--institutional-adoption", type=float, required=True)
parser.add_argument("--trust-verification", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--ethical-caution", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.procedural_portability +
    args.notation_change +
    args.translation_pathway +
    args.teaching_value +
    args.practical_utility +
    args.institutional_adoption +
    args.trust_verification +
    args.historical_significance +
    args.ethical_caution +
    args.modern_resonance
) / 10.0
print(f"reception_score={score:.6f}")
