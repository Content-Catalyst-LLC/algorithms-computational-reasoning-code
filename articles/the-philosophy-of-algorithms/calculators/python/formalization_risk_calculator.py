from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate formalization risk.")
parser.add_argument("--context-loss", type=float, required=True)
parser.add_argument("--label-ambiguity", type=float, required=True)
parser.add_argument("--proxy-risk", type=float, required=True)
parser.add_argument("--decision-severity", type=float, required=True)
args = parser.parse_args()
risk = (args.context_loss + args.label_ambiguity + args.proxy_risk + args.decision_severity) / 4.0
print(f"formalization_risk={risk:.6f}")
