from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute a toy hiring score from job-related evidence.")
parser.add_argument("--job-relevance", type=float, required=True)
parser.add_argument("--evidence-quality", type=float, required=True)
parser.add_argument("--experience-fit", type=float, required=True)
parser.add_argument("--accessibility-support", type=float, default=0.0)
parser.add_argument("--weights", type=str, default="0.40,0.30,0.20,0.10")
args = parser.parse_args()

weights = [float(part.strip()) for part in args.weights.split(",")]
if len(weights) != 4:
    raise SystemExit("weights must contain four comma-separated values")
total = sum(weights)
if total <= 0:
    raise SystemExit("weights must sum to a positive value")
w = [item / total for item in weights]
score = (
    w[0] * args.job_relevance +
    w[1] * args.evidence_quality +
    w[2] * args.experience_fit +
    w[3] * args.accessibility_support
)
print(f"hiring_score={score:.6f}")
