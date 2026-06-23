from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Check whether debits and credits balance.")
parser.add_argument("--debits", type=str, required=True, help="Comma-separated debit amounts.")
parser.add_argument("--credits", type=str, required=True, help="Comma-separated credit amounts.")
parser.add_argument("--tolerance", type=float, default=1e-9)
args = parser.parse_args()

debits = [float(x.strip()) for x in args.debits.split(",") if x.strip()]
credits = [float(x.strip()) for x in args.credits.split(",") if x.strip()]
debit_total = sum(debits)
credit_total = sum(credits)
difference = debit_total - credit_total
print(f"debit_total={debit_total:.6f}")
print(f"credit_total={credit_total:.6f}")
print(f"difference={difference:.6f}")
print(f"balanced={str(abs(difference) <= args.tolerance).lower()}")
