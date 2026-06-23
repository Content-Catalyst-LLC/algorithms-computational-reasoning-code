from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score governance relevance for an algorithmic system.")
for name in ["audit", "contestability", "harm", "transparency", "human_judgment"]:
    parser.add_argument(f"--has-{name.replace('_', '-')}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_audit == "true",
    args.has_contestability == "true",
    args.has_harm == "true",
    args.has_transparency == "true",
    args.has_human_judgment == "true",
]
score = sum(values) / len(values)
print(f"governance_relevance_score={score:.6f}")
