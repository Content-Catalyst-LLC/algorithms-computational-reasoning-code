from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate simple platform visibility amplification from engagement feedback.")
parser.add_argument("--initial-visibility", type=float, required=True)
parser.add_argument("--engagement-rate", type=float, required=True)
parser.add_argument("--ranking-gain", type=float, required=True)
parser.add_argument("--steps", type=int, default=5)
args = parser.parse_args()

visibility = args.initial_visibility
trace = []
for t in range(args.steps):
    engagement = visibility * args.engagement_rate
    visibility = visibility + args.ranking_gain * engagement
    trace.append({"t": t + 1, "visibility": round(visibility, 6), "engagement": round(engagement, 6)})

print("final_visibility=" + str(round(visibility, 6)))
print("trace=" + str(trace))
print("note=teaching_model_only_not_a_platform_model")
