from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class PositionalCalculationConfig:
    article: str = "hindu_arabic_numerals_and_the_transmission_of_positional_calculation"
    core_threshold: float = 0.80
    high_representation_threshold: float = 0.86


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def positional_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "decimal_place_value", "representation": 0.98, "procedure": 0.94, "transmission": 0.88, "practical_use": 0.92, "pedagogy": 0.92, "modern_resonance": 0.96},
        {"theme_id": "zero_placeholder", "representation": 0.96, "procedure": 0.88, "transmission": 0.86, "practical_use": 0.90, "pedagogy": 0.88, "modern_resonance": 0.96},
        {"theme_id": "written_algorism", "representation": 0.90, "procedure": 0.96, "transmission": 0.94, "practical_use": 0.92, "pedagogy": 0.96, "modern_resonance": 0.92},
        {"theme_id": "carrying_and_borrowing", "representation": 0.88, "procedure": 0.96, "transmission": 0.84, "practical_use": 0.94, "pedagogy": 0.92, "modern_resonance": 0.90},
        {"theme_id": "commercial_reckoning", "representation": 0.84, "procedure": 0.90, "transmission": 0.86, "practical_use": 0.98, "pedagogy": 0.88, "modern_resonance": 0.86},
        {"theme_id": "astronomical_tables", "representation": 0.86, "procedure": 0.88, "transmission": 0.84, "practical_use": 0.90, "pedagogy": 0.82, "modern_resonance": 0.86},
        {"theme_id": "latin_reception", "representation": 0.82, "procedure": 0.84, "transmission": 0.96, "practical_use": 0.90, "pedagogy": 0.94, "modern_resonance": 0.88},
        {"theme_id": "numeral_form_variation", "representation": 0.88, "procedure": 0.76, "transmission": 0.92, "practical_use": 0.78, "pedagogy": 0.82, "modern_resonance": 0.80},
    ]


def score_theme(row: dict[str, object], config: PositionalCalculationConfig) -> dict[str, object]:
    positional_score = mean([
        float(row["representation"]),
        float(row["procedure"]),
        float(row["transmission"]),
        float(row["practical_use"]),
        float(row["pedagogy"]),
        float(row["modern_resonance"]),
    ])

    if positional_score >= config.core_threshold and float(row["representation"]) >= config.high_representation_threshold:
        interpretive_status = "core_positional_calculation_thread"
    elif positional_score >= config.core_threshold:
        interpretive_status = "major_positional_calculation_thread"
    else:
        interpretive_status = "supporting_positional_calculation_thread"

    return {
        "theme_id": row["theme_id"],
        "representation": round(float(row["representation"]), 6),
        "procedure": round(float(row["procedure"]), 6),
        "transmission": round(float(row["transmission"]), 6),
        "practical_use": round(float(row["practical_use"]), 6),
        "pedagogy": round(float(row["pedagogy"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "positional_score": round(positional_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_erase_indian_origins", "meaning": "The decimal positional system developed in Indian mathematical contexts."},
        {"caution": "do_not_erase_arabic_transmission", "meaning": "Arabic and Islamic-world scholarship adapted, taught, and transmitted the numerals and procedures."},
        {"caution": "do_not_reduce_to_digit_shapes", "meaning": "Glyph forms matter, but place-value structure and procedures matter too."},
        {"caution": "do_not_treat_zero_as_trivial", "meaning": "Zero is both a placeholder and a conceptual arithmetic object."},
        {"caution": "do_not_make_transmission_passive", "meaning": "Translation, pedagogy, practical use, and reception are active historical work."},
    ]


def main() -> None:
    config = PositionalCalculationConfig()
    themes = positional_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_positional_calculation_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_positional_calculation_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_positional_calculation_thread"),
        "mean_positional_score": round(mean(float(row["positional_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Hindu-Arabic numerals should be studied as representational, procedural, pedagogical, practical, and translational infrastructure for algorithmic reasoning.",
    }

    write_csv(TABLES / "positional_calculation_themes.csv", themes)
    write_csv(TABLES / "positional_calculation_transmission_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "positional_calculation_summary.csv", [summary])

    write_json(JSON_DIR / "positional_calculation_config.json", asdict(config))
    write_json(JSON_DIR / "positional_calculation_transmission_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "positional_calculation_summary.json", summary)

    print("Hindu-Arabic numerals positional calculation map complete.")
    print(TABLES / "positional_calculation_summary.csv")


if __name__ == "__main__":
    main()
