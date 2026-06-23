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
class ProceduralLegacyConfig:
    article: str = "al_khwarizmi_algorism_and_the_procedural_imagination"
    core_legacy_threshold: float = 0.82
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


def legacy_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "name_to_algorithm", "procedure": 0.88, "representation": 0.82, "transmission": 0.96, "application": 0.84, "modern_resonance": 0.98},
        {"theme_id": "algorism_written_arithmetic", "procedure": 0.94, "representation": 0.96, "transmission": 0.92, "application": 0.90, "modern_resonance": 0.94},
        {"theme_id": "hindu_arabic_place_value", "procedure": 0.90, "representation": 0.98, "transmission": 0.90, "application": 0.92, "modern_resonance": 0.94},
        {"theme_id": "algebraic_restoration_balancing", "procedure": 0.92, "representation": 0.86, "transmission": 0.90, "application": 0.84, "modern_resonance": 0.92},
        {"theme_id": "problem_classification", "procedure": 0.90, "representation": 0.78, "transmission": 0.82, "application": 0.82, "modern_resonance": 0.88},
        {"theme_id": "verbal_procedure_before_symbols", "procedure": 0.86, "representation": 0.80, "transmission": 0.82, "application": 0.78, "modern_resonance": 0.86},
        {"theme_id": "astronomical_table_computation", "procedure": 0.84, "representation": 0.88, "transmission": 0.78, "application": 0.88, "modern_resonance": 0.82},
        {"theme_id": "latin_algorism_reception", "procedure": 0.84, "representation": 0.86, "transmission": 0.94, "application": 0.86, "modern_resonance": 0.90},
    ]


def score_theme(row: dict[str, object], config: ProceduralLegacyConfig) -> dict[str, object]:
    legacy_score = mean([
        float(row["procedure"]),
        float(row["representation"]),
        float(row["transmission"]),
        float(row["application"]),
        float(row["modern_resonance"]),
    ])

    if legacy_score >= config.core_legacy_threshold and float(row["transmission"]) >= config.high_transmission_threshold:
        interpretive_status = "core_procedural_legacy"
    elif legacy_score >= config.core_legacy_threshold:
        interpretive_status = "major_procedural_legacy"
    else:
        interpretive_status = "supporting_procedural_legacy"

    return {
        "theme_id": row["theme_id"],
        "procedure": round(float(row["procedure"]), 6),
        "representation": round(float(row["representation"]), 6),
        "transmission": round(float(row["transmission"]), 6),
        "application": round(float(row["application"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "legacy_score": round(legacy_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_claim_single_invention", "meaning": "Al-Khwārizmī is central to algorithmic naming and transmission, not the sole origin of algorithms."},
        {"caution": "do_not_confuse_algorism_with_all_algorithms", "meaning": "Algorism is historically tied to written arithmetic with Hindu-Arabic numerals; algorithm later generalizes."},
        {"caution": "do_not_project_modern_code_backwards", "meaning": "Verbal and tabular procedures are algorithmic without being computer programs."},
        {"caution": "do_not_ignore_representation", "meaning": "Numerals, tables, prose, and classifications shape what procedures can do."},
        {"caution": "do_not_separate_method_from_transmission", "meaning": "Translation, teaching, and reception are part of procedural history."},
        {"caution": "do_not_reduce_to_etymology", "meaning": "The word history matters, but the procedural content matters too."},
    ]


def main() -> None:
    config = ProceduralLegacyConfig()
    themes = legacy_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_legacy_threads": sum(1 for row in scored if row["interpretive_status"] == "core_procedural_legacy"),
        "major_legacy_threads": sum(1 for row in scored if row["interpretive_status"] == "major_procedural_legacy"),
        "supporting_legacy_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_procedural_legacy"),
        "mean_legacy_score": round(mean(float(row["legacy_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Al-Khwārizmī's legacy should be studied as a procedural, representational, and translational history: central to algorism and algorithmic naming, but not reducible to a single-origin myth.",
    }

    write_csv(TABLES / "procedural_legacy_themes.csv", themes)
    write_csv(TABLES / "al_khwarizmi_procedural_legacy_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "procedural_legacy_summary.csv", [summary])

    write_json(JSON_DIR / "procedural_legacy_config.json", asdict(config))
    write_json(JSON_DIR / "al_khwarizmi_procedural_legacy_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "procedural_legacy_summary.json", summary)

    print("Al-Khwārizmī procedural legacy map complete.")
    print(TABLES / "procedural_legacy_summary.csv")


if __name__ == "__main__":
    main()
