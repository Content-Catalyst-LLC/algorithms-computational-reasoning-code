from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag modern computing projected backward.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = ["first computer scientist", "wrote code", "programmed", "database", "robot", "artificial intelligence", "modern algorithm exactly"]
hits = [term for term in risky_terms if term in claim]
print(f"anachronism_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
