# privacy_preserving_calculator.py
# Educational calculator for privacy-preserving computation examples.

from __future__ import annotations

from pathlib import Path
from random import Random
import csv
import math

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ARTICLE_ROOT / "calculators" / "outputs"


def laplace_noise(scale: float, rng: Random) -> float:
    u = rng.random() - 0.5
    return -scale * math.copysign(math.log(1 - 2 * abs(u)), u)


def dp_count(true_count: int, epsilon: float, sensitivity: float = 1.0, seed: int = 7) -> dict[str, object]:
    rng = Random(seed)
    scale = sensitivity / epsilon
    noise = laplace_noise(scale, rng)
    return {
        "true_count": true_count,
        "epsilon": epsilon,
        "sensitivity": sensitivity,
        "scale": round(scale, 6),
        "noise": round(noise, 6),
        "noisy_count": round(true_count + noise, 6),
    }


def secure_aggregate(values: list[int], masks: list[int]) -> dict[str, object]:
    if len(values) != len(masks):
        raise ValueError("values and masks must have the same length")
    masked = [v + m for v, m in zip(values, masks)]
    return {
        "private_sum": sum(values),
        "mask_sum": sum(masks),
        "masked_sum": sum(masked),
        "masked_values": masked,
    }


def federated_average(local_weights: list[float], example_counts: list[int]) -> float:
    total = sum(example_counts)
    if total <= 0:
        raise ValueError("total examples must be positive")
    return sum(w * n for w, n in zip(local_weights, example_counts)) / total


def main() -> None:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    rows = []

    for eps in [0.25, 0.5, 1.0, 2.0]:
        result = dp_count(248, eps)
        result["calculator"] = "dp_count"
        rows.append(result)

    aggregate = secure_aggregate([18, 24, 15], [7, -3, -4])
    rows.append({"calculator": "secure_aggregate", **aggregate})

    fed = federated_average([0.42, 0.55, 0.49], [100, 240, 160])
    rows.append({"calculator": "federated_average", "global_weight": round(fed, 6)})

    fieldnames = sorted({key for row in rows for key in row})
    with (OUTPUTS / "privacy_preserving_calculator.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(OUTPUTS / "privacy_preserving_calculator.csv")


if __name__ == "__main__":
    main()
