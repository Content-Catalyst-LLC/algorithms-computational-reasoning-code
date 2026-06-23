from __future__ import annotations

import argparse
import string

ALPHABET = string.ascii_lowercase

parser = argparse.ArgumentParser(description="Toy Caesar cipher demo for classical-cipher education.")
parser.add_argument("--text", type=str, required=True)
parser.add_argument("--shift", type=int, required=True)
parser.add_argument("--mode", choices=["encrypt", "decrypt"], default="encrypt")
args = parser.parse_args()

shift = args.shift % 26
if args.mode == "decrypt":
    shift = -shift

out = []
for ch in args.text:
    lower = ch.lower()
    if lower in ALPHABET:
        idx = (ALPHABET.index(lower) + shift) % 26
        repl = ALPHABET[idx]
        out.append(repl.upper() if ch.isupper() else repl)
    else:
        out.append(ch)

print("".join(out))
