# simulation_calculator.py
# Self-contained calculator for simple simulation reasoning checks.

from __future__ import annotations

from pathlib import Path
import csv
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def run_simulation(initial=100.0, growth=0.08, loss=0.03, intervention=0.04, steps=30, stochastic=False, seed=42):
    rng = random.Random(seed)
    stock = initial
    rows = []
    for t in range(steps + 1):
        rows.append({"time_step": t, "stock": round(stock, 6)})
        shock = 0.12 * stock if stochastic and rng.random() < 0.18 else 0.0
        stock = max(0.0, stock + growth * stock - loss * stock - intervention * stock - shock)
    return rows


def main():
    rows = run_simulation()
    path = OUT / "simulation_calculator_output.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["time_step", "stock"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"final_stock={rows[-1]['stock']}")
    print(path)


if __name__ == "__main__":
    main()
