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
class WienerConfig:
    article: str = "norbert_wiener_cybernetics_and_feedback_in_computation"
    core_threshold: float = 0.80
    high_feedback_threshold: float = 0.86


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


def wiener_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "feedback_as_computational_structure", "feedback_centrality": 0.98, "control_relevance": 0.96, "communication_relevance": 0.94, "prediction_relevance": 0.86, "stability_relevance": 0.96, "amplification_risk": 0.90, "automation_ethics": 0.92, "ai_relevance": 0.96, "institutional_relevance": 0.92, "governance_caution": 0.96},
        {"theme_id": "control_communication_error", "feedback_centrality": 0.96, "control_relevance": 0.98, "communication_relevance": 0.98, "prediction_relevance": 0.88, "stability_relevance": 0.94, "amplification_risk": 0.84, "automation_ethics": 0.88, "ai_relevance": 0.92, "institutional_relevance": 0.88, "governance_caution": 0.92},
        {"theme_id": "negative_feedback_stability", "feedback_centrality": 0.98, "control_relevance": 0.96, "communication_relevance": 0.88, "prediction_relevance": 0.80, "stability_relevance": 0.98, "amplification_risk": 0.82, "automation_ethics": 0.86, "ai_relevance": 0.90, "institutional_relevance": 0.88, "governance_caution": 0.90},
        {"theme_id": "positive_feedback_amplification", "feedback_centrality": 0.96, "control_relevance": 0.90, "communication_relevance": 0.88, "prediction_relevance": 0.84, "stability_relevance": 0.84, "amplification_risk": 0.98, "automation_ethics": 0.94, "ai_relevance": 0.96, "institutional_relevance": 0.96, "governance_caution": 0.98},
        {"theme_id": "prediction_and_fire_control", "feedback_centrality": 0.92, "control_relevance": 0.98, "communication_relevance": 0.90, "prediction_relevance": 0.98, "stability_relevance": 0.88, "amplification_risk": 0.80, "automation_ethics": 0.92, "ai_relevance": 0.90, "institutional_relevance": 0.88, "governance_caution": 0.94},
        {"theme_id": "human_use_of_human_beings", "feedback_centrality": 0.88, "control_relevance": 0.90, "communication_relevance": 0.90, "prediction_relevance": 0.84, "stability_relevance": 0.82, "amplification_risk": 0.94, "automation_ethics": 0.98, "ai_relevance": 0.96, "institutional_relevance": 0.98, "governance_caution": 0.98},
        {"theme_id": "software_and_platform_feedback", "feedback_centrality": 0.98, "control_relevance": 0.94, "communication_relevance": 0.94, "prediction_relevance": 0.92, "stability_relevance": 0.88, "amplification_risk": 0.98, "automation_ethics": 0.94, "ai_relevance": 0.98, "institutional_relevance": 0.98, "governance_caution": 0.98},
        {"theme_id": "ai_governance_feedback_loops", "feedback_centrality": 0.98, "control_relevance": 0.96, "communication_relevance": 0.92, "prediction_relevance": 0.94, "stability_relevance": 0.90, "amplification_risk": 0.98, "automation_ethics": 0.98, "ai_relevance": 0.98, "institutional_relevance": 0.98, "governance_caution": 0.98},
    ]


def score_theme(row: dict[str, object], config: WienerConfig) -> dict[str, object]:
    cybernetic_score = mean([
        float(row["feedback_centrality"]),
        float(row["control_relevance"]),
        float(row["communication_relevance"]),
        float(row["prediction_relevance"]),
        float(row["stability_relevance"]),
        float(row["amplification_risk"]),
        float(row["automation_ethics"]),
        float(row["ai_relevance"]),
        float(row["institutional_relevance"]),
        float(row["governance_caution"]),
    ])

    if cybernetic_score >= config.core_threshold and float(row["feedback_centrality"]) >= config.high_feedback_threshold:
        interpretive_status = "core_wiener_cybernetic_feedback_thread"
    elif cybernetic_score >= config.core_threshold:
        interpretive_status = "major_wiener_cybernetic_feedback_thread"
    else:
        interpretive_status = "supporting_wiener_cybernetic_feedback_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "feedback_centrality", "control_relevance", "communication_relevance",
        "prediction_relevance", "stability_relevance", "amplification_risk",
        "automation_ethics", "ai_relevance", "institutional_relevance",
        "governance_caution"
    ]}
    scored.update({
        "theme_id": row["theme_id"],
        "cybernetic_score": round(cybernetic_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_feedback_as_inherently_good", "meaning": "Feedback can stabilize systems or amplify harm."},
        {"caution": "do_not_confuse_control_with_wisdom", "meaning": "A system can regulate toward the wrong goal."},
        {"caution": "do_not_ignore_human_agency", "meaning": "Automation can reorganize people around machine requirements."},
        {"caution": "do_not_erase_military_origins", "meaning": "Cybernetics was shaped partly by wartime prediction and control problems."},
        {"caution": "do_not_govern_models_without_governing_loops", "meaning": "AI governance must analyze how outputs reshape future inputs and institutions."},
    ]


def main() -> None:
    config = WienerConfig()
    themes = wiener_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_wiener_cybernetic_feedback_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_wiener_cybernetic_feedback_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_wiener_cybernetic_feedback_thread"),
        "mean_cybernetic_score": round(mean(float(row["cybernetic_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Wiener should be studied as a theorist of feedback, control, communication, prediction, automation ethics, and governance in computational systems.",
    }

    write_csv(TABLES / "wiener_themes.csv", themes)
    write_csv(TABLES / "wiener_cybernetic_feedback_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "wiener_cybernetic_feedback_summary.csv", [summary])

    write_json(JSON_DIR / "wiener_config.json", asdict(config))
    write_json(JSON_DIR / "wiener_cybernetic_feedback_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "wiener_cybernetic_feedback_summary.json", summary)

    print("Wiener cybernetic feedback map complete.")
    print(TABLES / "wiener_cybernetic_feedback_summary.csv")


if __name__ == "__main__":
    main()
