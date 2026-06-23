from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute staffing coverage margin.")
parser.add_argument("--scheduled-hours", type=float, required=True)
parser.add_argument("--demand-hours", type=float, required=True)
args = parser.parse_args()

margin = args.scheduled_hours - args.demand_hours
coverage_ratio = args.scheduled_hours / args.demand_hours if args.demand_hours > 0 else float("inf")
print(f"coverage_margin={margin:.6f}")
print(f"coverage_ratio={coverage_ratio:.6f}")
