from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score whether a test design is a careful behavioral framing.")
for name in ["controlled-setting", "human-judges", "clear-task", "failure-analysis", "scope-limits"]:
    parser.add_argument(f"--has-{name}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_controlled_setting == "true",
    args.has_human_judges == "true",
    args.has_clear_task == "true",
    args.has_failure_analysis == "true",
    args.has_scope_limits == "true",
]
score = sum(values) / len(values)
print(f"behavioral_framing_score={score:.6f}")
