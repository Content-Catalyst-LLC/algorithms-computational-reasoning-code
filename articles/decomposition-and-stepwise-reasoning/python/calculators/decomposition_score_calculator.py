#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    subproblem_clarity: float,
    boundary_definition: float,
    input_output_clarity: float,
    sequencing_quality: float,
    dependency_visibility: float,
    testability: float,
    traceability: float,
    recomposition_quality: float,
    governance_readiness: float,
    risk_awareness: float,
) -> dict[str, float | str]:
    score = clamp(
        100.0 * (
            0.12 * subproblem_clarity
            + 0.10 * boundary_definition
            + 0.10 * input_output_clarity
            + 0.10 * sequencing_quality
            + 0.10 * dependency_visibility
            + 0.12 * testability
            + 0.10 * traceability
            + 0.10 * recomposition_quality
            + 0.08 * governance_readiness
            + 0.08 * risk_awareness
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - boundary_definition,
        1.0 - dependency_visibility,
        1.0 - traceability,
        1.0 - recomposition_quality,
        1.0 - governance_readiness,
        1.0 - risk_awareness,
    ]))
    if score >= 80 and risk <= 25:
        interpretation = "strong decomposition with clear stepwise reasoning"
    elif score >= 65 and risk <= 40:
        interpretation = "usable decomposition with review needs"
    elif risk >= 55:
        interpretation = "high decomposition risk"
    else:
        interpretation = "partial decomposition"
    return {
        "decomposition_score": round(score, 3),
        "decomposition_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Decomposition score calculator.")
    parser.add_argument("--subproblem-clarity", type=float, default=0.80)
    parser.add_argument("--boundary-definition", type=float, default=0.75)
    parser.add_argument("--input-output-clarity", type=float, default=0.75)
    parser.add_argument("--sequencing-quality", type=float, default=0.75)
    parser.add_argument("--dependency-visibility", type=float, default=0.70)
    parser.add_argument("--testability", type=float, default=0.70)
    parser.add_argument("--traceability", type=float, default=0.70)
    parser.add_argument("--recomposition-quality", type=float, default=0.70)
    parser.add_argument("--governance-readiness", type=float, default=0.65)
    parser.add_argument("--risk-awareness", type=float, default=0.65)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.subproblem_clarity,
        args.boundary_definition,
        args.input_output_clarity,
        args.sequencing_quality,
        args.dependency_visibility,
        args.testability,
        args.traceability,
        args.recomposition_quality,
        args.governance_readiness,
        args.risk_awareness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "decomposition_score_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
