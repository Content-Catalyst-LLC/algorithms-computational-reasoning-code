from __future__ import annotations
import argparse
parser = argparse.ArgumentParser(description="Estimate Goodhart pressure.")
parser.add_argument("--metric-stakes", type=float, required=True)
parser.add_argument("--optimization-pressure", type=float, required=True)
parser.add_argument("--proxy-gap", type=float, required=True)
parser.add_argument("--monitoring-strength", type=float, required=True)
args = parser.parse_args()
raw = (args.metric_stakes + args.optimization_pressure + args.proxy_gap) / 3.0
mitigated = raw * (1.0 - max(0.0, min(1.0, args.monitoring_strength)) * 0.35)
print(f"goodhart_pressure={mitigated:.6f}")
