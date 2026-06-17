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
    constraint_clarity: float,
    state_definition: float,
    objective_alignment: float,
    assumption_documentation: float,
    edge_case_handling: float,
    stopping_condition_clarity: float,
    evaluation_quality: float,
    governance_readiness: float,
) -> dict[str, float | str]:
    score = clamp(
        100.0 * (
            0.10 * input_clarity
            + 0.10 * output_clarity
            + 0.10 * constraint_clarity
            + 0.08 * state_definition
            + 0.14 * objective_alignment
            + 0.12 * assumption_documentation
            + 0.10 * edge_case_handling
            + 0.08 * stopping_condition_clarity
            + 0.10 * evaluation_quality
            + 0.08 * governance_readiness
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - input_clarity,
        1.0 - output_clarity,
        1.0 - constraint_clarity,
        1.0 - objective_alignment,
        1.0 - assumption_documentation,
        1.0 - edge_case_handling,
        1.0 - evaluation_quality,
        1.0 - governance_readiness,
    ]))
    if score >= 80 and risk <= 25:
        interpretation = "strong formalization"
    elif score >= 65 and risk <= 40:
        interpretation = "usable formalization with review needs"
    elif risk >= 55:
        interpretation = "high formalization risk"
    else:
        interpretation = "partial formalization"
    return {
        "formalization_score": round(score, 3),
        "formalization_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Formalization score calculator.")
    parser.add_argument("--input-clarity", type=float, default=0.75)
    parser.add_argument("--output-clarity", type=float, default=0.75)
    parser.add_argument("--constraint-clarity", type=float, default=0.70)
    parser.add_argument("--state-definition", type=float, default=0.70)
    parser.add_argument("--objective-alignment", type=float, default=0.65)
    parser.add_argument("--assumption-documentation", type=float, default=0.60)
    parser.add_argument("--edge-case-handling", type=float, default=0.60)
    parser.add_argument("--stopping-condition-clarity", type=float, default=0.70)
    parser.add_argument("--evaluation-quality", type=float, default=0.65)
    parser.add_argument("--governance-readiness", type=float, default=0.60)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.input_clarity,
        args.output_clarity,
        args.constraint_clarity,
        args.state_definition,
        args.objective_alignment,
        args.assumption_documentation,
        args.edge_case_handling,
        args.stopping_condition_clarity,
        args.evaluation_quality,
        args.governance_readiness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "formalization_score_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
