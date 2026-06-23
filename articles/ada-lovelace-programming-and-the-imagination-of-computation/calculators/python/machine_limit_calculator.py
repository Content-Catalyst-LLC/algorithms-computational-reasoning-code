from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about independent machine agency.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()

claim = args.claim.lower()
risky_terms = [
    "originates on its own",
    "independently understands",
    "needs no human",
    "fully autonomous truth",
    "creates without prior knowledge",
    "outside instruction",
]
hits = [term for term in risky_terms if term in claim]
print(f"machine_agency_overclaim={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
