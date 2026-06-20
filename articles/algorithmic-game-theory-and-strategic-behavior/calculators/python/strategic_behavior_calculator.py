#!/usr/bin/env python3
"""Small calculator for strategic manipulation incentives."""
from __future__ import annotations
from pathlib import Path
import csv
OUTPUT = Path(__file__).resolve().parents[1] / "outputs" / "strategic_behavior_calculator.csv"
def net_gain(reward: float, manipulation_cost: float, penalty: float, detection_probability: float) -> float:
    return reward - manipulation_cost - detection_probability * penalty
def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for detection_probability in [0.0, 0.25, 0.50, 0.75, 1.0]:
        for penalty in [0.0, 3.0, 6.0, 9.0, 12.0]:
            gain = net_gain(10.0, 3.0, penalty, detection_probability)
            rows.append({"reward": 10.0, "manipulation_cost": 3.0, "penalty": penalty, "detection_probability": detection_probability, "net_gain": round(gain, 4), "manipulation_attractive": gain > 0})
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)
if __name__ == "__main__":
    main()
