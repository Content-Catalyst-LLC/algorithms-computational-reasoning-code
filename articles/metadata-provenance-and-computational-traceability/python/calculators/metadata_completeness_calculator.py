#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = [
    "title",
    "creator",
    "source",
    "date",
    "format",
    "version",
    "license",
    "access_level",
    "quality_note",
    "checksum",
]


def compute(present_fields: list[str]) -> dict[str, object]:
    present = set(field.strip() for field in present_fields if field.strip())
    missing = [field for field in REQUIRED_FIELDS if field not in present]
    completeness = (len(REQUIRED_FIELDS) - len(missing)) / len(REQUIRED_FIELDS)
    return {
        "required_field_count": len(REQUIRED_FIELDS),
        "present_field_count": len(REQUIRED_FIELDS) - len(missing),
        "missing_fields": missing,
        "metadata_completeness": round(completeness * 100, 2),
        "interpretation": "Metadata completeness is only a first check; accuracy, timeliness, provenance, and stewardship still require review.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Metadata completeness calculator.")
    parser.add_argument("--fields", default="title,creator,source,date,format,version")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute(args.fields.split(","))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "metadata_completeness_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
