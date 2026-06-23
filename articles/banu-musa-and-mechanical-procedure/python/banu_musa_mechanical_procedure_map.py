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
class MechanicalProcedureConfig:
    article: str = "banu_musa_and_mechanical_procedure"
    core_threshold: float = 0.80
    high_control_threshold: float = 0.86


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


def mechanical_procedure_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "hydraulic_material_logic", "mechanical_structure": 0.96, "procedural_sequence": 0.90, "conditional_control": 0.88, "hidden_state": 0.90, "feedback_potential": 0.84, "historical_significance": 0.94, "ethical_caution": 0.82, "modern_resonance": 0.94},
        {"theme_id": "pneumatic_pressure_control", "mechanical_structure": 0.94, "procedural_sequence": 0.88, "conditional_control": 0.90, "hidden_state": 0.92, "feedback_potential": 0.84, "historical_significance": 0.92, "ethical_caution": 0.82, "modern_resonance": 0.92},
        {"theme_id": "valves_floats_thresholds", "mechanical_structure": 0.96, "procedural_sequence": 0.92, "conditional_control": 0.98, "hidden_state": 0.88, "feedback_potential": 0.92, "historical_significance": 0.94, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "sequencing_and_timing", "mechanical_structure": 0.92, "procedural_sequence": 0.98, "conditional_control": 0.92, "hidden_state": 0.90, "feedback_potential": 0.86, "historical_significance": 0.92, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "trick_vessels_interface_mechanism", "mechanical_structure": 0.90, "procedural_sequence": 0.90, "conditional_control": 0.92, "hidden_state": 0.96, "feedback_potential": 0.82, "historical_significance": 0.90, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "fountains_and_alternating_behavior", "mechanical_structure": 0.94, "procedural_sequence": 0.94, "conditional_control": 0.90, "hidden_state": 0.88, "feedback_potential": 0.88, "historical_significance": 0.92, "ethical_caution": 0.82, "modern_resonance": 0.94},
        {"theme_id": "diagrams_and_reproducibility", "mechanical_structure": 0.88, "procedural_sequence": 0.92, "conditional_control": 0.86, "hidden_state": 0.86, "feedback_potential": 0.80, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: MechanicalProcedureConfig) -> dict[str, object]:
    mechanical_score = mean([
        float(row["mechanical_structure"]),
        float(row["procedural_sequence"]),
        float(row["conditional_control"]),
        float(row["hidden_state"]),
        float(row["feedback_potential"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if mechanical_score >= config.core_threshold and float(row["conditional_control"]) >= config.high_control_threshold:
        interpretive_status = "core_mechanical_procedure_thread"
    elif mechanical_score >= config.core_threshold:
        interpretive_status = "major_mechanical_procedure_thread"
    else:
        interpretive_status = "supporting_mechanical_procedure_thread"

    return {
        "theme_id": row["theme_id"],
        "mechanical_structure": round(float(row["mechanical_structure"]), 6),
        "procedural_sequence": round(float(row["procedural_sequence"]), 6),
        "conditional_control": round(float(row["conditional_control"]), 6),
        "hidden_state": round(float(row["hidden_state"]), 6),
        "feedback_potential": round(float(row["feedback_potential"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "mechanical_score": round(mechanical_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_call_the_devices_modern_robots", "meaning": "The devices show automatic behavior and mechanical procedure, not modern robotics or AI."},
        {"caution": "do_not_dismiss_trick_devices_as_toys", "meaning": "Courtly or surprising devices can still demonstrate serious hydraulic and pneumatic reasoning."},
        {"caution": "do_not_treat_mechanics_as_non_computational", "meaning": "Mechanical systems can embody rule-governed state transitions and conditional behavior."},
        {"caution": "do_not_ignore_material_constraints", "meaning": "Flow, pressure, leakage, friction, and construction determine whether procedure works."},
        {"caution": "do_not_create_single_origin_myths", "meaning": "Study Greek, Hellenistic, Islamic-world, and later engineering traditions as transmission and transformation."},
    ]


def main() -> None:
    config = MechanicalProcedureConfig()
    themes = mechanical_procedure_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_mechanical_procedure_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_mechanical_procedure_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_mechanical_procedure_thread"),
        "mean_mechanical_score": round(mean(float(row["mechanical_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Banū Mūsā mechanical devices should be studied as embodied procedure: input, state, condition, transition, output, timing, feedback, and material constraint.",
    }

    write_csv(TABLES / "mechanical_procedure_themes.csv", themes)
    write_csv(TABLES / "mechanical_procedure_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "mechanical_procedure_summary.csv", [summary])

    write_json(JSON_DIR / "mechanical_procedure_config.json", asdict(config))
    write_json(JSON_DIR / "mechanical_procedure_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "mechanical_procedure_summary.json", summary)

    print("Banū Mūsā mechanical procedure map complete.")
    print(TABLES / "mechanical_procedure_summary.csv")


if __name__ == "__main__":
    main()
