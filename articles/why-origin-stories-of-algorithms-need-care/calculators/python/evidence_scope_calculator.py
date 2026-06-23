from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Score whether an origin claim includes evidence and scope.")
for name in ["evidence", "date_or_period", "scope", "uncertainty", "transmission"]:
    parser.add_argument(f"--has-{name.replace('_', '-')}", choices=["true", "false"], required=True)
args = parser.parse_args()

values = [
    args.has_evidence == "true",
    args.has_date_or_period == "true",
    args.has_scope == "true",
    args.has_uncertainty == "true",
    args.has_transmission == "true",
]
score = sum(values) / len(values)
print(f"evidence_scope_score={score:.6f}")
