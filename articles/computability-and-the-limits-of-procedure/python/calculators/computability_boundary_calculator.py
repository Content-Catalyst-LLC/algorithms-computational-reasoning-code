#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


FIELDS = [
    "procedure_definition",
    "input_domain_clarity",
    "decision_status_clarity",
    "termination_guarantee",
    "recognizability_status",
    "reduction_awareness",
    "approximation_honesty",
    "automation_scope_clarity",
    "traceability",
    "governance_readiness",
]

WEIGHTS = [0.10, 0.10, 0.12, 0.12, 0.10, 0.10, 0.10, 0.10, 0.08, 0.08]


def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in values[2:])))
    if quality >= 82 and risk <= 22:
        label = "strong computability-boundary posture"
    elif quality >= 68 and risk <= 38:
        label = "usable computability-boundary posture with review needs"
    elif risk >= 55:
        label = "high procedural overclaim risk"
    else:
        label = "partial computability-boundary posture"
    return {
        "computability_boundary_quality": round(quality, 3),
        "procedural_overclaim_risk": round(risk, 3),
        "interpretation": label,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Computability boundary and procedural-overclaim calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    values = [getattr(args, field) for field in FIELDS]
    result = compute(values)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "computability_boundary_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
