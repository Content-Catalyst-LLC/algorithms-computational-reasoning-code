from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Dijkstra structured programming.")
for name in [
    "structured-control", "correctness", "invariants", "proof-relevance", "formal-methods",
    "readability", "maintainability", "algorithmic-relevance", "system-design", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.structured_control +
    args.correctness +
    args.invariants +
    args.proof_relevance +
    args.formal_methods +
    args.readability +
    args.maintainability +
    args.algorithmic_relevance +
    args.system_design +
    args.governance_caution
) / 10.0
print(f"discipline_score={score:.6f}")
