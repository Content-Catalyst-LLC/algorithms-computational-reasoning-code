from __future__ import annotations

import argparse

def parse_vector(text: str) -> list[float]:
    return [float(part.strip()) for part in text.split(",") if part.strip()]

parser = argparse.ArgumentParser(description="Compute weighted portfolio return.")
parser.add_argument("--weights", type=str, required=True)
parser.add_argument("--returns", type=str, required=True)
args = parser.parse_args()

weights = parse_vector(args.weights)
returns = parse_vector(args.returns)
if len(weights) != len(returns):
    raise SystemExit("weights and returns must have same length")
portfolio_return = sum(w * r for w, r in zip(weights, returns))
print(f"portfolio_return={portfolio_return:.6f}")
