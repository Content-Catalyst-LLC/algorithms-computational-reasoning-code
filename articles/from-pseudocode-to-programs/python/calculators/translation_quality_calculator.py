#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    intent_clarity: float,
    input_specification: float,
    output_specification: float,
    state_handling: float,
    control_flow_fidelity: float,
    edge_case_coverage: float,
    error_handling: float,
    test_coverage: float,
    readability: float,
    maintainability: float,
) -> dict[str, float | str]:
    quality = clamp(
        100.0 * (
            0.12 * intent_clarity
            + 0.10 * input_specification
            + 0.10 * output_specification
            + 0.10 * state_handling
            + 0.12 * control_flow_fidelity
            + 0.10 * edge_case_coverage
            + 0.10 * error_handling
            + 0.10 * test_coverage
            + 0.08 * readability
            + 0.08 * maintainability
        )
    )
    risk = clamp(100.0 * mean([
        1.0 - intent_clarity,
        1.0 - input_specification,
        1.0 - output_specification,
        1.0 - control_flow_fidelity,
        1.0 - edge_case_coverage,
        1.0 - error_handling,
        1.0 - test_coverage,
        1.0 - maintainability,
    ]))
    if quality >= 80 and risk <= 25:
        interpretation = "strong translation"
    elif quality >= 65 and risk <= 40:
        interpretation = "usable translation with review needs"
    elif risk >= 55:
        interpretation = "high translation risk"
    else:
        interpretation = "partial translation"
    return {
        "translation_quality": round(quality, 3),
        "translation_risk": round(risk, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Pseudocode-to-program translation quality calculator.")
    parser.add_argument("--intent-clarity", type=float, default=0.80)
    parser.add_argument("--input-specification", type=float, default=0.75)
    parser.add_argument("--output-specification", type=float, default=0.75)
    parser.add_argument("--state-handling", type=float, default=0.70)
    parser.add_argument("--control-flow-fidelity", type=float, default=0.80)
    parser.add_argument("--edge-case-coverage", type=float, default=0.65)
    parser.add_argument("--error-handling", type=float, default=0.65)
    parser.add_argument("--test-coverage", type=float, default=0.70)
    parser.add_argument("--readability", type=float, default=0.75)
    parser.add_argument("--maintainability", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.intent_clarity,
        args.input_specification,
        args.output_specification,
        args.state_handling,
        args.control_flow_fidelity,
        args.edge_case_coverage,
        args.error_handling,
        args.test_coverage,
        args.readability,
        args.maintainability,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "translation_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
