from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag modern-code projection into older procedure.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = ["wrote code", "database", "software", "programming language", "artificial intelligence", "modern algorithm exactly", "computer scientist"]
hits = [term for term in risky_terms if term in claim]
print(f"modern_projection_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
