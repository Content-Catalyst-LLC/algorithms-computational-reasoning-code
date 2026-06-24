from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Average neural-logic interpretive dimensions.")
for name in [
    "logical-clarity", "neural-abstraction", "computational-relevance",
    "cybernetic-connection", "ai-lineage", "biological-caution",
    "historical-influence", "interpretability", "formal-tractability",
    "responsible-use-relevance"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()
score = (
    args.logical_clarity + args.neural_abstraction + args.computational_relevance +
    args.cybernetic_connection + args.ai_lineage + args.biological_caution +
    args.historical_influence + args.interpretability + args.formal_tractability +
    args.responsible_use_relevance
) / 10.0
print(f"neural_logic_score={score:.6f}")
