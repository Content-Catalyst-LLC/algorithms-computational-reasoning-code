#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    rule_clarity: float,
    predicate_definition: float,
    input_validity: float,
    contradiction_control: float,
    inference_traceability: float,
    constraint_coverage: float,
    testability: float,
    verification_readiness: float,
    explainability: float,
    governance_readiness: float,
) -> dict[str, float | str]:
    quality = clamp(
        100.0 * (
            0.12 * rule_clarity
            + 0.12 * predicate_definition
            + 0.10 * input_validity
            + 0.10 * contradiction_control
            + 0.12 * inference_traceability
            + 0.10 * constraint_coverage
            + 0.10 * testability
            + 0.08 * verification_readiness
            + 0.08 * explainability
            + 0.08 * governance_readiness
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - rule_clarity,
        1.0 - predicate_definition,
        1.0 - input_validity,
        1.0 - contradiction_control,
        1.0 - inference_traceability,
        1.0 - constraint_coverage,
        1.0 - testability,
        1.0 - explainability,
    ]))
    if quality >= 80 and risk <= 25:
        interpretation = "strong logical structure"
    elif quality >= 65 and risk <= 40:
        interpretation = "usable logical structure with review needs"
    elif risk >= 55:
        interpretation = "high logic risk"
    else:
        interpretation = "partial logical structure"
    return {
        "logic_quality": round(quality, 3),
        "logic_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Logic quality calculator.")
    parser.add_argument("--rule-clarity", type=float, default=0.80)
    parser.add_argument("--predicate-definition", type=float, default=0.80)
    parser.add_argument("--input-validity", type=float, default=0.75)
    parser.add_argument("--contradiction-control", type=float, default=0.70)
    parser.add_argument("--inference-traceability", type=float, default=0.75)
    parser.add_argument("--constraint-coverage", type=float, default=0.75)
    parser.add_argument("--testability", type=float, default=0.75)
    parser.add_argument("--verification-readiness", type=float, default=0.65)
    parser.add_argument("--explainability", type=float, default=0.70)
    parser.add_argument("--governance-readiness", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.rule_clarity,
        args.predicate_definition,
        args.input_validity,
        args.contradiction_control,
        args.inference_traceability,
        args.constraint_coverage,
        args.testability,
        args.verification_readiness,
        args.explainability,
        args.governance_readiness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "logic_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
