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
class HistoricalReasoningConfig:
    article: str = "islamic_world_roots_of_algorithmic_reasoning"
    high_significance_threshold: float = 0.78
    high_transmission_threshold: float = 0.80


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


def historical_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "al_khwarizmi_algorism", "procedural_explicitness": 0.92, "transmission_importance": 0.96, "practical_application": 0.88, "representation_importance": 0.94, "modern_resonance": 0.96},
        {"theme_id": "algebraic_transformation", "procedural_explicitness": 0.90, "transmission_importance": 0.92, "practical_application": 0.82, "representation_importance": 0.88, "modern_resonance": 0.92},
        {"theme_id": "hindu_arabic_positional_calculation", "procedural_explicitness": 0.88, "transmission_importance": 0.94, "practical_application": 0.92, "representation_importance": 0.96, "modern_resonance": 0.94},
        {"theme_id": "astronomical_tables", "procedural_explicitness": 0.86, "transmission_importance": 0.84, "practical_application": 0.90, "representation_importance": 0.86, "modern_resonance": 0.84},
        {"theme_id": "cryptanalytic_frequency_analysis", "procedural_explicitness": 0.84, "transmission_importance": 0.72, "practical_application": 0.78, "representation_importance": 0.86, "modern_resonance": 0.90},
        {"theme_id": "practical_inheritance_and_commerce", "procedural_explicitness": 0.88, "transmission_importance": 0.76, "practical_application": 0.96, "representation_importance": 0.78, "modern_resonance": 0.82},
        {"theme_id": "geography_coordinates_mapping", "procedural_explicitness": 0.80, "transmission_importance": 0.76, "practical_application": 0.84, "representation_importance": 0.88, "modern_resonance": 0.84},
        {"theme_id": "mechanical_automata", "procedural_explicitness": 0.78, "transmission_importance": 0.70, "practical_application": 0.76, "representation_importance": 0.74, "modern_resonance": 0.80},
        {"theme_id": "translation_movements", "procedural_explicitness": 0.74, "transmission_importance": 0.98, "practical_application": 0.82, "representation_importance": 0.88, "modern_resonance": 0.86},
    ]


def score_theme(row: dict[str, object], config: HistoricalReasoningConfig) -> dict[str, object]:
    significance_score = mean([
        float(row["procedural_explicitness"]),
        float(row["transmission_importance"]),
        float(row["practical_application"]),
        float(row["representation_importance"]),
        float(row["modern_resonance"]),
    ])

    if significance_score >= config.high_significance_threshold and float(row["transmission_importance"]) >= config.high_transmission_threshold:
        interpretive_status = "core_algorithmic_reasoning_thread"
    elif significance_score >= config.high_significance_threshold:
        interpretive_status = "major_algorithmic_reasoning_thread"
    else:
        interpretive_status = "supporting_algorithmic_reasoning_thread"

    return {
        "theme_id": row["theme_id"],
        "procedural_explicitness": round(float(row["procedural_explicitness"]), 6),
        "transmission_importance": round(float(row["transmission_importance"]), 6),
        "practical_application": round(float(row["practical_application"]), 6),
        "representation_importance": round(float(row["representation_importance"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "significance_score": round(significance_score, 6),
        "interpretive_status": interpretive_status,
    }


def historical_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "avoid_single_origin_story", "meaning": "Algorithms have multiple ancient and medieval lineages."},
        {"caution": "separate_etymology_from_total_origin", "meaning": "The word algorithm is tied to al-Khwarizmi, but procedural reasoning is broader."},
        {"caution": "avoid_preservation_only_framing", "meaning": "Islamic-world scholarship translated, extended, systematized, taught, and transmitted knowledge."},
        {"caution": "avoid_modern_projection", "meaning": "Pre-modern procedures should not be described as modern computer programs."},
        {"caution": "recognize_translation_as_creation", "meaning": "Translation, commentary, pedagogy, and adaptation are forms of intellectual work."},
        {"caution": "include_practical_domains", "meaning": "Commerce, inheritance, surveying, astronomy, geography, cryptanalysis, and devices matter to algorithmic history."},
    ]


def main() -> None:
    config = HistoricalReasoningConfig()
    themes = historical_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = historical_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_algorithmic_reasoning_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_algorithmic_reasoning_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_algorithmic_reasoning_thread"),
        "mean_significance_score": round(mean(float(row["significance_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Islamic-world roots of algorithmic reasoning should be studied as procedural, translational, practical, representational, and institutional history without reducing algorithms to a single-origin story.",
    }

    write_csv(TABLES / "historical_themes.csv", themes)
    write_csv(TABLES / "historical_algorithmic_reasoning_map.csv", scored)
    write_csv(TABLES / "historical_cautions.csv", cautions)
    write_csv(TABLES / "historical_reasoning_summary.csv", [summary])

    write_json(JSON_DIR / "historical_reasoning_config.json", asdict(config))
    write_json(JSON_DIR / "historical_algorithmic_reasoning_map.json", scored)
    write_json(JSON_DIR / "historical_cautions.json", cautions)
    write_json(JSON_DIR / "historical_reasoning_summary.json", summary)

    print("Islamic-world roots of algorithmic reasoning map complete.")
    print(TABLES / "historical_reasoning_summary.csv")


if __name__ == "__main__":
    main()
