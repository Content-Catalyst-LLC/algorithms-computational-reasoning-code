#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


FIELDS = [
    "expression_clarity",
    "binding_safety",
    "substitution_discipline",
    "reduction_traceability",
    "evaluation_strategy_clarity",
    "recursion_awareness",
    "type_discipline_clarity",
    "proof_connection",
    "implementation_relevance",
    "governance_readiness",
]

WEIGHTS = [0.10, 0.12, 0.12, 0.10, 0.10, 0.08, 0.12, 0.08, 0.08, 0.10]


def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in [values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[9]])))
    if quality >= 82 and risk <= 22:
        label = "strong lambda-calculus reasoning posture"
    elif quality >= 68 and risk <= 38:
        label = "usable lambda-calculus reasoning posture with review needs"
    elif risk >= 55:
        label = "high formalization risk"
    else:
        label = "partial lambda-calculus reasoning posture"
    return {
        "lambda_reasoning_quality": round(quality, 3),
        "formalization_risk": round(risk, 3),
        "interpretation": label,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Lambda reasoning quality and formalization risk calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    values = [getattr(args, field) for field in FIELDS]
    result = compute(values)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "lambda_reasoning_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
