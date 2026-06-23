from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score algorithm-like procedural features.")
for name in ["input", "steps", "conditions", "iteration", "termination", "verification"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_input == "true",
    args.has_steps == "true",
    args.has_conditions == "true",
    args.has_iteration == "true",
    args.has_termination == "true",
    args.has_verification == "true",
]
score = sum(values) / len(values)
print(f"procedure_feature_score={score:.6f}")
