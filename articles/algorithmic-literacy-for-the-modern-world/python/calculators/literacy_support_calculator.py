#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def compute(
    procedural_transparency: float,
    data_visibility: float,
    output_interpretability: float,
    uncertainty_communication: float,
    contestability: float,
    governance_readiness: float,
    impact_awareness: float,
    human_judgment_support: float,
) -> dict[str, float | str]:
    support = clamp(
        100.0 * (
            0.14 * procedural_transparency
            + 0.12 * data_visibility
            + 0.14 * output_interpretability
            + 0.12 * uncertainty_communication
            + 0.12 * contestability
            + 0.12 * governance_readiness
            + 0.12 * impact_awareness
            + 0.12 * human_judgment_support
        )
    )
    gap = clamp(100.0 * mean([
        1.0 - procedural_transparency,
        1.0 - data_visibility,
        1.0 - output_interpretability,
        1.0 - uncertainty_communication,
        1.0 - contestability,
        1.0 - governance_readiness,
        1.0 - impact_awareness,
        1.0 - human_judgment_support,
    ]))
    if support >= 80 and gap <= 25:
        interpretation = "strong literacy support"
    elif support >= 65 and gap <= 40:
        interpretation = "moderate literacy support with review needs"
    elif gap >= 55:
        interpretation = "high literacy gap"
    else:
        interpretation = "partial literacy support"
    return {
        "literacy_support_score": round(support, 3),
        "literacy_gap_score": round(gap, 3),
        "interpretation": interpretation,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Algorithmic literacy support calculator.")
    parser.add_argument("--procedural-transparency", type=float, default=0.65)
    parser.add_argument("--data-visibility", type=float, default=0.60)
    parser.add_argument("--output-interpretability", type=float, default=0.65)
    parser.add_argument("--uncertainty-communication", type=float, default=0.55)
    parser.add_argument("--contestability", type=float, default=0.55)
    parser.add_argument("--governance-readiness", type=float, default=0.60)
    parser.add_argument("--impact-awareness", type=float, default=0.75)
    parser.add_argument("--human-judgment-support", type=float, default=0.70)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()

    result = compute(
        args.procedural_transparency,
        args.data_visibility,
        args.output_interpretability,
        args.uncertainty_communication,
        args.contestability,
        args.governance_readiness,
        args.impact_awareness,
        args.human_judgment_support,
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "literacy_support_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
