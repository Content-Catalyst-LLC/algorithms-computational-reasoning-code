from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Estimate type/safety orientation.")
parser.add_argument("--static-checking", type=float, required=True)
parser.add_argument("--runtime-checking", type=float, required=True)
parser.add_argument("--memory-safety", type=float, required=True)
parser.add_argument("--concurrency-safety", type=float, required=True)
parser.add_argument("--tooling", type=float, required=True)
args = parser.parse_args()

score = (
    args.static_checking +
    args.runtime_checking +
    args.memory_safety +
    args.concurrency_safety +
    args.tooling
) / 5.0
print(f"type_safety_score={score:.6f}")
