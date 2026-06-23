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
class LovelaceConfig:
    article: str = "ada_lovelace_programming_and_the_imagination_of_computation"
    core_threshold: float = 0.80
    high_programming_threshold: float = 0.86


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


def lovelace_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "note_g_bernoulli_procedure", "programming_structure": 0.98, "symbolic_generality": 0.86, "machine_orientation": 0.98, "mathematical_grounding": 0.94, "imaginative_reach": 0.86, "limit_awareness": 0.76, "collaboration": 0.92, "authorship": 0.90, "modern_resonance": 0.98, "ai_caution": 0.82},
        {"theme_id": "analytical_engine_general_machine", "programming_structure": 0.92, "symbolic_generality": 0.96, "machine_orientation": 0.98, "mathematical_grounding": 0.90, "imaginative_reach": 0.94, "limit_awareness": 0.84, "collaboration": 0.92, "authorship": 0.86, "modern_resonance": 0.98, "ai_caution": 0.86},
        {"theme_id": "computation_beyond_arithmetic", "programming_structure": 0.86, "symbolic_generality": 0.98, "machine_orientation": 0.92, "mathematical_grounding": 0.88, "imaginative_reach": 0.98, "limit_awareness": 0.86, "collaboration": 0.86, "authorship": 0.94, "modern_resonance": 0.98, "ai_caution": 0.90},
        {"theme_id": "music_pattern_symbolic_generality", "programming_structure": 0.78, "symbolic_generality": 0.98, "machine_orientation": 0.88, "mathematical_grounding": 0.82, "imaginative_reach": 0.98, "limit_awareness": 0.82, "collaboration": 0.78, "authorship": 0.94, "modern_resonance": 0.96, "ai_caution": 0.86},
        {"theme_id": "lovelace_objection_machine_limits", "programming_structure": 0.78, "symbolic_generality": 0.88, "machine_orientation": 0.92, "mathematical_grounding": 0.82, "imaginative_reach": 0.90, "limit_awareness": 0.98, "collaboration": 0.80, "authorship": 0.94, "modern_resonance": 0.98, "ai_caution": 0.98},
        {"theme_id": "translation_notes_authorship", "programming_structure": 0.84, "symbolic_generality": 0.90, "machine_orientation": 0.88, "mathematical_grounding": 0.86, "imaginative_reach": 0.94, "limit_awareness": 0.86, "collaboration": 0.98, "authorship": 0.98, "modern_resonance": 0.94, "ai_caution": 0.84},
        {"theme_id": "gender_credit_recognition", "programming_structure": 0.76, "symbolic_generality": 0.82, "machine_orientation": 0.78, "mathematical_grounding": 0.78, "imaginative_reach": 0.90, "limit_awareness": 0.88, "collaboration": 0.96, "authorship": 0.98, "modern_resonance": 0.96, "ai_caution": 0.86},
    ]


def score_theme(row: dict[str, object], config: LovelaceConfig) -> dict[str, object]:
    imagination_score = mean([
        float(row["programming_structure"]),
        float(row["symbolic_generality"]),
        float(row["machine_orientation"]),
        float(row["mathematical_grounding"]),
        float(row["imaginative_reach"]),
        float(row["limit_awareness"]),
        float(row["collaboration"]),
        float(row["authorship"]),
        float(row["modern_resonance"]),
        float(row["ai_caution"]),
    ])

    if imagination_score >= config.core_threshold and float(row["programming_structure"]) >= config.high_programming_threshold:
        interpretive_status = "core_lovelace_computation_thread"
    elif imagination_score >= config.core_threshold:
        interpretive_status = "major_lovelace_computation_thread"
    else:
        interpretive_status = "supporting_lovelace_computation_thread"

    return {
        "theme_id": row["theme_id"],
        "programming_structure": round(float(row["programming_structure"]), 6),
        "symbolic_generality": round(float(row["symbolic_generality"]), 6),
        "machine_orientation": round(float(row["machine_orientation"]), 6),
        "mathematical_grounding": round(float(row["mathematical_grounding"]), 6),
        "imaginative_reach": round(float(row["imaginative_reach"]), 6),
        "limit_awareness": round(float(row["limit_awareness"]), 6),
        "collaboration": round(float(row["collaboration"]), 6),
        "authorship": round(float(row["authorship"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "ai_caution": round(float(row["ai_caution"]), 6),
        "imagination_score": round(imagination_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_reduce_lovelace_to_a_slogan", "meaning": "The phrase first programmer is useful only when Note G, collaboration, and definition are explained."},
        {"caution": "do_not_dismiss_translation_as_passive", "meaning": "Translation, annotation, interpretation, and expansion are intellectual work."},
        {"caution": "do_not_project_modern_software_backward", "meaning": "Lovelace wrote machine-oriented procedure, not modern source code."},
        {"caution": "do_not_ignore_babbage", "meaning": "Babbage's machine design and collaboration are central to the story."},
        {"caution": "do_not_overstate_machine_agency", "meaning": "Lovelace's machine-limit reflections remain important for AI-era claims."},
    ]


def main() -> None:
    config = LovelaceConfig()
    themes = lovelace_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_lovelace_computation_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_lovelace_computation_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_lovelace_computation_thread"),
        "mean_imagination_score": round(mean(float(row["imagination_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Lovelace should be studied as a bridge between mechanical procedure and software imagination: programming structure, symbolic generality, machine orientation, and machine limits.",
    }

    write_csv(TABLES / "lovelace_themes.csv", themes)
    write_csv(TABLES / "lovelace_computation_imagination_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "lovelace_imagination_summary.csv", [summary])

    write_json(JSON_DIR / "lovelace_config.json", asdict(config))
    write_json(JSON_DIR / "lovelace_computation_imagination_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "lovelace_imagination_summary.json", summary)

    print("Lovelace computation imagination map complete.")
    print(TABLES / "lovelace_imagination_summary.csv")


if __name__ == "__main__":
    main()
