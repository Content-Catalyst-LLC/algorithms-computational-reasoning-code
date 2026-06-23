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
class SequencedActionConfig:
    article: str = "al_jazari_automata_and_sequenced_mechanical_action"
    core_threshold: float = 0.80
    high_sequence_threshold: float = 0.86


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


def sequenced_action_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "clocks_as_timed_state_change", "sequence_structure": 0.98, "timing_control": 0.98, "mechanical_embodiment": 0.94, "conditional_action": 0.90, "repeatability": 0.94, "documentation_quality": 0.92, "historical_significance": 0.96, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "elephant_clock_layered_sequence", "sequence_structure": 0.96, "timing_control": 0.94, "mechanical_embodiment": 0.96, "conditional_action": 0.92, "repeatability": 0.90, "documentation_quality": 0.92, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "cams_levers_control", "sequence_structure": 0.94, "timing_control": 0.92, "mechanical_embodiment": 0.98, "conditional_action": 0.92, "repeatability": 0.94, "documentation_quality": 0.88, "historical_significance": 0.94, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "water_raising_repeated_work", "sequence_structure": 0.92, "timing_control": 0.86, "mechanical_embodiment": 0.96, "conditional_action": 0.84, "repeatability": 0.98, "documentation_quality": 0.90, "historical_significance": 0.94, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "floats_vessels_thresholds", "sequence_structure": 0.92, "timing_control": 0.92, "mechanical_embodiment": 0.94, "conditional_action": 0.98, "repeatability": 0.90, "documentation_quality": 0.88, "historical_significance": 0.92, "ethical_caution": 0.82, "modern_resonance": 0.96},
        {"theme_id": "musical_automata_patterned_performance", "sequence_structure": 0.96, "timing_control": 0.96, "mechanical_embodiment": 0.94, "conditional_action": 0.88, "repeatability": 0.94, "documentation_quality": 0.88, "historical_significance": 0.92, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "diagrams_reproducibility_debugging", "sequence_structure": 0.88, "timing_control": 0.84, "mechanical_embodiment": 0.90, "conditional_action": 0.86, "repeatability": 0.90, "documentation_quality": 0.98, "historical_significance": 0.96, "ethical_caution": 0.86, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: SequencedActionConfig) -> dict[str, object]:
    sequenced_action_score = mean([
        float(row["sequence_structure"]),
        float(row["timing_control"]),
        float(row["mechanical_embodiment"]),
        float(row["conditional_action"]),
        float(row["repeatability"]),
        float(row["documentation_quality"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if sequenced_action_score >= config.core_threshold and float(row["sequence_structure"]) >= config.high_sequence_threshold:
        interpretive_status = "core_sequenced_mechanical_action_thread"
    elif sequenced_action_score >= config.core_threshold:
        interpretive_status = "major_sequenced_mechanical_action_thread"
    else:
        interpretive_status = "supporting_sequenced_mechanical_action_thread"

    return {
        "theme_id": row["theme_id"],
        "sequence_structure": round(float(row["sequence_structure"]), 6),
        "timing_control": round(float(row["timing_control"]), 6),
        "mechanical_embodiment": round(float(row["mechanical_embodiment"]), 6),
        "conditional_action": round(float(row["conditional_action"]), 6),
        "repeatability": round(float(row["repeatability"]), 6),
        "documentation_quality": round(float(row["documentation_quality"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "sequenced_action_score": round(sequenced_action_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_call_al_jazari_devices_modern_robots", "meaning": "The devices are automata and mechanical sequences, not modern robotics or AI."},
        {"caution": "do_not_call_the_book_source_code", "meaning": "Diagrams and instructions are technical specifications, not software code."},
        {"caution": "do_not_ignore_courtly_display", "meaning": "Spectacle and entertainment can coexist with serious engineering."},
        {"caution": "do_not_project_general_purpose_programming_backward", "meaning": "Adjustable or sequenced behavior is not the same as modern programmability."},
        {"caution": "do_not_ignore_material_constraints", "meaning": "Flow, weight, leakage, timing, wear, and calibration shape actual operation."},
    ]


def main() -> None:
    config = SequencedActionConfig()
    themes = sequenced_action_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_sequenced_mechanical_action_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_sequenced_mechanical_action_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_sequenced_mechanical_action_thread"),
        "mean_sequenced_action_score": round(mean(float(row["sequenced_action_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Al-Jazarī’s automata should be studied as sequenced mechanical action: timed state change, conditional triggers, repeatable cycles, mechanical embodiment, and documented reproducibility.",
    }

    write_csv(TABLES / "sequenced_action_themes.csv", themes)
    write_csv(TABLES / "sequenced_action_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "sequenced_action_summary.csv", [summary])

    write_json(JSON_DIR / "sequenced_action_config.json", asdict(config))
    write_json(JSON_DIR / "sequenced_action_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "sequenced_action_summary.json", summary)

    print("Al-Jazarī automata and sequenced mechanical action map complete.")
    print(TABLES / "sequenced_action_summary.csv")


if __name__ == "__main__":
    main()
