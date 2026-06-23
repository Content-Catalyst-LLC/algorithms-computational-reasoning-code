from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Flag whether a toy ciphertext is likely too short for stable frequency estimates.")
parser.add_argument("--text", type=str, required=True)
parser.add_argument("--minimum", type=int, default=100)
args = parser.parse_args()

n = sum(1 for ch in args.text if ch.isalpha())
print(f"alphabetic_symbols={n}")
print(f"minimum_recommended={args.minimum}")
print(f"sample_size_warning={str(n < args.minimum).lower()}")
