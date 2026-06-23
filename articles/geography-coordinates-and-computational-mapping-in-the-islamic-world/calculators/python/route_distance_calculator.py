from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Sum comma-separated route segment distances.")
parser.add_argument("--segments", type=str, required=True, help="Comma-separated distances, e.g. 12,20,7.5")
args = parser.parse_args()

segments = [float(x.strip()) for x in args.segments.split(",") if x.strip()]
if any(s < 0 for s in segments):
    raise SystemExit("segments must be nonnegative")
print(f"segments={len(segments)}")
print(f"total_distance={sum(segments):.6f}")
