from __future__ import annotations
import argparse

parser = argparse.ArgumentParser(description="Estimate computational literacy coverage.")
for name in ["data", "algorithms", "statistics", "systems", "ai-limits", "governance"]:
    parser.add_argument(f"--{name}", type=float, required=True)
args = parser.parse_args()
score = (args.data + args.algorithms + args.statistics + args.systems + args.ai_limits + args.governance) / 6.0
print(f"computational_literacy_score={score:.6f}")
