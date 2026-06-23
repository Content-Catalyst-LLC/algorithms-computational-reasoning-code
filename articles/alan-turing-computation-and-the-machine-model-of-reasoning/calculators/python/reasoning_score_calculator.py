from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Turing machine reasoning.")
for name in [
    "formalization", "machine-abstraction", "symbolic-representation", "universality",
    "decidability", "limit-awareness", "reasoning-relevance", "ai-relevance",
    "governance-caution", "modern-resonance"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.formalization +
    args.machine_abstraction +
    args.symbolic_representation +
    args.universality +
    args.decidability +
    args.limit_awareness +
    args.reasoning_relevance +
    args.ai_relevance +
    args.governance_caution +
    args.modern_resonance
) / 10.0
print(f"reasoning_score={score:.6f}")
