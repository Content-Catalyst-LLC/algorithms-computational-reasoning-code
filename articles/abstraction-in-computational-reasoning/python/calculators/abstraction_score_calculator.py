#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    representation_clarity: float,
    scope_definition: float,
    detail_preservation: float,
    assumption_documentation: float,
    testability: float,
    interpretability: float,
    reuse_safety: float,
    uncertainty_visibility: float,
    governance_readiness: float,
    risk_awareness: float,
) -> dict[str, float | str]:
    score = clamp(
        100.0 * (
            0.12 * representation_clarity
            + 0.10 * scope_definition
            + 0.12 * detail_preservation
            + 0.12 * assumption_documentation
            + 0.10 * testability
            + 0.12 * interpretability
            + 0.08 * reuse_safety
            + 0.08 * uncertainty_visibility
            + 0.08 * governance_readiness
            + 0.08 * risk_awareness
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - scope_definition,
        1.0 - detail_preservation,
        1.0 - assumption_documentation,
        1.0 - interpretability,
        1.0 - reuse_safety,
        1.0 - uncertainty_visibility,
        1.0 - governance_readiness,
        1.0 - risk_awareness,
    ]))
    if score >= 80 and risk <= 25:
        interpretation = "strong abstraction with clear scope and interpretation"
    elif score >= 65 and risk <= 40:
        interpretation = "usable abstraction with review needs"
    elif risk >= 55:
        interpretation = "high abstraction risk"
    else:
        interpretation = "partial abstraction"
    return {
        "abstraction_score": round(score, 3),
        "abstraction_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Abstraction score calculator.")
    parser.add_argument("--representation-clarity", type=float, default=0.80)
    parser.add_argument("--scope-definition", type=float, default=0.70)
    parser.add_argument("--detail-preservation", type=float, default=0.65)
    parser.add_argument("--assumption-documentation", type=float, default=0.65)
    parser.add_argument("--testability", type=float, default=0.70)
    parser.add_argument("--interpretability", type=float, default=0.70)
    parser.add_argument("--reuse-safety", type=float, default=0.65)
    parser.add_argument("--uncertainty-visibility", type=float, default=0.60)
    parser.add_argument("--governance-readiness", type=float, default=0.65)
    parser.add_argument("--risk-awareness", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.representation_clarity,
        args.scope_definition,
        args.detail_preservation,
        args.assumption_documentation,
        args.testability,
        args.interpretability,
        args.reuse_safety,
        args.uncertainty_visibility,
        args.governance_readiness,
        args.risk_awareness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "abstraction_score_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
