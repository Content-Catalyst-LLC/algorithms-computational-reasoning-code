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
class UnknownVariableConfig:
    article: str = "the_unknown_the_variable_and_islamic_mathematical_philosophy"
    core_threshold: float = 0.80
    high_unknown_threshold: float = 0.86


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


def unknown_variable_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "unknown_as_named_object", "unknown_representation": 0.98, "procedural_transformation": 0.94, "abstraction": 0.96, "proof_relation": 0.88, "translation_continuity": 0.90, "practical_grounding": 0.92, "philosophical_depth": 0.96, "historical_significance": 0.98, "ethical_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "shay_root_square_number", "unknown_representation": 0.98, "procedural_transformation": 0.96, "abstraction": 0.94, "proof_relation": 0.90, "translation_continuity": 0.94, "practical_grounding": 0.90, "philosophical_depth": 0.94, "historical_significance": 0.98, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "case_classification_and_rule", "unknown_representation": 0.92, "procedural_transformation": 0.98, "abstraction": 0.92, "proof_relation": 0.90, "translation_continuity": 0.88, "practical_grounding": 0.92, "philosophical_depth": 0.90, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "geometric_demonstration", "unknown_representation": 0.90, "procedural_transformation": 0.92, "abstraction": 0.94, "proof_relation": 0.98, "translation_continuity": 0.86, "practical_grounding": 0.88, "philosophical_depth": 0.96, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "from_unknown_to_variable", "unknown_representation": 0.96, "procedural_transformation": 0.94, "abstraction": 0.98, "proof_relation": 0.88, "translation_continuity": 0.94, "practical_grounding": 0.86, "philosophical_depth": 0.96, "historical_significance": 0.98, "ethical_caution": 0.88, "modern_resonance": 0.98},
        {"theme_id": "res_cosa_symbolic_transition", "unknown_representation": 0.94, "procedural_transformation": 0.90, "abstraction": 0.94, "proof_relation": 0.84, "translation_continuity": 0.98, "practical_grounding": 0.86, "philosophical_depth": 0.90, "historical_significance": 0.94, "ethical_caution": 0.86, "modern_resonance": 0.96},
        {"theme_id": "origin_story_caution", "unknown_representation": 0.86, "procedural_transformation": 0.86, "abstraction": 0.90, "proof_relation": 0.86, "translation_continuity": 0.92, "practical_grounding": 0.84, "philosophical_depth": 0.94, "historical_significance": 0.94, "ethical_caution": 0.98, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: UnknownVariableConfig) -> dict[str, object]:
    unknown_variable_score = mean([
        float(row["unknown_representation"]),
        float(row["procedural_transformation"]),
        float(row["abstraction"]),
        float(row["proof_relation"]),
        float(row["translation_continuity"]),
        float(row["practical_grounding"]),
        float(row["philosophical_depth"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if unknown_variable_score >= config.core_threshold and float(row["unknown_representation"]) >= config.high_unknown_threshold:
        interpretive_status = "core_unknown_variable_philosophy_thread"
    elif unknown_variable_score >= config.core_threshold:
        interpretive_status = "major_unknown_variable_philosophy_thread"
    else:
        interpretive_status = "supporting_unknown_variable_philosophy_thread"

    return {
        "theme_id": row["theme_id"],
        "unknown_representation": round(float(row["unknown_representation"]), 6),
        "procedural_transformation": round(float(row["procedural_transformation"]), 6),
        "abstraction": round(float(row["abstraction"]), 6),
        "proof_relation": round(float(row["proof_relation"]), 6),
        "translation_continuity": round(float(row["translation_continuity"]), 6),
        "practical_grounding": round(float(row["practical_grounding"]), 6),
        "philosophical_depth": round(float(row["philosophical_depth"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "unknown_variable_score": round(unknown_variable_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_project_modern_symbolism_backward", "meaning": "Verbal algebra can be abstract and rigorous without modern notation."},
        {"caution": "do_not_equate_unknown_and_variable_too_quickly", "meaning": "An unknown is usually problem-specific; a variable is a broader formal object."},
        {"caution": "do_not_treat_practical_problems_as_non_philosophical", "meaning": "Inheritance, trade, and measurement can raise deep questions about quantity and method."},
        {"caution": "do_not_reduce_algebra_to_etymology", "meaning": "Terms such as al-jabr, res, and cosa matter, but procedure and proof matter too."},
        {"caution": "do_not_create_single_origin_myths", "meaning": "The variable has a layered history across Greek, Indian, Arabic, Latin, vernacular, and symbolic traditions."},
    ]


def main() -> None:
    config = UnknownVariableConfig()
    themes = unknown_variable_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_unknown_variable_philosophy_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_unknown_variable_philosophy_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_unknown_variable_philosophy_thread"),
        "mean_unknown_variable_score": round(mean(float(row["unknown_variable_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "The unknown should be studied as a disciplined mathematical object: named, classified, transformed, demonstrated, translated, verified, and gradually generalized toward variable thinking.",
    }

    write_csv(TABLES / "unknown_variable_themes.csv", themes)
    write_csv(TABLES / "unknown_variable_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "unknown_variable_summary.csv", [summary])

    write_json(JSON_DIR / "unknown_variable_config.json", asdict(config))
    write_json(JSON_DIR / "unknown_variable_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "unknown_variable_summary.json", summary)

    print("Unknown, variable, and Islamic mathematical philosophy map complete.")
    print(TABLES / "unknown_variable_summary.csv")


if __name__ == "__main__":
    main()
