#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def compute(boundaries: int, validated_boundaries: int, typed_errors: int, documented_schemas: int) -> dict[str, object]:
    total = max(1, boundaries)
    validation_ratio = min(1.0, validated_boundaries / total)
    typed_error_ratio = min(1.0, typed_errors / total)
    schema_ratio = min(1.0, documented_schemas / total)
    score = round(100.0 * (0.45 * validation_ratio + 0.25 * typed_error_ratio + 0.30 * schema_ratio), 2)
    return {
        "boundaries": boundaries,
        "validated_boundaries": validated_boundaries,
        "typed_errors": typed_errors,
        "documented_schemas": documented_schemas,
        "boundary_validation_score": score,
        "interpretation": "Boundary validation improves when external inputs are checked, schemas are documented, and errors are typed specifically.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Boundary validation calculator.")
    parser.add_argument("--boundaries", type=int, default=8)
    parser.add_argument("--validated-boundaries", type=int, default=7)
    parser.add_argument("--typed-errors", type=int, default=6)
    parser.add_argument("--documented-schemas", type=int, default=7)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute(args.boundaries, args.validated_boundaries, args.typed_errors, args.documented_schemas)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "boundary_validation_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
