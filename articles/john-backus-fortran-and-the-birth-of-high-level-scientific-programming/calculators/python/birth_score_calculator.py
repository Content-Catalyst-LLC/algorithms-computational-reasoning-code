from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Backus/FORTRAN high-level scientific programming.")
for name in [
    "high-level-language", "scientific-expression", "compiler-optimization", "numerical-relevance",
    "portability", "performance-credibility", "language-history", "formal-specification",
    "maintainability", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.high_level_language +
    args.scientific_expression +
    args.compiler_optimization +
    args.numerical_relevance +
    args.portability +
    args.performance_credibility +
    args.language_history +
    args.formal_specification +
    args.maintainability +
    args.governance_caution
) / 10.0
print(f"birth_score={score:.6f}")
