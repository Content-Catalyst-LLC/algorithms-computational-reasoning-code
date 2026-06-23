from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Convert an amount by an exchange rate.")
parser.add_argument("--amount", type=float, required=True)
parser.add_argument("--rate", type=float, required=True)
args = parser.parse_args()

converted = args.amount * args.rate
print(f"converted_amount={converted:.6f}")
