from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Simple SIR population accounting.")
parser.add_argument("--susceptible", type=float, required=True)
parser.add_argument("--infected", type=float, required=True)
parser.add_argument("--recovered", type=float, required=True)
args = parser.parse_args()

population = args.susceptible + args.infected + args.recovered
if population <= 0:
    raise SystemExit("population must be positive")
infected_share = args.infected / population
print(f"population={population:.6f}")
print(f"infected_share={infected_share:.6f}")
