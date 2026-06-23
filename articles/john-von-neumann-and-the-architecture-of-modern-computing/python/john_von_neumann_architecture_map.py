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
class ArchitectureConfig:
    article: str = "john_von_neumann_and_the_architecture_of_modern_computing"
    core_threshold: float = 0.80
    high_architecture_threshold: float = 0.86


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


def architecture_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "stored_program_concept", "stored_program": 0.98, "memory_organization": 0.96, "control_structure": 0.94, "program_as_data": 0.98, "implementation_influence": 0.96, "bottleneck_awareness": 0.82, "collaboration_context": 0.86, "software_relevance": 0.98, "ai_infrastructure": 0.90, "governance_caution": 0.88},
        {"theme_id": "edvac_architectural_vocabulary", "stored_program": 0.96, "memory_organization": 0.94, "control_structure": 0.94, "program_as_data": 0.94, "implementation_influence": 0.96, "bottleneck_awareness": 0.80, "collaboration_context": 0.92, "software_relevance": 0.92, "ai_infrastructure": 0.84, "governance_caution": 0.88},
        {"theme_id": "memory_instructions_data", "stored_program": 0.98, "memory_organization": 0.98, "control_structure": 0.88, "program_as_data": 0.98, "implementation_influence": 0.94, "bottleneck_awareness": 0.92, "collaboration_context": 0.82, "software_relevance": 0.98, "ai_infrastructure": 0.94, "governance_caution": 0.92},
        {"theme_id": "control_arithmetic_io", "stored_program": 0.92, "memory_organization": 0.90, "control_structure": 0.98, "program_as_data": 0.88, "implementation_influence": 0.96, "bottleneck_awareness": 0.86, "collaboration_context": 0.82, "software_relevance": 0.94, "ai_infrastructure": 0.90, "governance_caution": 0.86},
        {"theme_id": "program_as_data", "stored_program": 0.96, "memory_organization": 0.96, "control_structure": 0.90, "program_as_data": 0.98, "implementation_influence": 0.94, "bottleneck_awareness": 0.84, "collaboration_context": 0.80, "software_relevance": 0.98, "ai_infrastructure": 0.92, "governance_caution": 0.96},
        {"theme_id": "von_neumann_bottleneck", "stored_program": 0.86, "memory_organization": 0.98, "control_structure": 0.88, "program_as_data": 0.84, "implementation_influence": 0.94, "bottleneck_awareness": 0.98, "collaboration_context": 0.76, "software_relevance": 0.94, "ai_infrastructure": 0.98, "governance_caution": 0.88},
        {"theme_id": "software_layer_legacy", "stored_program": 0.94, "memory_organization": 0.92, "control_structure": 0.94, "program_as_data": 0.98, "implementation_influence": 0.94, "bottleneck_awareness": 0.84, "collaboration_context": 0.80, "software_relevance": 0.98, "ai_infrastructure": 0.92, "governance_caution": 0.92},
        {"theme_id": "credit_and_collaboration", "stored_program": 0.86, "memory_organization": 0.82, "control_structure": 0.80, "program_as_data": 0.82, "implementation_influence": 0.90, "bottleneck_awareness": 0.76, "collaboration_context": 0.98, "software_relevance": 0.84, "ai_infrastructure": 0.80, "governance_caution": 0.96},
        {"theme_id": "ai_and_scientific_infrastructure", "stored_program": 0.88, "memory_organization": 0.94, "control_structure": 0.90, "program_as_data": 0.92, "implementation_influence": 0.94, "bottleneck_awareness": 0.96, "collaboration_context": 0.82, "software_relevance": 0.96, "ai_infrastructure": 0.98, "governance_caution": 0.96},
    ]


def score_theme(row: dict[str, object], config: ArchitectureConfig) -> dict[str, object]:
    architecture_score = mean([
        float(row["stored_program"]),
        float(row["memory_organization"]),
        float(row["control_structure"]),
        float(row["program_as_data"]),
        float(row["implementation_influence"]),
        float(row["bottleneck_awareness"]),
        float(row["collaboration_context"]),
        float(row["software_relevance"]),
        float(row["ai_infrastructure"]),
        float(row["governance_caution"]),
    ])

    if architecture_score >= config.core_threshold and float(row["stored_program"]) >= config.high_architecture_threshold:
        interpretive_status = "core_von_neumann_architecture_thread"
    elif architecture_score >= config.core_threshold:
        interpretive_status = "major_von_neumann_architecture_thread"
    else:
        interpretive_status = "supporting_von_neumann_architecture_thread"

    return {
        "theme_id": row["theme_id"],
        "stored_program": round(float(row["stored_program"]), 6),
        "memory_organization": round(float(row["memory_organization"]), 6),
        "control_structure": round(float(row["control_structure"]), 6),
        "program_as_data": round(float(row["program_as_data"]), 6),
        "implementation_influence": round(float(row["implementation_influence"]), 6),
        "bottleneck_awareness": round(float(row["bottleneck_awareness"]), 6),
        "collaboration_context": round(float(row["collaboration_context"]), 6),
        "software_relevance": round(float(row["software_relevance"]), 6),
        "ai_infrastructure": round(float(row["ai_infrastructure"]), 6),
        "governance_caution": round(float(row["governance_caution"]), 6),
        "architecture_score": round(architecture_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_tell_a_lone_inventor_story", "meaning": "Stored-program computing emerged through collaborative work and institutional networks."},
        {"caution": "do_not_confuse_architecture_with_implementation", "meaning": "Architecture describes organization; implementation realizes it materially."},
        {"caution": "do_not_ignore_the_bottleneck", "meaning": "Data movement and memory bandwidth shape performance."},
        {"caution": "do_not_treat_program_as_data_as_only_a_benefit", "meaning": "Program-as-data enables software power and security risk."},
        {"caution": "do_not_reduce_modern_computing_to_one_architecture", "meaning": "Modern systems extend, modify, and work around the von Neumann model."},
    ]


def main() -> None:
    config = ArchitectureConfig()
    themes = architecture_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_von_neumann_architecture_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_von_neumann_architecture_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_von_neumann_architecture_thread"),
        "mean_architecture_score": round(mean(float(row["architecture_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "von Neumann should be studied as an architectural synthesizer of stored-program computing, shared memory, control, software layers, bottlenecks, and institutional computing.",
    }

    write_csv(TABLES / "architecture_themes.csv", themes)
    write_csv(TABLES / "von_neumann_architecture_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "von_neumann_architecture_summary.csv", [summary])

    write_json(JSON_DIR / "architecture_config.json", asdict(config))
    write_json(JSON_DIR / "von_neumann_architecture_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "von_neumann_architecture_summary.json", summary)

    print("von Neumann architecture map complete.")
    print(TABLES / "von_neumann_architecture_summary.csv")


if __name__ == "__main__":
    main()
