#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    reproducibility: float,
    expected_behavior_clarity: float,
    trace_quality: float,
    hypothesis_strength: float,
    isolation_quality: float,
    edge_case_awareness: float,
    fix_verification: float,
    regression_testing: float,
    documentation_quality: float,
    governance_readiness: float,
) -> dict[str, float | str]:
    quality = clamp(
        100.0 * (
            0.12 * reproducibility
            + 0.10 * expected_behavior_clarity
            + 0.10 * trace_quality
            + 0.10 * hypothesis_strength
            + 0.10 * isolation_quality
            + 0.10 * edge_case_awareness
            + 0.12 * fix_verification
            + 0.10 * regression_testing
            + 0.08 * documentation_quality
            + 0.08 * governance_readiness
        )
    )
    recurrence = clamp(100.0 * mean([
        1.0 - reproducibility,
        1.0 - expected_behavior_clarity,
        1.0 - trace_quality,
        1.0 - isolation_quality,
        1.0 - edge_case_awareness,
        1.0 - fix_verification,
        1.0 - regression_testing,
        1.0 - documentation_quality,
    ]))
    if quality >= 80 and recurrence <= 25:
        interpretation = "strong debugging process"
    elif quality >= 65 and recurrence <= 40:
        interpretation = "usable debugging process with review needs"
    elif recurrence >= 55:
        interpretation = "high recurrence risk"
    else:
        interpretation = "partial debugging process"
    return {
        "debugging_quality": round(quality, 3),
        "recurrence_risk": round(recurrence, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Debugging quality calculator.")
    parser.add_argument("--reproducibility", type=float, default=0.80)
    parser.add_argument("--expected-behavior-clarity", type=float, default=0.75)
    parser.add_argument("--trace-quality", type=float, default=0.70)
    parser.add_argument("--hypothesis-strength", type=float, default=0.70)
    parser.add_argument("--isolation-quality", type=float, default=0.70)
    parser.add_argument("--edge-case-awareness", type=float, default=0.70)
    parser.add_argument("--fix-verification", type=float, default=0.75)
    parser.add_argument("--regression-testing", type=float, default=0.70)
    parser.add_argument("--documentation-quality", type=float, default=0.65)
    parser.add_argument("--governance-readiness", type=float, default=0.65)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.reproducibility,
        args.expected_behavior_clarity,
        args.trace_quality,
        args.hypothesis_strength,
        args.isolation_quality,
        args.edge_case_awareness,
        args.fix_verification,
        args.regression_testing,
        args.documentation_quality,
        args.governance_readiness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "debugging_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
