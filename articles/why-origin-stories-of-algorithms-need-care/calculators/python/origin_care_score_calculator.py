from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for algorithm origin-story care.")
parser.add_argument("--evidence-grounding", type=float, required=True)
parser.add_argument("--scope-clarity", type=float, required=True)
parser.add_argument("--anachronism-control", type=float, required=True)
parser.add_argument("--network-awareness", type=float, required=True)
parser.add_argument("--etymology-caution", type=float, required=True)
parser.add_argument("--transmission-depth", type=float, required=True)
parser.add_argument("--credit-distribution", type=float, required=True)
parser.add_argument("--public-usefulness", type=float, required=True)
parser.add_argument("--historical-significance", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.evidence_grounding +
    args.scope_clarity +
    args.anachronism_control +
    args.network_awareness +
    args.etymology_caution +
    args.transmission_depth +
    args.credit_distribution +
    args.public_usefulness +
    args.historical_significance +
    args.modern_resonance
) / 10.0
print(f"origin_care_score={score:.6f}")
