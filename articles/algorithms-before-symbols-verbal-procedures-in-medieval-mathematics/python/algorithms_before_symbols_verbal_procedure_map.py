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
class VerbalProcedureConfig:
    article: str = "algorithms_before_symbols_verbal_procedures_in_medieval_mathematics"
    core_threshold: float = 0.80
    high_procedural_clarity_threshold: float = 0.86


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


def verbal_procedure_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "rhetorical_algebra", "procedural_clarity": 0.90, "representation_dependence": 0.86, "pedagogical_value": 0.88, "transmission_importance": 0.90, "practical_use": 0.82, "modern_resonance": 0.88},
        {"theme_id": "problem_classification", "procedural_clarity": 0.92, "representation_dependence": 0.82, "pedagogical_value": 0.90, "transmission_importance": 0.84, "practical_use": 0.86, "modern_resonance": 0.90},
        {"theme_id": "worked_examples", "procedural_clarity": 0.94, "representation_dependence": 0.82, "pedagogical_value": 0.96, "transmission_importance": 0.90, "practical_use": 0.88, "modern_resonance": 0.86},
        {"theme_id": "geometric_demonstration", "procedural_clarity": 0.84, "representation_dependence": 0.92, "pedagogical_value": 0.88, "transmission_importance": 0.82, "practical_use": 0.78, "modern_resonance": 0.86},
        {"theme_id": "table_lookup_interpolation", "procedural_clarity": 0.88, "representation_dependence": 0.90, "pedagogical_value": 0.84, "transmission_importance": 0.86, "practical_use": 0.92, "modern_resonance": 0.90},
        {"theme_id": "commercial_reckoning_rules", "procedural_clarity": 0.88, "representation_dependence": 0.82, "pedagogical_value": 0.86, "transmission_importance": 0.84, "practical_use": 0.96, "modern_resonance": 0.84},
        {"theme_id": "manuscript_commentary_transmission", "procedural_clarity": 0.78, "representation_dependence": 0.86, "pedagogical_value": 0.88, "transmission_importance": 0.96, "practical_use": 0.82, "modern_resonance": 0.84},
        {"theme_id": "symbolic_compression", "procedural_clarity": 0.86, "representation_dependence": 0.88, "pedagogical_value": 0.82, "transmission_importance": 0.82, "practical_use": 0.80, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: VerbalProcedureConfig) -> dict[str, object]:
    verbal_score = mean([
        float(row["procedural_clarity"]),
        float(row["representation_dependence"]),
        float(row["pedagogical_value"]),
        float(row["transmission_importance"]),
        float(row["practical_use"]),
        float(row["modern_resonance"]),
    ])

    if verbal_score >= config.core_threshold and float(row["procedural_clarity"]) >= config.high_procedural_clarity_threshold:
        interpretive_status = "core_verbal_procedure_thread"
    elif verbal_score >= config.core_threshold:
        interpretive_status = "major_verbal_procedure_thread"
    else:
        interpretive_status = "supporting_verbal_procedure_thread"

    return {
        "theme_id": row["theme_id"],
        "procedural_clarity": round(float(row["procedural_clarity"]), 6),
        "representation_dependence": round(float(row["representation_dependence"]), 6),
        "pedagogical_value": round(float(row["pedagogical_value"]), 6),
        "transmission_importance": round(float(row["transmission_importance"]), 6),
        "practical_use": round(float(row["practical_use"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "verbal_procedure_score": round(verbal_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_verbal_with_vague", "meaning": "Verbal procedure can be precise within a technical tradition."},
        {"caution": "do_not_project_modern_symbols_backward", "meaning": "Medieval procedures should not be judged only by modern symbolic notation."},
        {"caution": "do_not_equate_procedure_with_programming", "meaning": "Pre-modern mathematical procedures are algorithmic without being computer code."},
        {"caution": "do_not_ignore_examples", "meaning": "Worked examples often carry the general method."},
        {"caution": "do_not_make_transmission_passive", "meaning": "Manuscripts, translations, commentaries, and teaching reshape procedure."},
    ]


def main() -> None:
    config = VerbalProcedureConfig()
    themes = verbal_procedure_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_verbal_procedure_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_verbal_procedure_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_verbal_procedure_thread"),
        "mean_verbal_procedure_score": round(mean(float(row["verbal_procedure_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Algorithms before symbols should be studied as verbal, pedagogical, representational, practical, and transmissible procedures rather than as modern code projected backward.",
    }

    write_csv(TABLES / "verbal_procedure_themes.csv", themes)
    write_csv(TABLES / "verbal_procedure_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "verbal_procedure_summary.csv", [summary])

    write_json(JSON_DIR / "verbal_procedure_config.json", asdict(config))
    write_json(JSON_DIR / "verbal_procedure_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "verbal_procedure_summary.json", summary)

    print("Algorithms before symbols verbal procedure map complete.")
    print(TABLES / "verbal_procedure_summary.csv")


if __name__ == "__main__":
    main()
