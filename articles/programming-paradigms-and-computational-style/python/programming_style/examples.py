from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv


def procedural_average(values: list[float]) -> float:
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    if count == 0:
        return 0.0
    return total / count


def functional_average(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


@dataclass(frozen=True)
class StyleRecord:
    paradigm: str
    central_unit: str
    reasoning_emphasis: str
    example_language_or_context: str


def load_paradigm_taxonomy(article_root: Path) -> list[StyleRecord]:
    path = article_root / "data" / "synthetic_paradigm_taxonomy.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            StyleRecord(
                row["paradigm"],
                row["central_unit"],
                row["reasoning_emphasis"],
                row["example_language_or_context"],
            )
            for row in csv.DictReader(handle)
        ]


def demo_styles(article_root: Path | None = None) -> dict[str, object]:
    values = [0.90, 0.82, 0.88, 0.86]
    payload: dict[str, object] = {
        "values": values,
        "procedural_average": round(procedural_average(values), 4),
        "functional_average": round(functional_average(values), 4),
        "interpretation": "Different styles can compute the same result while making different reasoning structures visible.",
    }
    if article_root is not None:
        taxonomy_path = article_root / "data" / "synthetic_paradigm_taxonomy.csv"
        if taxonomy_path.exists():
            payload["paradigm_count"] = len(load_paradigm_taxonomy(article_root))
    return payload
