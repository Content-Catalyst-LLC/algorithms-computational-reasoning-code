from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate conceptual cycle time from comma-separated stage durations.")
parser.add_argument("--stages", type=str, required=True, help="Comma-separated durations, e.g. 2,3.5,4")
args = parser.parse_args()

stages = [float(x.strip()) for x in args.stages.split(",") if x.strip()]
if any(stage < 0 for stage in stages):
    raise SystemExit("stages must be nonnegative")
print(f"stage_count={len(stages)}")
print(f"cycle_time={sum(stages):.6f}")
