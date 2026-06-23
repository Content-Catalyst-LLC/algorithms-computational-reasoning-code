from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score whether a domain can be represented for symbolic operation.")
for name in ["representation", "relations", "operations", "patterns", "outputs"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_representation == "true",
    args.has_relations == "true",
    args.has_operations == "true",
    args.has_patterns == "true",
    args.has_outputs == "true",
]
score = sum(values) / len(values)
print(f"symbolic_generality_score={score:.6f}")
