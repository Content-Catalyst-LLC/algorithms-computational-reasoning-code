from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Compute decimal value from comma-separated digits, e.g. 1,2,3 -> 123.")
parser.add_argument("--digits", type=str, required=True)
args = parser.parse_args()

digits = [int(part.strip()) for part in args.digits.split(",") if part.strip()]
if any(d < 0 or d > 9 for d in digits):
    raise SystemExit("digits must be between 0 and 9")
value = 0
for digit in digits:
    value = value * 10 + digit
print(f"place_value={value}")
