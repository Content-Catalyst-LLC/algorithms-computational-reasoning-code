from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute grid balance margin.")
parser.add_argument("--supply", type=float, required=True)
parser.add_argument("--storage", type=float, default=0.0)
parser.add_argument("--imports", type=float, default=0.0)
parser.add_argument("--demand", type=float, required=True)
parser.add_argument("--exports", type=float, default=0.0)
parser.add_argument("--losses", type=float, default=0.0)
args = parser.parse_args()

margin = args.supply + args.storage + args.imports - args.demand - args.exports - args.losses
print(f"grid_balance_margin={margin:.6f}")
