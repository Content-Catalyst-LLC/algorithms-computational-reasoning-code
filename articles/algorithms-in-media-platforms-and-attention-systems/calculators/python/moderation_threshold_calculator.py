from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Classify moderation action from harm score and thresholds.")
parser.add_argument("--harm-score", type=float, required=True)
parser.add_argument("--review-threshold", type=float, default=0.50)
parser.add_argument("--remove-threshold", type=float, default=0.85)
args = parser.parse_args()

if args.harm_score >= args.remove_threshold:
    action = "remove"
elif args.harm_score >= args.review_threshold:
    action = "review"
else:
    action = "allow"

print(f"moderation_action={action}")
