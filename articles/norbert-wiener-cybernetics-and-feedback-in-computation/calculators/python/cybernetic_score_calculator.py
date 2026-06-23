from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Average interpretive dimensions for Wiener cybernetic feedback.")
for name in [
    "feedback-centrality", "control-relevance", "communication-relevance", "prediction-relevance",
    "stability-relevance", "amplification-risk", "automation-ethics",
    "ai-relevance", "institutional-relevance", "governance-caution"
]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()

score = (
    args.feedback_centrality +
    args.control_relevance +
    args.communication_relevance +
    args.prediction_relevance +
    args.stability_relevance +
    args.amplification_risk +
    args.automation_ethics +
    args.ai_relevance +
    args.institutional_relevance +
    args.governance_caution
) / 10.0
print(f"cybernetic_score={score:.6f}")
