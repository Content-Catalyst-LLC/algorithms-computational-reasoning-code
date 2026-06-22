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
class AccountabilityConfig:
    article: str = "algorithmic_accountability_and_audit_trails"
    low_audit_completeness_threshold: float = 0.75
    low_accountability_capacity_threshold: float = 0.70
    high_reconstruction_risk_threshold: float = 0.30


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


def system_records() -> list[dict[str, object]]:
    return [
        {"system_id": "benefits_eligibility_model", "required_records": 12, "available_records": 9, "documentation": 0.72, "provenance": 0.68, "reviewability": 0.64, "contestability": 0.58, "remediation": 0.52, "governance": 0.66, "stakes": 0.90},
        {"system_id": "credit_risk_score", "required_records": 12, "available_records": 11, "documentation": 0.86, "provenance": 0.82, "reviewability": 0.78, "contestability": 0.72, "remediation": 0.70, "governance": 0.80, "stakes": 0.84},
        {"system_id": "content_moderation_classifier", "required_records": 12, "available_records": 8, "documentation": 0.64, "provenance": 0.60, "reviewability": 0.58, "contestability": 0.48, "remediation": 0.50, "governance": 0.55, "stakes": 0.74},
        {"system_id": "clinical_triage_support", "required_records": 12, "available_records": 10, "documentation": 0.82, "provenance": 0.76, "reviewability": 0.80, "contestability": 0.70, "remediation": 0.74, "governance": 0.78, "stakes": 0.96},
    ]


def score_system(row: dict[str, object], config: AccountabilityConfig) -> dict[str, object]:
    required = float(row["required_records"])
    available = float(row["available_records"])
    audit_completeness = 0.0 if required == 0 else available / required
    accountability_capacity = mean([
        float(row["documentation"]),
        float(row["provenance"]),
        float(row["reviewability"]),
        float(row["contestability"]),
        float(row["remediation"]),
        float(row["governance"]),
    ])
    reconstruction_risk = float(row["stakes"]) * (1.0 - audit_completeness)

    status = "pass"
    if (
        audit_completeness < config.low_audit_completeness_threshold
        or accountability_capacity < config.low_accountability_capacity_threshold
        or reconstruction_risk >= config.high_reconstruction_risk_threshold
    ):
        status = "review"
    if reconstruction_risk >= config.high_reconstruction_risk_threshold and accountability_capacity < config.low_accountability_capacity_threshold:
        status = "escalate"

    return {
        "system_id": row["system_id"],
        "required_records": int(required),
        "available_records": int(available),
        "audit_completeness_score": round(audit_completeness, 6),
        "documentation": round(float(row["documentation"]), 6),
        "provenance": round(float(row["provenance"]), 6),
        "reviewability": round(float(row["reviewability"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "remediation": round(float(row["remediation"]), 6),
        "governance": round(float(row["governance"]), 6),
        "stakes": round(float(row["stakes"]), 6),
        "accountability_capacity_score": round(accountability_capacity, 6),
        "reconstruction_risk_score": round(reconstruction_risk, 6),
        "status": status,
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "data_provenance", "review_question": "Can data sources, transformations, and versions be traced?", "status": "required"},
        {"item": "model_versioning", "review_question": "Can the active model and threshold be reconstructed for each decision?", "status": "required"},
        {"item": "decision_logs", "review_question": "Are inputs, outputs, reasons, reviewers, and actions recorded?", "status": "required"},
        {"item": "appeal_records", "review_question": "Can affected people challenge outcomes and obtain correction?", "status": "required"},
        {"item": "incident_response", "review_question": "Are failures preserved, investigated, escalated, and remediated?", "status": "required"},
        {"item": "ownership", "review_question": "Who has authority to pause, modify, or retire the system?", "status": "required"},
    ]


def main() -> None:
    config = AccountabilityConfig()
    records = system_records()
    audit = [score_system(row, config) for row in records]
    governance = governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "systems_reviewed": len(audit),
        "systems_passed": sum(1 for row in audit if row["status"] == "pass"),
        "systems_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "systems_escalated": sum(1 for row in audit if row["status"] == "escalate"),
        "mean_audit_completeness_score": round(mean(float(row["audit_completeness_score"]) for row in audit), 6),
        "mean_accountability_capacity_score": round(mean(float(row["accountability_capacity_score"]) for row in audit), 6),
        "mean_reconstruction_risk_score": round(mean(float(row["reconstruction_risk_score"]) for row in audit), 6),
        "governance_items": len(governance),
        "interpretation": "Accountability review should connect audit completeness, provenance, decision logs, contestability, remediation, ownership, and reconstruction risk.",
    }

    write_csv(TABLES / "accountability_system_records.csv", records)
    write_csv(TABLES / "accountability_audit.csv", audit)
    write_csv(TABLES / "accountability_governance_register.csv", governance)
    write_csv(TABLES / "accountability_audit_summary.csv", [summary])

    write_json(JSON_DIR / "accountability_config.json", asdict(config))
    write_json(JSON_DIR / "accountability_audit.json", audit)
    write_json(JSON_DIR / "accountability_governance_register.json", governance)
    write_json(JSON_DIR / "accountability_audit_summary.json", summary)

    print("Algorithmic accountability and audit trails review complete.")
    print(TABLES / "accountability_audit_summary.csv")


if __name__ == "__main__":
    main()
