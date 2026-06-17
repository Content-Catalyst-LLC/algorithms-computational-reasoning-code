#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    step_clarity: float,
    decomposition: float,
    control_flow: float,
    testability: float,
    representation_quality: float,
    data_context: float,
    complexity_awareness: float,
    interpretability: float,
    governance_readiness: float,
    stakeholder_awareness: float,
) -> dict[str, float | str]:
    algorithmic = clamp(100.0 * (0.28 * step_clarity + 0.24 * decomposition + 0.24 * control_flow + 0.24 * testability))
    computational = clamp(
        100.0 * (
            0.11 * step_clarity
            + 0.10 * decomposition
            + 0.09 * control_flow
            + 0.10 * testability
            + 0.13 * representation_quality
            + 0.12 * data_context
            + 0.11 * complexity_awareness
            + 0.12 * interpretability
            + 0.12 * governance_readiness
            + 0.10 * stakeholder_awareness
        )
    )
    gap = computational - algorithmic
    if gap >= 15:
        interpretation = "computational reasoning is stronger than procedural design"
    elif gap <= -15:
        interpretation = "procedural algorithmic thinking is stronger than broader computational reasoning"
    else:
        interpretation = "scores are relatively balanced"
    return {
        "algorithmic_thinking_score": round(algorithmic, 3),
        "computational_reasoning_score": round(computational, 3),
        "reasoning_gap": round(gap, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Reasoning gap calculator.")
    parser.add_argument("--step-clarity", type=float, default=0.80)
    parser.add_argument("--decomposition", type=float, default=0.75)
    parser.add_argument("--control-flow", type=float, default=0.75)
    parser.add_argument("--testability", type=float, default=0.70)
    parser.add_argument("--representation-quality", type=float, default=0.70)
    parser.add_argument("--data-context", type=float, default=0.65)
    parser.add_argument("--complexity-awareness", type=float, default=0.65)
    parser.add_argument("--interpretability", type=float, default=0.65)
    parser.add_argument("--governance-readiness", type=float, default=0.60)
    parser.add_argument("--stakeholder-awareness", type=float, default=0.60)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.step_clarity,
        args.decomposition,
        args.control_flow,
        args.testability,
        args.representation_quality,
        args.data_context,
        args.complexity_awareness,
        args.interpretability,
        args.governance_readiness,
        args.stakeholder_awareness,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "reasoning_gap_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
