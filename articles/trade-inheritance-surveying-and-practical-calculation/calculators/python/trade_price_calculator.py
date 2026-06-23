from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute trade price as quantity times unit price.")
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--unit-price", type=float, required=True)
args = parser.parse_args()

total = args.quantity * args.unit_price
print(f"total_price={total:.6f}")
