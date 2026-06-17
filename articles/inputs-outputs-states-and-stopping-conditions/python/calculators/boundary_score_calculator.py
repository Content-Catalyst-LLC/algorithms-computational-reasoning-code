#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    input_clarity: float,
    output_clarity: float,
    state_definition: float,
    transition_clarity: float,
    stopping_condition_clarity: float,
    validation_quality: float,
    edge_case_handling: float,
    failure_reporting: float,
    interpretability: float,
    governance_readiness: float,
) -> dict[str, float | str]:
    score = clamp(
        100.0 * (
            0.12 * input_clarity
            + 0.12 * output_clarity
            + 0.12 * state_definition
            + 0.10 * transition_clarity
            + 0.12 * stopping_condition_clarity
            + 0.10 * validation_quality
            + 0.08 * edge_case_handling
            + 0.08 * failure_reporting
            + 0.08 * interpretability
            + 0.08 * governance_readiness
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - input_clarity,
        1.0 - output_clarity,
        1.0 - state_definition,
        1.0 - stopping_condition_clarity,
        1.0 - edge_case_handling,
        1.0 - failure_reporting,
        1.0 - interpretability,
        1.0 - governance_readiness,
    ]))
    if score >= 80 and risk <= 25:
        interpretation = "strong boundary specification"
    elif score >= 65 and risk <= 40:
        interpretation = "usable boundary specification with review needs"
    elif risk >= 55:
        interpretation = "high procedural-boundary risk"
    else:
        interpretation = "partial boundary specification"
    return {
        "boundary_score": round(score, 3),
        "boundary_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Boundary score calculator.")
    parser.add_argument("--input-clarity", type=float, default=0.80)
    parser.add_argument("--output-clarity", type=float, default=0.75)
    parser.add_argument("--state-definition", type=float, default=0.75)
    parser.add_argument("--transition-clarity", type=float, default=0.70)
    parser.add_argument("--stopping-condition-clarity", type=float, default=0.70)
    parser.add_argument("--validation-quality", type=float, default=0.70)
    parser.add_argument("--edge-case-handling", type=float, default=0.65)
    parser.add_argument("--failure-reporting", type=float, default=0.65)
    parser.add_argument("--interpretability", type=float, default=0.65)
    parser.add_argument("--governance-readiness", type=float, default=0.65)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.input_clarity,
        args.output_clarity,
        args.state_definition,
        args.transition_clarity,
        args.stopping_condition_clarity,
        args.validation_quality,
        args.edge_case_handling,
        args.failure_reporting,
        args.interpretability,
        args.governance_readiness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "boundary_score_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
