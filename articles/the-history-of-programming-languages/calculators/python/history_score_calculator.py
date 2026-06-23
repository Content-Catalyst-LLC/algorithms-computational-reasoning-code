from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for programming-language history.")
for name in [
    "abstraction", "performance-orientation", "readability", "formal-specification",
    "ecosystem-depth", "domain-fit", "safety-orientation", "institutional-adoption",
    "historical-influence", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.abstraction +
    args.performance_orientation +
    args.readability +
    args.formal_specification +
    args.ecosystem_depth +
    args.domain_fit +
    args.safety_orientation +
    args.institutional_adoption +
    args.historical_influence +
    args.governance_caution
) / 10.0
print(f"history_score={score:.6f}")
