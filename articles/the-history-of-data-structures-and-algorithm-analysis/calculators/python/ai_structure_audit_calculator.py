from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag AI infrastructure claims that ignore data-structure governance.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "data structures do not matter",
    "no provenance needed",
    "no index audit needed",
    "embeddings are neutral",
    "queues and logs do not matter",
    "no monitoring needed",
    "no storage governance needed",
]
hits = [term for term in risky_terms if term in claim]
print(f"ai_structure_audit_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
