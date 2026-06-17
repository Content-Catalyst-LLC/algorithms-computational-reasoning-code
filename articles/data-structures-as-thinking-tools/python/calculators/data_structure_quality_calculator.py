#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


FIELDS = [
    "operation_fit",
    "structural_fidelity",
    "invariant_clarity",
    "complexity_awareness",
    "memory_awareness",
    "interpretability",
    "retrieval_support",
    "transformation_support",
    "representation_risk_documentation",
    "governance_readiness",
]

WEIGHTS = [0.12, 0.12, 0.10, 0.10, 0.08, 0.10, 0.10, 0.08, 0.10, 0.10]


def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in [values[0], values[1], values[2], values[3], values[5], values[6], values[8], values[9]])))
    if quality >= 82 and risk <= 22:
        label = "strong data-structure reasoning posture"
    elif quality >= 68 and risk <= 38:
        label = "usable data-structure reasoning posture with review needs"
    elif risk >= 55:
        label = "high structure-mismatch risk"
    else:
        label = "partial data-structure reasoning posture"
    return {
        "structure_reasoning_quality": round(quality, 3),
        "structure_mismatch_risk": round(risk, 3),
        "interpretation": label,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Data-structure reasoning quality and mismatch-risk calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    values = [getattr(args, field) for field in FIELDS]
    result = compute(values)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "data_structure_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
