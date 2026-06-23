from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute synthetic day offset between two calendar markers.")
parser.add_argument("--start-day", type=int, required=True)
parser.add_argument("--end-day", type=int, required=True)
args = parser.parse_args()

offset = args.end_day - args.start_day
print(f"day_offset={offset}")
