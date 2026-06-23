from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Apply a toy substitution map such as a=b,b=c.")
parser.add_argument("--text", type=str, required=True)
parser.add_argument("--mapping", type=str, required=True, help="Comma-separated map, e.g. a=b,b=c")
args = parser.parse_args()

mapping = {}
for item in args.mapping.split(","):
    if not item.strip():
        continue
    left, right = item.split("=")
    mapping[left.strip().lower()] = right.strip().lower()

out = []
for ch in args.text:
    low = ch.lower()
    if low in mapping:
        repl = mapping[low]
        out.append(repl.upper() if ch.isupper() else repl)
    else:
        out.append(ch)
print("".join(out))
