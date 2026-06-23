from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Flag AI-output claims that confuse generation with accountable reasoning.")
parser.add_argument("--claim", type=str, required=True)
args = parser.parse_args()
claim = args.claim.lower()
risky_terms = ["ai output is always correct","no human review needed","no sources needed","no tests needed","no audit trail needed","ai decides","fully autonomous with no oversight"]
hits = [term for term in risky_terms if term in claim]
print(f"ai_output_governance_risk={str(bool(hits)).lower()}")
print("matched_terms=" + ",".join(hits))
