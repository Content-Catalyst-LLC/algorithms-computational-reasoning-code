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
class OriginStoryConfig:
    article: str = "why_origin_stories_of_algorithms_need_care"
    core_threshold: float = 0.80
    high_caution_threshold: float = 0.86


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


def origin_story_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "word_history_not_concept_history", "evidence_grounding": 0.96, "scope_clarity": 0.98, "anachronism_control": 0.96, "network_awareness": 0.88, "etymology_caution": 0.98, "transmission_depth": 0.90, "credit_distribution": 0.90, "public_usefulness": 0.96, "historical_significance": 0.98, "modern_resonance": 0.98},
        {"theme_id": "al_khwarizmi_without_myth", "evidence_grounding": 0.98, "scope_clarity": 0.96, "anachronism_control": 0.96, "network_awareness": 0.92, "etymology_caution": 0.96, "transmission_depth": 0.94, "credit_distribution": 0.94, "public_usefulness": 0.98, "historical_significance": 0.98, "modern_resonance": 0.96},
        {"theme_id": "procedures_before_algorithm_word", "evidence_grounding": 0.94, "scope_clarity": 0.96, "anachronism_control": 0.98, "network_awareness": 0.96, "etymology_caution": 0.92, "transmission_depth": 0.92, "credit_distribution": 0.96, "public_usefulness": 0.94, "historical_significance": 0.96, "modern_resonance": 0.96},
        {"theme_id": "translation_reception_institutional_memory", "evidence_grounding": 0.94, "scope_clarity": 0.92, "anachronism_control": 0.90, "network_awareness": 0.98, "etymology_caution": 0.88, "transmission_depth": 0.98, "credit_distribution": 0.98, "public_usefulness": 0.94, "historical_significance": 0.96, "modern_resonance": 0.96},
        {"theme_id": "great_man_vs_network_history", "evidence_grounding": 0.92, "scope_clarity": 0.94, "anachronism_control": 0.92, "network_awareness": 0.98, "etymology_caution": 0.90, "transmission_depth": 0.94, "credit_distribution": 0.98, "public_usefulness": 0.96, "historical_significance": 0.94, "modern_resonance": 0.98},
        {"theme_id": "civilizational_erasure_token_inclusion", "evidence_grounding": 0.92, "scope_clarity": 0.94, "anachronism_control": 0.92, "network_awareness": 0.96, "etymology_caution": 0.88, "transmission_depth": 0.94, "credit_distribution": 0.98, "public_usefulness": 0.94, "historical_significance": 0.96, "modern_resonance": 0.98},
        {"theme_id": "ai_age_origin_story_caution", "evidence_grounding": 0.88, "scope_clarity": 0.96, "anachronism_control": 0.98, "network_awareness": 0.94, "etymology_caution": 0.90, "transmission_depth": 0.88, "credit_distribution": 0.92, "public_usefulness": 0.98, "historical_significance": 0.94, "modern_resonance": 0.98},
    ]


def score_theme(row: dict[str, object], config: OriginStoryConfig) -> dict[str, object]:
    origin_care_score = mean([
        float(row["evidence_grounding"]),
        float(row["scope_clarity"]),
        float(row["anachronism_control"]),
        float(row["network_awareness"]),
        float(row["etymology_caution"]),
        float(row["transmission_depth"]),
        float(row["credit_distribution"]),
        float(row["public_usefulness"]),
        float(row["historical_significance"]),
        float(row["modern_resonance"]),
    ])

    if origin_care_score >= config.core_threshold and float(row["anachronism_control"]) >= config.high_caution_threshold:
        interpretive_status = "core_origin_story_care_thread"
    elif origin_care_score >= config.core_threshold:
        interpretive_status = "major_origin_story_care_thread"
    else:
        interpretive_status = "supporting_origin_story_care_thread"

    return {
        "theme_id": row["theme_id"],
        "evidence_grounding": round(float(row["evidence_grounding"]), 6),
        "scope_clarity": round(float(row["scope_clarity"]), 6),
        "anachronism_control": round(float(row["anachronism_control"]), 6),
        "network_awareness": round(float(row["network_awareness"]), 6),
        "etymology_caution": round(float(row["etymology_caution"]), 6),
        "transmission_depth": round(float(row["transmission_depth"]), 6),
        "credit_distribution": round(float(row["credit_distribution"]), 6),
        "public_usefulness": round(float(row["public_usefulness"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "origin_care_score": round(origin_care_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_word_origin_with_invention", "meaning": "The word algorithm has an etymological history, but the concept and practices are broader."},
        {"caution": "do_not_turn_al_khwarizmi_into_a_myth", "meaning": "Honor his role without claiming he invented every algorithm or modern computer science."},
        {"caution": "do_not_project_modern_computing_backward", "meaning": "Historical procedures can be algorithm-like without being programs or modern formal algorithms."},
        {"caution": "do_not_erase_transmission_networks", "meaning": "Translators, scribes, teachers, readers, and institutions make methods durable."},
        {"caution": "do_not_replace_erasure_with_tokenism", "meaning": "Inclusion requires context, method, transmission, and evidence, not just name-dropping."},
    ]


def main() -> None:
    config = OriginStoryConfig()
    themes = origin_story_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_origin_story_care_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_origin_story_care_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_origin_story_care_thread"),
        "mean_origin_care_score": round(mean(float(row["origin_care_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Algorithm origin stories need care because word histories, concept histories, procedure histories, transmission histories, and modern formalization do not all begin at the same point.",
    }

    write_csv(TABLES / "origin_story_themes.csv", themes)
    write_csv(TABLES / "origin_story_care_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "origin_story_summary.csv", [summary])

    write_json(JSON_DIR / "origin_story_config.json", asdict(config))
    write_json(JSON_DIR / "origin_story_care_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "origin_story_summary.json", summary)

    print("Algorithm origin story caution map complete.")
    print(TABLES / "origin_story_summary.csv")


if __name__ == "__main__":
    main()
