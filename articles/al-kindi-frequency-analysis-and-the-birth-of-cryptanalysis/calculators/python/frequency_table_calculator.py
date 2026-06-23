from __future__ import annotations

import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="Count alphabetic symbols and relative frequencies in toy text.")
parser.add_argument("--text", type=str, required=True)
args = parser.parse_args()

symbols = [ch.lower() for ch in args.text if ch.isalpha()]
total = len(symbols)
counts = Counter(symbols)

print("symbol,count,relative_frequency,rank")
for rank, (symbol, count) in enumerate(counts.most_common(), start=1):
    rel = count / total if total else 0.0
    print(f"{symbol},{count},{rel:.6f},{rank}")
