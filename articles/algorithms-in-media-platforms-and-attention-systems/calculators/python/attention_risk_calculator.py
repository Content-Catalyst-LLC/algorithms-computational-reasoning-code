from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute attention risk.")
parser.add_argument("--engagement-pressure", type=float, required=True)
parser.add_argument("--creator-impact", type=float, required=True)
parser.add_argument("--public-knowledge-impact", type=float, required=True)
parser.add_argument("--user-control", type=float, required=True)
parser.add_argument("--contestability", type=float, required=True)
args = parser.parse_args()

score = (
    args.engagement_pressure +
    args.creator_impact +
    args.public_knowledge_impact +
    (1.0 - args.user_control) +
    (1.0 - args.contestability)
) / 5.0
print(f"attention_risk_score={score:.6f}")
