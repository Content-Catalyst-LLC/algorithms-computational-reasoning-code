from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for data-structure and algorithm-analysis history.")
for name in [
    "representation-centrality", "operation-clarity", "memory-awareness", "time-analysis",
    "space-analysis", "scale-sensitivity", "abstraction-maturity", "systems-relevance",
    "historical-influence", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.representation_centrality +
    args.operation_clarity +
    args.memory_awareness +
    args.time_analysis +
    args.space_analysis +
    args.scale_sensitivity +
    args.abstraction_maturity +
    args.systems_relevance +
    args.historical_influence +
    args.governance_caution
) / 10.0
print(f"history_score={score:.6f}")
