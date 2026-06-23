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
class AstronomicalPredictionConfig:
    article: str = "astronomical_tables_calendars_and_algorithmic_prediction"
    core_threshold: float = 0.80
    high_predictive_threshold: float = 0.86


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


def astronomical_prediction_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "tables_as_stored_computation", "table_structure": 0.98, "procedural_clarity": 0.90, "predictive_function": 0.92, "institutional_use": 0.86, "correction_awareness": 0.86, "transmission_importance": 0.90, "modern_resonance": 0.94},
        {"theme_id": "calendars_as_rule_systems", "table_structure": 0.86, "procedural_clarity": 0.90, "predictive_function": 0.88, "institutional_use": 0.96, "correction_awareness": 0.88, "transmission_importance": 0.88, "modern_resonance": 0.92},
        {"theme_id": "zij_tabular_astronomy", "table_structure": 0.96, "procedural_clarity": 0.90, "predictive_function": 0.94, "institutional_use": 0.88, "correction_awareness": 0.90, "transmission_importance": 0.94, "modern_resonance": 0.92},
        {"theme_id": "interpolation_and_correction", "table_structure": 0.90, "procedural_clarity": 0.94, "predictive_function": 0.94, "institutional_use": 0.84, "correction_awareness": 0.98, "transmission_importance": 0.86, "modern_resonance": 0.96},
        {"theme_id": "observation_model_procedure", "table_structure": 0.82, "procedural_clarity": 0.88, "predictive_function": 0.92, "institutional_use": 0.86, "correction_awareness": 0.92, "transmission_importance": 0.84, "modern_resonance": 0.94},
        {"theme_id": "timekeeping_ritual_administration", "table_structure": 0.84, "procedural_clarity": 0.86, "predictive_function": 0.88, "institutional_use": 0.98, "correction_awareness": 0.84, "transmission_importance": 0.88, "modern_resonance": 0.90},
        {"theme_id": "instrument_table_human_system", "table_structure": 0.88, "procedural_clarity": 0.86, "predictive_function": 0.88, "institutional_use": 0.88, "correction_awareness": 0.86, "transmission_importance": 0.88, "modern_resonance": 0.92},
    ]


def score_theme(row: dict[str, object], config: AstronomicalPredictionConfig) -> dict[str, object]:
    prediction_score = mean([
        float(row["table_structure"]),
        float(row["procedural_clarity"]),
        float(row["predictive_function"]),
        float(row["institutional_use"]),
        float(row["correction_awareness"]),
        float(row["transmission_importance"]),
        float(row["modern_resonance"]),
    ])

    if prediction_score >= config.core_threshold and float(row["predictive_function"]) >= config.high_predictive_threshold:
        interpretive_status = "core_astronomical_prediction_thread"
    elif prediction_score >= config.core_threshold:
        interpretive_status = "major_astronomical_prediction_thread"
    else:
        interpretive_status = "supporting_astronomical_prediction_thread"

    return {
        "theme_id": row["theme_id"],
        "table_structure": round(float(row["table_structure"]), 6),
        "procedural_clarity": round(float(row["procedural_clarity"]), 6),
        "predictive_function": round(float(row["predictive_function"]), 6),
        "institutional_use": round(float(row["institutional_use"]), 6),
        "correction_awareness": round(float(row["correction_awareness"]), 6),
        "transmission_importance": round(float(row["transmission_importance"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "prediction_score": round(prediction_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_tables_as_passive_lists", "meaning": "Astronomical tables store computation and require rules of use."},
        {"caution": "do_not_equate_prediction_with_certainty", "meaning": "Prediction is structured expectation under assumptions and correction."},
        {"caution": "do_not_separate_calendar_from_institution", "meaning": "Calendars coordinate ritual, administration, agriculture, and public time."},
        {"caution": "do_not_ignore_copying_and_correction", "meaning": "Manuscript transmission can preserve, alter, or repair computation."},
        {"caution": "do_not_project_modern_software_backward", "meaning": "Premodern astronomical tables are computational artifacts, but not modern software."},
    ]


def main() -> None:
    config = AstronomicalPredictionConfig()
    themes = astronomical_prediction_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_astronomical_prediction_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_astronomical_prediction_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_astronomical_prediction_thread"),
        "mean_prediction_score": round(mean(float(row["prediction_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Astronomical tables and calendars should be studied as algorithmic prediction systems: stored computation, procedural lookup, correction, interpolation, calendar rules, and institutional timekeeping.",
    }

    write_csv(TABLES / "astronomical_prediction_themes.csv", themes)
    write_csv(TABLES / "astronomical_prediction_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "astronomical_prediction_summary.csv", [summary])

    write_json(JSON_DIR / "astronomical_prediction_config.json", asdict(config))
    write_json(JSON_DIR / "astronomical_prediction_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "astronomical_prediction_summary.json", summary)

    print("Astronomical tables, calendars, and algorithmic prediction map complete.")
    print(TABLES / "astronomical_prediction_summary.csv")


if __name__ == "__main__":
    main()
