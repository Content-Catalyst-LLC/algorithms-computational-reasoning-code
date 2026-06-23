from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Hopper compiler humanization.")
for name in [
    "compiler-centrality", "human-readability", "portability", "documentation",
    "standards", "debugging", "business-relevance", "institutional-scale",
    "abstraction", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.compiler_centrality +
    args.human_readability +
    args.portability +
    args.documentation +
    args.standards +
    args.debugging +
    args.business_relevance +
    args.institutional_scale +
    args.abstraction +
    args.governance_caution
) / 10.0
print(f"humanization_score={score:.6f}")
