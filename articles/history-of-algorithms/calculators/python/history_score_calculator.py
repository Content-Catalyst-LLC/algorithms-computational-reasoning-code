from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for algorithm history.")
parser.add_argument("--procedural-explicitness", type=float, required=True)
parser.add_argument("--representation", type=float, required=True)
parser.add_argument("--proof-correctness", type=float, required=True)
parser.add_argument("--portability", type=float, required=True)
parser.add_argument("--mechanization", type=float, required=True)
parser.add_argument("--formalization", type=float, required=True)
parser.add_argument("--programmability", type=float, required=True)
parser.add_argument("--institutional-adoption", type=float, required=True)
parser.add_argument("--governance-relevance", type=float, required=True)
parser.add_argument("--modern-resonance", type=float, required=True)
args = parser.parse_args()

score = (
    args.procedural_explicitness +
    args.representation +
    args.proof_correctness +
    args.portability +
    args.mechanization +
    args.formalization +
    args.programmability +
    args.institutional_adoption +
    args.governance_relevance +
    args.modern_resonance
) / 10.0
print(f"history_score={score:.6f}")
