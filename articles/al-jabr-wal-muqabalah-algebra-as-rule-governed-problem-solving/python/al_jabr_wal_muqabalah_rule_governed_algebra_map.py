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
class AlgebraProcedureConfig:
    article: str = "al_jabr_wal_muqabalah_algebra_as_rule_governed_problem_solving"
    core_threshold: float = 0.80
    high_transformation_threshold: float = 0.85


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


def algebraic_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "restoration_al_jabr", "classification": 0.82, "transformation": 0.94, "representation": 0.84, "demonstration": 0.78, "practical_use": 0.84, "transmission": 0.90, "modern_resonance": 0.92},
        {"theme_id": "balancing_al_muqabalah", "classification": 0.84, "transformation": 0.92, "representation": 0.84, "demonstration": 0.80, "practical_use": 0.82, "transmission": 0.88, "modern_resonance": 0.92},
        {"theme_id": "equation_type_classification", "classification": 0.96, "transformation": 0.86, "representation": 0.82, "demonstration": 0.78, "practical_use": 0.84, "transmission": 0.86, "modern_resonance": 0.90},
        {"theme_id": "unknown_quantity", "classification": 0.84, "transformation": 0.86, "representation": 0.92, "demonstration": 0.78, "practical_use": 0.82, "transmission": 0.86, "modern_resonance": 0.94},
        {"theme_id": "completing_the_square", "classification": 0.86, "transformation": 0.96, "representation": 0.90, "demonstration": 0.92, "practical_use": 0.78, "transmission": 0.84, "modern_resonance": 0.92},
        {"theme_id": "verbal_algebra", "classification": 0.80, "transformation": 0.84, "representation": 0.88, "demonstration": 0.76, "practical_use": 0.82, "transmission": 0.86, "modern_resonance": 0.84},
        {"theme_id": "practical_word_problems", "classification": 0.82, "transformation": 0.82, "representation": 0.80, "demonstration": 0.74, "practical_use": 0.94, "transmission": 0.82, "modern_resonance": 0.84},
    ]


def score_theme(row: dict[str, object], config: AlgebraProcedureConfig) -> dict[str, object]:
    procedure_score = mean([
        float(row["classification"]),
        float(row["transformation"]),
        float(row["representation"]),
        float(row["demonstration"]),
        float(row["practical_use"]),
        float(row["transmission"]),
        float(row["modern_resonance"]),
    ])

    if procedure_score >= config.core_threshold and float(row["transformation"]) >= config.high_transformation_threshold:
        interpretive_status = "core_rule_governed_algebra_thread"
    elif procedure_score >= config.core_threshold:
        interpretive_status = "major_rule_governed_algebra_thread"
    else:
        interpretive_status = "supporting_rule_governed_algebra_thread"

    return {
        "theme_id": row["theme_id"],
        "classification": round(float(row["classification"]), 6),
        "transformation": round(float(row["transformation"]), 6),
        "representation": round(float(row["representation"]), 6),
        "demonstration": round(float(row["demonstration"]), 6),
        "practical_use": round(float(row["practical_use"]), 6),
        "transmission": round(float(row["transmission"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "procedure_score": round(procedure_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_project_symbolic_notation_backward", "meaning": "Early algebra often used verbal procedure rather than modern symbolic notation."},
        {"caution": "do_not_reduce_algebra_to_word_origin", "meaning": "Al-jabr matters as procedure, not only as etymology."},
        {"caution": "do_not_claim_single_origin", "meaning": "Algebraic reasoning has multiple ancient and medieval roots."},
        {"caution": "do_not_separate_procedure_from_proof", "meaning": "Geometric demonstration and correctness reasoning matter."},
        {"caution": "do_not_ignore_practical_context", "meaning": "Inheritance, commerce, surveying, and education shaped algebraic use."},
    ]


def main() -> None:
    config = AlgebraProcedureConfig()
    themes = algebraic_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_rule_governed_algebra_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_rule_governed_algebra_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_rule_governed_algebra_thread"),
        "mean_procedure_score": round(mean(float(row["procedure_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Al-jabr wa'l-muqabalah should be studied as rule-governed algebraic procedure: classification, restoration, balancing, representation, demonstration, practical use, and transmission.",
    }

    write_csv(TABLES / "algebraic_procedure_themes.csv", themes)
    write_csv(TABLES / "rule_governed_algebra_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "algebraic_procedure_summary.csv", [summary])

    write_json(JSON_DIR / "algebra_procedure_config.json", asdict(config))
    write_json(JSON_DIR / "rule_governed_algebra_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "algebraic_procedure_summary.json", summary)

    print("Al-jabr wa'l-muqabalah rule-governed algebra map complete.")
    print(TABLES / "algebraic_procedure_summary.csv")


if __name__ == "__main__":
    main()
