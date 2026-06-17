#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean


def compute(values: list[float]) -> dict[str, float | str]:
    weights = [0.10, 0.12, 0.12, 0.12, 0.10, 0.10, 0.10, 0.08, 0.08, 0.08]
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, weights))))
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in values[:8])))
    label = "strong symbolic representation" if quality >= 80 and risk <= 25 else "review needed"
    return {"representation_quality": round(quality, 3), "representation_risk": round(risk, 3), "interpretation": label}


def main() -> None:
    parser = argparse.ArgumentParser(description="Symbolic representation quality calculator.")
    for arg in [
        "alphabet_clarity", "grammar_explicitness", "syntax_validation", "semantic_clarity",
        "parser_readiness", "schema_support", "error_reporting", "testability",
        "interoperability", "governance_readiness"
    ]:
        parser.add_argument(f"--{arg.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    vals = [getattr(args, name) for name in [
        "alphabet_clarity", "grammar_explicitness", "syntax_validation", "semantic_clarity",
        "parser_readiness", "schema_support", "error_reporting", "testability",
        "interoperability", "governance_readiness"
    ]]
    result = compute(vals)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "representation_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
