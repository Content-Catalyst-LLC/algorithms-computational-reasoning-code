#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


FIELDS = [
    "stopping_condition_clarity",
    "progress_measure_definition",
    "invariant_coverage",
    "boundary_case_coverage",
    "invalid_input_handling",
    "recursion_safety",
    "numerical_edge_handling",
    "concurrency_edge_awareness",
    "counterexample_traceability",
    "governance_readiness",
]

WEIGHTS = [0.12, 0.12, 0.12, 0.10, 0.10, 0.08, 0.08, 0.08, 0.10, 0.10]


def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in values[:8])))
    if quality >= 82 and risk <= 22:
        label = "strong boundary reliability posture"
    elif quality >= 68 and risk <= 38:
        label = "usable reliability posture with review needs"
    elif risk >= 55:
        label = "high boundary risk"
    else:
        label = "partial reliability posture"
    return {
        "reliability_quality": round(quality, 3),
        "reliability_risk": round(risk, 3),
        "interpretation": label,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Termination, invariant, and edge-case reliability calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    values = [getattr(args, field) for field in FIELDS]
    result = compute(values)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "reliability_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
