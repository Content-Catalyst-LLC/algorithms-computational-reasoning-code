from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Toy event trigger calculator for sequenced mechanical action.")
parser.add_argument("--value", type=float, required=True)
parser.add_argument("--trigger", type=float, required=True)
args = parser.parse_args()

triggered = args.value >= args.trigger
print(f"event_triggered={str(triggered).lower()}")
