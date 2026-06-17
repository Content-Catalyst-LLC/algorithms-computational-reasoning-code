#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean

FIELDS = ["translation_clarity","semantic_checking","optimization_traceability","runtime_visibility","diagnostics_quality","portability","reproducibility","security_boundaries","performance_fit","governance_readiness"]
WEIGHTS = [0.10,0.10,0.10,0.10,0.10,0.10,0.12,0.12,0.08,0.08]

def compute(values: list[float]) -> dict[str, float | str]:
    quality = max(0.0, min(100.0, 100.0 * sum(v * w for v, w in zip(values, WEIGHTS))))
    risk_fields = [values[0], values[1], values[2], values[3], values[4], values[6], values[7], values[9]]
    risk = max(0.0, min(100.0, 100.0 * mean(1.0 - v for v in risk_fields)))
    if quality >= 84 and risk <= 20:
        label = "strong execution model"
    elif quality >= 70 and risk <= 35:
        label = "usable execution model with review needs"
    elif risk >= 55:
        label = "high execution risk"
    else:
        label = "partial execution discipline"
    return {"execution_quality": round(quality, 3), "execution_risk": round(risk, 3), "interpretation": label}

def main() -> None:
    parser = argparse.ArgumentParser(description="Execution quality and execution-risk calculator.")
    for field in FIELDS:
        parser.add_argument(f"--{field.replace('_', '-')}", type=float, default=0.75)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute([getattr(args, field) for field in FIELDS])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "execution_quality_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
