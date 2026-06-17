#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


FIELDS = [
    "style_clarity",
    "state_visibility",
    "abstraction_fit",
    "composability",
    "testability",
    "error_handling",
    "traceability",
    "performance_fit",
    "team_readability",
    "governance_readiness",
]
WEIGHTS = [0.12, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.08, 0.10, 0.10]


def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk_fields = [values[0], values[1], values[2], values[4], values[5], values[6], values[8], values[9]]
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in risk_fields)))
    if quality >= 84 and risk <= 20:
        label = "strong computational style"
    elif quality >= 70 and risk <= 35:
        label = "usable computational style with review needs"
    elif risk >= 55:
        label = "high style risk"
    else:
        label = "partial computational style"
    return {
        "style_quality": round(quality, 3),
        "style_risk": round(risk, 3),
        "interpretation": label,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Programming style quality and risk calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    values = [getattr(args, field) for field in FIELDS]
    result = compute(values)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "style_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
