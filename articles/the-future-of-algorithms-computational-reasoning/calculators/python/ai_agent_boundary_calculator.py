from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Flag weak AI-agent boundaries.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()
claim = args.claim.lower()
risky_terms = [
    "full autonomy no approval",
    "no logs needed",
    "all tools allowed",
    "no rollback",
    "unlimited permissions",
    "no human confirmation",
    "no audit trail",
]
hits = [term for term in risky_terms if term in claim]
print(f"agent_boundary_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
