from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import math
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class BackusConfig:
    article: str = "john_backus_fortran_and_the_birth_of_high_level_scientific_programming"
    core_threshold: float = 0.80
    high_language_threshold: float = 0.86


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


def formula_translation_example(x: float, a: float, b: float, c: float) -> float:
    return a * x * x + b * x + c


def vector_formula_example(values: list[float]) -> list[float]:
    return [math.sin(x) + x * x for x in values]


def backus_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "formula_translation", "high_level_language": 0.98, "scientific_expression": 0.98, "compiler_optimization": 0.94, "numerical_relevance": 0.96, "portability": 0.90, "performance_credibility": 0.96, "language_history": 0.94, "formal_specification": 0.84, "maintainability": 0.90, "governance_caution": 0.88},
        {"theme_id": "ibm_704_fortran_compiler", "high_level_language": 0.96, "scientific_expression": 0.94, "compiler_optimization": 0.98, "numerical_relevance": 0.94, "portability": 0.86, "performance_credibility": 0.98, "language_history": 0.96, "formal_specification": 0.82, "maintainability": 0.88, "governance_caution": 0.88},
        {"theme_id": "scientists_engineers_domain_expression", "high_level_language": 0.96, "scientific_expression": 0.98, "compiler_optimization": 0.88, "numerical_relevance": 0.98, "portability": 0.88, "performance_credibility": 0.92, "language_history": 0.90, "formal_specification": 0.80, "maintainability": 0.92, "governance_caution": 0.88},
        {"theme_id": "arrays_loops_numerical_work", "high_level_language": 0.94, "scientific_expression": 0.96, "compiler_optimization": 0.92, "numerical_relevance": 0.98, "portability": 0.88, "performance_credibility": 0.94, "language_history": 0.88, "formal_specification": 0.82, "maintainability": 0.90, "governance_caution": 0.88},
        {"theme_id": "machine_independence_portability", "high_level_language": 0.94, "scientific_expression": 0.90, "compiler_optimization": 0.90, "numerical_relevance": 0.92, "portability": 0.98, "performance_credibility": 0.90, "language_history": 0.94, "formal_specification": 0.86, "maintainability": 0.96, "governance_caution": 0.92},
        {"theme_id": "fortran_scientific_computing_hpc", "high_level_language": 0.92, "scientific_expression": 0.98, "compiler_optimization": 0.96, "numerical_relevance": 0.98, "portability": 0.94, "performance_credibility": 0.98, "language_history": 0.94, "formal_specification": 0.86, "maintainability": 0.96, "governance_caution": 0.92},
        {"theme_id": "backus_naur_form", "high_level_language": 0.88, "scientific_expression": 0.78, "compiler_optimization": 0.80, "numerical_relevance": 0.74, "portability": 0.86, "performance_credibility": 0.76, "language_history": 0.98, "formal_specification": 0.98, "maintainability": 0.88, "governance_caution": 0.90},
        {"theme_id": "functional_programming_later_backus", "high_level_language": 0.88, "scientific_expression": 0.82, "compiler_optimization": 0.82, "numerical_relevance": 0.78, "portability": 0.84, "performance_credibility": 0.78, "language_history": 0.96, "formal_specification": 0.94, "maintainability": 0.88, "governance_caution": 0.92},
        {"theme_id": "ai_code_generation_fortran_lesson", "high_level_language": 0.90, "scientific_expression": 0.92, "compiler_optimization": 0.90, "numerical_relevance": 0.90, "portability": 0.88, "performance_credibility": 0.94, "language_history": 0.88, "formal_specification": 0.88, "maintainability": 0.96, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: BackusConfig) -> dict[str, object]:
    birth_score = mean([
        float(row["high_level_language"]),
        float(row["scientific_expression"]),
        float(row["compiler_optimization"]),
        float(row["numerical_relevance"]),
        float(row["portability"]),
        float(row["performance_credibility"]),
        float(row["language_history"]),
        float(row["formal_specification"]),
        float(row["maintainability"]),
        float(row["governance_caution"]),
    ])

    if birth_score >= config.core_threshold and float(row["high_level_language"]) >= config.high_language_threshold:
        interpretive_status = "core_backus_fortran_scientific_programming_thread"
    elif birth_score >= config.core_threshold:
        interpretive_status = "major_backus_fortran_scientific_programming_thread"
    else:
        interpretive_status = "supporting_backus_fortran_scientific_programming_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "high_level_language", "scientific_expression", "compiler_optimization",
        "numerical_relevance", "portability", "performance_credibility",
        "language_history", "formal_specification", "maintainability", "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "birth_score": round(birth_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_reduce_fortran_to_old_syntax", "meaning": "Fortran matters because it made high-level scientific programming practical and performant."},
        {"caution": "do_not_tell_a_lone_inventor_story", "meaning": "Backus led a team; FORTRAN was a collaborative language and compiler achievement."},
        {"caution": "do_not_ignore_optimization", "meaning": "FORTRAN succeeded because the compiler made abstraction credible through performance."},
        {"caution": "do_not_confuse_high_level_with_low_rigor", "meaning": "High-level scientific programming still requires numerical analysis, tests, and performance review."},
        {"caution": "do_not_trust_generated_code_without_translation_review", "meaning": "AI-generated code must be checked for correctness, performance, assumptions, and maintainability."},
    ]


def main() -> None:
    config = BackusConfig()
    themes = backus_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    formula_rows = [
        {"x": x, "a": 2.0, "b": -3.0, "c": 1.0, "y": round(formula_translation_example(x, 2.0, -3.0, 1.0), 6)}
        for x in [-2, -1, 0, 1, 2, 3]
    ]
    vector_rows = [
        {"index": i + 1, "x": x, "sin_x_plus_x_squared": round(y, 6)}
        for i, (x, y) in enumerate(zip([0.0, 0.5, 1.0, 1.5, 2.0], vector_formula_example([0.0, 0.5, 1.0, 1.5, 2.0])))
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_backus_fortran_scientific_programming_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_backus_fortran_scientific_programming_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_backus_fortran_scientific_programming_thread"),
        "mean_birth_score": round(mean(float(row["birth_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Backus and FORTRAN should be studied as the practical birth of high-level scientific programming: formula translation, compiler optimization, numerical expression, and performance-oriented abstraction.",
    }

    write_csv(TABLES / "backus_themes.csv", themes)
    write_csv(TABLES / "backus_fortran_scientific_programming_map.csv", scored)
    write_csv(TABLES / "formula_translation_example.csv", formula_rows)
    write_csv(TABLES / "vector_formula_example.csv", vector_rows)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "backus_fortran_scientific_programming_summary.csv", [summary])

    write_json(JSON_DIR / "backus_config.json", asdict(config))
    write_json(JSON_DIR / "backus_fortran_scientific_programming_map.json", scored)
    write_json(JSON_DIR / "formula_translation_example.json", formula_rows)
    write_json(JSON_DIR / "vector_formula_example.json", vector_rows)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "backus_fortran_scientific_programming_summary.json", summary)

    print("Backus Fortran scientific programming map complete.")
    print(TABLES / "backus_fortran_scientific_programming_summary.csv")


if __name__ == "__main__":
    main()
