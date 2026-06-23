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
class PracticalCalculationConfig:
    article: str = "trade_inheritance_surveying_and_practical_calculation"
    core_threshold: float = 0.80
    high_institutional_threshold: float = 0.86


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


def practical_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "trade_commercial_reckoning", "procedure": 0.92, "representation": 0.86, "institutional_importance": 0.94, "verification": 0.88, "transmission": 0.86, "modern_resonance": 0.90},
        {"theme_id": "inheritance_allocation", "procedure": 0.94, "representation": 0.88, "institutional_importance": 0.96, "verification": 0.92, "transmission": 0.88, "modern_resonance": 0.90},
        {"theme_id": "surveying_land_measurement", "procedure": 0.90, "representation": 0.92, "institutional_importance": 0.92, "verification": 0.86, "transmission": 0.84, "modern_resonance": 0.88},
        {"theme_id": "proportion_common_measure", "procedure": 0.94, "representation": 0.88, "institutional_importance": 0.90, "verification": 0.88, "transmission": 0.86, "modern_resonance": 0.92},
        {"theme_id": "word_problem_translation", "procedure": 0.88, "representation": 0.90, "institutional_importance": 0.86, "verification": 0.82, "transmission": 0.90, "modern_resonance": 0.88},
        {"theme_id": "written_reckoning_auditability", "procedure": 0.88, "representation": 0.92, "institutional_importance": 0.92, "verification": 0.96, "transmission": 0.90, "modern_resonance": 0.94},
        {"theme_id": "human_calculator_roles", "procedure": 0.82, "representation": 0.84, "institutional_importance": 0.90, "verification": 0.84, "transmission": 0.88, "modern_resonance": 0.86},
    ]


def score_theme(row: dict[str, object], config: PracticalCalculationConfig) -> dict[str, object]:
    practical_score = mean([
        float(row["procedure"]),
        float(row["representation"]),
        float(row["institutional_importance"]),
        float(row["verification"]),
        float(row["transmission"]),
        float(row["modern_resonance"]),
    ])

    if practical_score >= config.core_threshold and float(row["institutional_importance"]) >= config.high_institutional_threshold:
        interpretive_status = "core_practical_calculation_thread"
    elif practical_score >= config.core_threshold:
        interpretive_status = "major_practical_calculation_thread"
    else:
        interpretive_status = "supporting_practical_calculation_thread"

    return {
        "theme_id": row["theme_id"],
        "procedure": round(float(row["procedure"]), 6),
        "representation": round(float(row["representation"]), 6),
        "institutional_importance": round(float(row["institutional_importance"]), 6),
        "verification": round(float(row["verification"]), 6),
        "transmission": round(float(row["transmission"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "practical_score": round(practical_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_practical_math_as_lesser", "meaning": "Practical calculation is a major form of procedural reasoning."},
        {"caution": "do_not_assume_calculation_is_neutral", "meaning": "Allocation, measurement, and accounting have social consequences."},
        {"caution": "do_not_separate_method_from_institution", "meaning": "Trade, inheritance, surveying, and administration shape procedure."},
        {"caution": "do_not_ignore_verification", "meaning": "Practical calculation requires checks, records, and dispute resolution."},
        {"caution": "do_not_project_modern_systems_backward", "meaning": "Historical practical procedures are not identical to modern software systems."},
    ]


def main() -> None:
    config = PracticalCalculationConfig()
    themes = practical_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_practical_calculation_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_practical_calculation_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_practical_calculation_thread"),
        "mean_practical_score": round(mean(float(row["practical_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Practical calculation should be studied as institutional algorithmic reasoning: rule-governed methods for allocation, measurement, trade, recordkeeping, verification, and trust.",
    }

    write_csv(TABLES / "practical_calculation_themes.csv", themes)
    write_csv(TABLES / "practical_calculation_procedure_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "practical_calculation_summary.csv", [summary])

    write_json(JSON_DIR / "practical_calculation_config.json", asdict(config))
    write_json(JSON_DIR / "practical_calculation_procedure_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "practical_calculation_summary.json", summary)

    print("Trade, inheritance, surveying, and practical calculation map complete.")
    print(TABLES / "practical_calculation_summary.csv")


if __name__ == "__main__":
    main()
