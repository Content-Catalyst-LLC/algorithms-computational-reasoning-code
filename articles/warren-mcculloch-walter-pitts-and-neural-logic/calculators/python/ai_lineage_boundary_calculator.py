from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Flag overclaims about McCulloch-Pitts and modern AI.")
parser.add_argument("--claim", required=True)
args = parser.parse_args()
claim = args.claim.lower()
risky_terms = [
    "invented deep learning",
    "same as modern deep learning",
    "fully explains the brain",
    "proved machines understand",
    "real neurons are boolean gates",
    "brain is just a computer",
]
hits = [term for term in risky_terms if term in claim]
print(f"lineage_overclaim_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
