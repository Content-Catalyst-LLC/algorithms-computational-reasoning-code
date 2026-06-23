from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Evaluate a base-10 number from comma-separated digits.")
parser.add_argument("--digits", type=str, required=True, help="Comma-separated digits, e.g. 1,2,3,0")
args = parser.parse_args()

digits = [int(x.strip()) for x in args.digits.split(",") if x.strip()]
if any(d < 0 or d > 9 for d in digits):
    raise SystemExit("All digits must be between 0 and 9.")

value = 0
for digit in digits:
    value = value * 10 + digit

print(f"place_value_result={value}")
