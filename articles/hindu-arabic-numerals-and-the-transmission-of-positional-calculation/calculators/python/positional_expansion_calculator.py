from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Expand a base-10 integer into place-value terms.")
parser.add_argument("--number", type=int, required=True)
args = parser.parse_args()

if args.number < 0:
    raise SystemExit("number must be nonnegative")
digits = list(map(int, str(args.number)))
terms = []
for idx, digit in enumerate(reversed(digits)):
    if digit != 0:
        terms.append(f"{digit}*10^{idx}")
if not terms:
    terms = ["0"]
print(" + ".join(reversed(terms)))
