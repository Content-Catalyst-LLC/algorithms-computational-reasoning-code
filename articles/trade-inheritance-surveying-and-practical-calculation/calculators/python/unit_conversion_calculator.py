from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Convert a quantity by a conversion factor.")
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--factor", type=float, required=True)
args = parser.parse_args()

converted = args.quantity * args.factor
print(f"converted_quantity={converted:.6f}")
