from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score completeness of a procedural knowledge object.")
for name in ["terms", "steps", "examples", "diagrams", "tables", "context"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_terms == "true",
    args.has_steps == "true",
    args.has_examples == "true",
    args.has_diagrams == "true",
    args.has_tables == "true",
    args.has_context == "true",
]
score = sum(values) / len(values)
print(f"knowledge_object_completeness={score:.6f}")
