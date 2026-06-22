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
class DocumentationConfig:
    article: str = "documentation_model_cards_and_datasheets_for_algorithms"
    low_completeness_threshold: float = 0.80
    low_quality_threshold: float = 0.70
    high_documentation_risk_threshold: float = 0.30


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


def documentation_records() -> list[dict[str, object]]:
    return [
        {"system_id": "benefits_eligibility_model", "required_fields": 16, "completed_fields": 11, "accuracy": 0.62, "specificity": 0.58, "timeliness": 0.50, "accessibility": 0.56, "actionability": 0.52, "model_card": 1, "datasheet": 1, "risk_register": 1, "change_log": 0, "appeal_documentation": 1, "stakes": 0.92},
        {"system_id": "clinical_triage_support", "required_fields": 16, "completed_fields": 14, "accuracy": 0.82, "specificity": 0.78, "timeliness": 0.76, "accessibility": 0.72, "actionability": 0.76, "model_card": 1, "datasheet": 1, "risk_register": 1, "change_log": 1, "appeal_documentation": 1, "stakes": 0.96},
        {"system_id": "content_ranking_system", "required_fields": 16, "completed_fields": 10, "accuracy": 0.58, "specificity": 0.50, "timeliness": 0.44, "accessibility": 0.46, "actionability": 0.42, "model_card": 0, "datasheet": 1, "risk_register": 0, "change_log": 1, "appeal_documentation": 0, "stakes": 0.72},
        {"system_id": "document_routing_tool", "required_fields": 16, "completed_fields": 15, "accuracy": 0.86, "specificity": 0.84, "timeliness": 0.82, "accessibility": 0.78, "actionability": 0.80, "model_card": 1, "datasheet": 1, "risk_register": 1, "change_log": 1, "appeal_documentation": 1, "stakes": 0.30},
    ]


def score_record(row: dict[str, object], config: DocumentationConfig) -> dict[str, object]:
    required = float(row["required_fields"])
    completed = float(row["completed_fields"])
    completeness = 0.0 if required == 0 else completed / required
    quality = mean([
        float(row["accuracy"]),
        completeness,
        float(row["specificity"]),
        float(row["timeliness"]),
        float(row["accessibility"]),
        float(row["actionability"]),
    ])
    artifact_coverage = mean([
        float(row["model_card"]),
        float(row["datasheet"]),
        float(row["risk_register"]),
        float(row["change_log"]),
        float(row["appeal_documentation"]),
    ])
    documentation_risk = float(row["stakes"]) * (1.0 - quality)

    status = "pass"
    if (
        completeness < config.low_completeness_threshold
        or quality < config.low_quality_threshold
        or documentation_risk >= config.high_documentation_risk_threshold
    ):
        status = "review"
    if documentation_risk >= config.high_documentation_risk_threshold and artifact_coverage < 0.80:
        status = "escalate"

    return {
        "system_id": row["system_id"],
        "required_fields": int(required),
        "completed_fields": int(completed),
        "documentation_completeness_score": round(completeness, 6),
        "accuracy": round(float(row["accuracy"]), 6),
        "specificity": round(float(row["specificity"]), 6),
        "timeliness": round(float(row["timeliness"]), 6),
        "accessibility": round(float(row["accessibility"]), 6),
        "actionability": round(float(row["actionability"]), 6),
        "artifact_coverage_score": round(artifact_coverage, 6),
        "documentation_quality_score": round(quality, 6),
        "stakes": round(float(row["stakes"]), 6),
        "documentation_risk_score": round(documentation_risk, 6),
        "status": status,
    }


def documentation_register() -> list[dict[str, str]]:
    return [
        {"artifact": "model_card", "review_question": "Does the model card state purpose, intended use, evaluation, limits, and governance?", "status": "required"},
        {"artifact": "datasheet", "review_question": "Does the datasheet record dataset motivation, composition, collection, processing, uses, and maintenance?", "status": "required"},
        {"artifact": "risk_register", "review_question": "Are risks, controls, owners, and escalation triggers documented?", "status": "required"},
        {"artifact": "change_log", "review_question": "Can system, data, model, threshold, and governance changes be reconstructed?", "status": "required"},
        {"artifact": "appeal_documentation", "review_question": "Can affected people understand, challenge, and correct outcomes?", "status": "required"},
        {"artifact": "maintenance_plan", "review_question": "Is documentation reviewed and updated after changes or incidents?", "status": "required"},
    ]


def main() -> None:
    config = DocumentationConfig()
    records = documentation_records()
    audit = [score_record(row, config) for row in records]
    register = documentation_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_passed": sum(1 for row in audit if row["status"] == "pass"),
        "systems_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "systems_escalated": sum(1 for row in audit if row["status"] == "escalate"),
        "mean_documentation_completeness_score": round(mean(float(row["documentation_completeness_score"]) for row in audit), 6),
        "mean_documentation_quality_score": round(mean(float(row["documentation_quality_score"]) for row in audit), 6),
        "mean_artifact_coverage_score": round(mean(float(row["artifact_coverage_score"]) for row in audit), 6),
        "mean_documentation_risk_score": round(mean(float(row["documentation_risk_score"]) for row in audit), 6),
        "documentation_artifacts": len(register),
        "interpretation": "Documentation review should connect model cards, datasheets, risk registers, change logs, appeal documentation, accuracy, specificity, timeliness, accessibility, and actionability.",
    }

    write_csv(TABLES / "documentation_records.csv", records)
    write_csv(TABLES / "documentation_audit.csv", audit)
    write_csv(TABLES / "documentation_register.csv", register)
    write_csv(TABLES / "documentation_audit_summary.csv", [summary])

    write_json(JSON_DIR / "documentation_config.json", asdict(config))
    write_json(JSON_DIR / "documentation_audit.json", audit)
    write_json(JSON_DIR / "documentation_register.json", register)
    write_json(JSON_DIR / "documentation_audit_summary.json", summary)

    print("Documentation, model cards, and datasheets audit complete.")
    print(TABLES / "documentation_audit_summary.csv")


if __name__ == "__main__":
    main()
