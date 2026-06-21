from __future__ import annotations

from pathlib import Path
import argparse
import csv
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ARTICLE_ROOT / "outputs" / "tables" / "agent_based_calculator_output.csv"


def run_threshold_adoption(agents: int, threshold: float, steps: int, seed: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    adopted = [rng.random() < 0.08 for _ in range(agents)]
    rows = []
    for step in range(steps + 1):
        share = sum(adopted) / agents
        rows.append({"step": step, "agents": agents, "threshold": threshold, "adoption_share": round(share, 6), "seed": seed})
        if step == steps:
            break
        next_adopted = adopted[:]
        for i, value in enumerate(adopted):
            if value:
                continue
            left = adopted[(i - 1) % agents]
            right = adopted[(i + 1) % agents]
            local_share = (int(left) + int(right)) / 2
            if local_share >= threshold or rng.random() < 0.015:
                next_adopted[i] = True
        adopted = next_adopted
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Small threshold-adoption calculator for agent-based emergence.")
    parser.add_argument("--agents", type=int, default=100)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--steps", type=int, default=30)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    rows = run_threshold_adoption(args.agents, args.threshold, args.steps, args.seed)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)


if __name__ == "__main__":
    main()
