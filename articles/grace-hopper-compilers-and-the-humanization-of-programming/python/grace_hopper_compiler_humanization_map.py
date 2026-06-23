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
class HopperConfig:
    article: str = "grace_hopper_compilers_and_the_humanization_of_programming"
    core_threshold: float = 0.80
    high_compiler_threshold: float = 0.86


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


def hopper_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "compiler_as_bridge", "compiler_centrality": 0.98, "human_readability": 0.96, "portability": 0.92, "documentation": 0.90, "standards": 0.88, "debugging": 0.86, "business_relevance": 0.88, "institutional_scale": 0.92, "abstraction": 0.98, "governance_caution": 0.90},
        {"theme_id": "automatic_programming", "compiler_centrality": 0.96, "human_readability": 0.90, "portability": 0.90, "documentation": 0.84, "standards": 0.82, "debugging": 0.82, "business_relevance": 0.84, "institutional_scale": 0.88, "abstraction": 0.96, "governance_caution": 0.86},
        {"theme_id": "a0_a2_subroutine_translation", "compiler_centrality": 0.94, "human_readability": 0.84, "portability": 0.86, "documentation": 0.84, "standards": 0.78, "debugging": 0.80, "business_relevance": 0.82, "institutional_scale": 0.86, "abstraction": 0.92, "governance_caution": 0.84},
        {"theme_id": "flow_matic_english_like_programming", "compiler_centrality": 0.94, "human_readability": 0.98, "portability": 0.88, "documentation": 0.88, "standards": 0.86, "debugging": 0.84, "business_relevance": 0.98, "institutional_scale": 0.94, "abstraction": 0.94, "governance_caution": 0.88},
        {"theme_id": "cobol_business_computation", "compiler_centrality": 0.90, "human_readability": 0.98, "portability": 0.94, "documentation": 0.92, "standards": 0.98, "debugging": 0.88, "business_relevance": 0.98, "institutional_scale": 0.98, "abstraction": 0.92, "governance_caution": 0.92},
        {"theme_id": "documentation_debugging_culture", "compiler_centrality": 0.82, "human_readability": 0.92, "portability": 0.82, "documentation": 0.98, "standards": 0.90, "debugging": 0.98, "business_relevance": 0.86, "institutional_scale": 0.92, "abstraction": 0.86, "governance_caution": 0.92},
        {"theme_id": "standards_validation_institutional_computing", "compiler_centrality": 0.88, "human_readability": 0.88, "portability": 0.98, "documentation": 0.94, "standards": 0.98, "debugging": 0.90, "business_relevance": 0.94, "institutional_scale": 0.98, "abstraction": 0.90, "governance_caution": 0.98},
        {"theme_id": "ai_code_generation_caution", "compiler_centrality": 0.82, "human_readability": 0.94, "portability": 0.86, "documentation": 0.92, "standards": 0.88, "debugging": 0.94, "business_relevance": 0.88, "institutional_scale": 0.94, "abstraction": 0.96, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: HopperConfig) -> dict[str, object]:
    humanization_score = mean([
        float(row["compiler_centrality"]),
        float(row["human_readability"]),
        float(row["portability"]),
        float(row["documentation"]),
        float(row["standards"]),
        float(row["debugging"]),
        float(row["business_relevance"]),
        float(row["institutional_scale"]),
        float(row["abstraction"]),
        float(row["governance_caution"]),
    ])

    if humanization_score >= config.core_threshold and float(row["compiler_centrality"]) >= config.high_compiler_threshold:
        interpretive_status = "core_hopper_compiler_humanization_thread"
    elif humanization_score >= config.core_threshold:
        interpretive_status = "major_hopper_compiler_humanization_thread"
    else:
        interpretive_status = "supporting_hopper_compiler_humanization_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "compiler_centrality", "human_readability", "portability", "documentation",
        "standards", "debugging", "business_relevance", "institutional_scale",
        "abstraction", "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "humanization_score": round(humanization_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_humanization_as_lack_of_rigor", "meaning": "Human-facing programming still requires formal syntax, semantics, testing, and validation."},
        {"caution": "do_not_tell_a_single_inventor_story", "meaning": "COBOL and programming languages emerged through teams, standards committees, vendors, and institutions."},
        {"caution": "do_not_confuse_compilers_with_ai_code_generation", "meaning": "Compilers translate formal languages; AI coding tools generate statistically likely code that still requires review."},
        {"caution": "do_not_ignore_maintenance", "meaning": "Human-readable languages matter because code persists over decades."},
        {"caution": "do_not_hide_machine_constraints", "meaning": "Abstraction mediates hardware constraints; it does not abolish them."},
    ]


def main() -> None:
    config = HopperConfig()
    themes = hopper_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_hopper_compiler_humanization_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_hopper_compiler_humanization_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_hopper_compiler_humanization_thread"),
        "mean_humanization_score": round(mean(float(row["humanization_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Hopper should be studied as a pioneer of compiler-mediated programming, human-readable source language, machine independence, standards, documentation, and accountable automation.",
    }

    write_csv(TABLES / "hopper_themes.csv", themes)
    write_csv(TABLES / "hopper_compiler_humanization_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "hopper_compiler_humanization_summary.csv", [summary])

    write_json(JSON_DIR / "hopper_config.json", asdict(config))
    write_json(JSON_DIR / "hopper_compiler_humanization_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "hopper_compiler_humanization_summary.json", summary)

    print("Hopper compiler humanization map complete.")
    print(TABLES / "hopper_compiler_humanization_summary.csv")


if __name__ == "__main__":
    main()
