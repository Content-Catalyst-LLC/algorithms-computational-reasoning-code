from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Church formal computation.")
for name in [
    "formalization", "functional-abstraction", "symbolic-transformation", "substitution",
    "reduction", "computability", "undecidability", "type-influence",
    "programming-relevance", "ai-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.formalization +
    args.functional_abstraction +
    args.symbolic_transformation +
    args.substitution +
    args.reduction +
    args.computability +
    args.undecidability +
    args.type_influence +
    args.programming_relevance +
    args.ai_caution
) / 10.0
print(f"formal_score={score:.6f}")
