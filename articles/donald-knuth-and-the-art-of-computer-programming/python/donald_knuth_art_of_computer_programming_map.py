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
class KnuthConfig:
    article: str = "donald_knuth_and_the_art_of_computer_programming"
    core_threshold: float = 0.80
    high_analysis_threshold: float = 0.86


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


def comparison_sort_lower_bound(n: int) -> float:
    if n <= 1:
        return 0.0
    return math.log2(math.factorial(n))


def growth_table() -> list[dict[str, object]]:
    rows = []
    for n in [10, 100, 1000, 10000]:
        rows.append({
            "n": n,
            "log2_n": round(math.log2(n), 6),
            "n": n,
            "n_log2_n": round(n * math.log2(n), 6),
            "n_squared": n * n,
        })
    return rows


def knuth_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "art_of_computer_programming", "algorithm_analysis": 0.98, "exposition": 0.98, "mathematical_rigor": 0.98, "historical_depth": 0.94, "implementation_relevance": 0.94, "typography_relevance": 0.88, "literate_programming": 0.90, "pedagogy": 0.98, "maintainability": 0.92, "governance_caution": 0.90},
        {"theme_id": "analysis_of_algorithms", "algorithm_analysis": 0.98, "exposition": 0.92, "mathematical_rigor": 0.98, "historical_depth": 0.88, "implementation_relevance": 0.94, "typography_relevance": 0.78, "literate_programming": 0.82, "pedagogy": 0.94, "maintainability": 0.88, "governance_caution": 0.90},
        {"theme_id": "asymptotic_thinking", "algorithm_analysis": 0.96, "exposition": 0.90, "mathematical_rigor": 0.96, "historical_depth": 0.84, "implementation_relevance": 0.92, "typography_relevance": 0.76, "literate_programming": 0.80, "pedagogy": 0.92, "maintainability": 0.86, "governance_caution": 0.88},
        {"theme_id": "sorting_searching_data_structures", "algorithm_analysis": 0.96, "exposition": 0.94, "mathematical_rigor": 0.94, "historical_depth": 0.92, "implementation_relevance": 0.98, "typography_relevance": 0.80, "literate_programming": 0.82, "pedagogy": 0.96, "maintainability": 0.90, "governance_caution": 0.88},
        {"theme_id": "mix_mmix_machine_models", "algorithm_analysis": 0.92, "exposition": 0.90, "mathematical_rigor": 0.90, "historical_depth": 0.90, "implementation_relevance": 0.98, "typography_relevance": 0.82, "literate_programming": 0.84, "pedagogy": 0.94, "maintainability": 0.88, "governance_caution": 0.86},
        {"theme_id": "tex_metafont_typography", "algorithm_analysis": 0.82, "exposition": 0.98, "mathematical_rigor": 0.92, "historical_depth": 0.92, "implementation_relevance": 0.92, "typography_relevance": 0.98, "literate_programming": 0.90, "pedagogy": 0.92, "maintainability": 0.94, "governance_caution": 0.88},
        {"theme_id": "literate_programming_web_cweb", "algorithm_analysis": 0.88, "exposition": 0.98, "mathematical_rigor": 0.90, "historical_depth": 0.90, "implementation_relevance": 0.96, "typography_relevance": 0.94, "literate_programming": 0.98, "pedagogy": 0.96, "maintainability": 0.98, "governance_caution": 0.94},
        {"theme_id": "ai_code_generation_review", "algorithm_analysis": 0.90, "exposition": 0.96, "mathematical_rigor": 0.94, "historical_depth": 0.84, "implementation_relevance": 0.96, "typography_relevance": 0.82, "literate_programming": 0.94, "pedagogy": 0.92, "maintainability": 0.98, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: KnuthConfig) -> dict[str, object]:
    art_score = mean([
        float(row["algorithm_analysis"]),
        float(row["exposition"]),
        float(row["mathematical_rigor"]),
        float(row["historical_depth"]),
        float(row["implementation_relevance"]),
        float(row["typography_relevance"]),
        float(row["literate_programming"]),
        float(row["pedagogy"]),
        float(row["maintainability"]),
        float(row["governance_caution"]),
    ])

    if art_score >= config.core_threshold and float(row["algorithm_analysis"]) >= config.high_analysis_threshold:
        interpretive_status = "core_knuth_algorithmic_art_thread"
    elif art_score >= config.core_threshold:
        interpretive_status = "major_knuth_algorithmic_art_thread"
    else:
        interpretive_status = "supporting_knuth_algorithmic_art_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "algorithm_analysis", "exposition", "mathematical_rigor", "historical_depth",
        "implementation_relevance", "typography_relevance", "literate_programming",
        "pedagogy", "maintainability", "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "art_score": round(art_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_art_as_anti_rigor", "meaning": "Knuth's art combines beauty, style, mathematical proof, implementation detail, and analysis."},
        {"caution": "do_not_reduce_knuth_to_taocp_only", "meaning": "TAOCP is central, but TeX, METAFONT, literate programming, and digital typography are also part of the legacy."},
        {"caution": "do_not_confuse_code_generation_with_understanding", "meaning": "Generated code still needs explanation, analysis, tests, and review."},
        {"caution": "do_not_ignore_machine_models", "meaning": "Algorithm analysis depends on assumptions about operations and representation."},
        {"caution": "do_not_skip_exposition", "meaning": "Readable explanation is part of computational responsibility."},
    ]


def main() -> None:
    config = KnuthConfig()
    themes = knuth_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    lower_bounds = [
        {"n": n, "comparison_sort_lower_bound_log2_factorial": round(comparison_sort_lower_bound(n), 6)}
        for n in [2, 3, 4, 8, 16, 32]
    ]

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_knuth_algorithmic_art_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_knuth_algorithmic_art_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_knuth_algorithmic_art_thread"),
        "mean_art_score": round(mean(float(row["art_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Knuth should be studied as a theorist of algorithmic analysis, rigorous exposition, literate programming, typography, and computational craft.",
    }

    write_csv(TABLES / "knuth_themes.csv", themes)
    write_csv(TABLES / "knuth_algorithmic_art_map.csv", scored)
    write_csv(TABLES / "growth_table.csv", growth_table())
    write_csv(TABLES / "comparison_sort_lower_bounds.csv", lower_bounds)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "knuth_algorithmic_art_summary.csv", [summary])

    write_json(JSON_DIR / "knuth_config.json", asdict(config))
    write_json(JSON_DIR / "knuth_algorithmic_art_map.json", scored)
    write_json(JSON_DIR / "growth_table.json", growth_table())
    write_json(JSON_DIR / "comparison_sort_lower_bounds.json", lower_bounds)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "knuth_algorithmic_art_summary.json", summary)

    print("Knuth algorithmic art map complete.")
    print(TABLES / "knuth_algorithmic_art_summary.csv")


if __name__ == "__main__":
    main()
