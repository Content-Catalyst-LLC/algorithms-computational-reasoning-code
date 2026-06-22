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
class HarmResponsibilityConfig:
    article: str = "algorithmic_harm_error_and_institutional_responsibility"
    high_harm_threshold: float = 0.30
    low_responsibility_threshold: float = 0.65
    remediation_gap_threshold: float = 0.20
    high_severity_threshold: float = 0.75


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


def harm_contexts() -> list[dict[str, object]]:
    return [
        {"case_id": "public_benefits_denial", "domain": "public_administration", "error_likelihood": 0.34, "severity": 0.92, "exposure": 0.78, "contestability": 0.42, "ownership": 0.48, "monitoring": 0.45, "appeals": 0.40, "repair": 0.35, "governance": 0.50},
        {"case_id": "credit_score_proxy_error", "domain": "finance", "error_likelihood": 0.24, "severity": 0.80, "exposure": 0.55, "contestability": 0.64, "ownership": 0.70, "monitoring": 0.62, "appeals": 0.66, "repair": 0.58, "governance": 0.68},
        {"case_id": "content_moderation_false_positive", "domain": "platform", "error_likelihood": 0.30, "severity": 0.58, "exposure": 0.72, "contestability": 0.50, "ownership": 0.52, "monitoring": 0.55, "appeals": 0.48, "repair": 0.36, "governance": 0.54},
        {"case_id": "hiring_ranking_bias", "domain": "employment", "error_likelihood": 0.28, "severity": 0.83, "exposure": 0.62, "contestability": 0.30, "ownership": 0.40, "monitoring": 0.38, "appeals": 0.20, "repair": 0.22, "governance": 0.36},
        {"case_id": "health_decision_support_error", "domain": "health", "error_likelihood": 0.18, "severity": 0.95, "exposure": 0.40, "contestability": 0.76, "ownership": 0.82, "monitoring": 0.78, "appeals": 0.72, "repair": 0.70, "governance": 0.80},
        {"case_id": "generative_ai_summary_error", "domain": "knowledge_work", "error_likelihood": 0.38, "severity": 0.62, "exposure": 0.65, "contestability": 0.54, "ownership": 0.46, "monitoring": 0.34, "appeals": 0.32, "repair": 0.40, "governance": 0.42},
    ]


def audit_harm(row: dict[str, object], config: HarmResponsibilityConfig) -> dict[str, object]:
    error = float(row["error_likelihood"])
    severity = float(row["severity"])
    exposure = float(row["exposure"])
    contestability = float(row["contestability"])
    responsibility_scores = [
        float(row["ownership"]),
        float(row["monitoring"]),
        float(row["appeals"]),
        float(row["repair"]),
        float(row["governance"]),
    ]

    harm_risk = error * severity * exposure * (1.0 - contestability)
    responsibility_capacity = mean(responsibility_scores)
    remediation_gap = max(0.0, severity - float(row["repair"]))
    high_harm = int(harm_risk >= config.high_harm_threshold)
    low_responsibility = int(responsibility_capacity < config.low_responsibility_threshold)
    high_remediation_gap = int(remediation_gap >= config.remediation_gap_threshold)
    high_severity = int(severity >= config.high_severity_threshold)

    status = "pass"
    if high_harm or low_responsibility or high_remediation_gap:
        status = "review"
    if (high_harm and low_responsibility) or (high_severity and high_remediation_gap and low_responsibility):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "domain": row["domain"],
        "error_likelihood": round(error, 6),
        "severity": round(severity, 6),
        "exposure": round(exposure, 6),
        "contestability": round(contestability, 6),
        "ownership": round(float(row["ownership"]), 6),
        "monitoring": round(float(row["monitoring"]), 6),
        "appeals": round(float(row["appeals"]), 6),
        "repair": round(float(row["repair"]), 6),
        "governance": round(float(row["governance"]), 6),
        "harm_risk_score": round(harm_risk, 6),
        "responsibility_capacity": round(responsibility_capacity, 6),
        "remediation_gap": round(remediation_gap, 6),
        "high_harm": high_harm,
        "low_responsibility": low_responsibility,
        "high_remediation_gap": high_remediation_gap,
        "high_severity": high_severity,
        "status": status,
        "interpretation": "Algorithmic harm risk rises with error likelihood, severity, exposure, and weak contestability; institutional responsibility depends on ownership, monitoring, appeals, repair, and governance.",
    }


def harm_taxonomy() -> list[dict[str, str]]:
    return [
        {"harm_type": "allocative", "description": "Resources or opportunities are distributed unfairly.", "review_focus": "outcomes and subgroup effects"},
        {"harm_type": "quality_of_service", "description": "System performs worse for some people or contexts.", "review_focus": "disaggregated performance"},
        {"harm_type": "representational", "description": "People are mislabeled, stereotyped, erased, or mischaracterized.", "review_focus": "labels and categories"},
        {"harm_type": "procedural", "description": "People cannot understand, contest, or correct decisions.", "review_focus": "notice appeals and repair"},
        {"harm_type": "autonomy", "description": "People are manipulated, constrained, surveilled, or nudged without adequate control.", "review_focus": "choice architecture and consent"},
        {"harm_type": "systemic", "description": "Cumulative harms reinforce institutional disadvantage.", "review_focus": "long-term and collective impacts"},
    ]


def incident_register() -> list[dict[str, str]]:
    return [
        {"field": "system_identifier", "purpose": "Link incident to model, tool, version, and workflow.", "required": "yes"},
        {"field": "harm_type", "purpose": "Classify allocative, representational, procedural, autonomy, or systemic harm.", "required": "yes"},
        {"field": "severity", "purpose": "Prioritize response and escalation.", "required": "yes"},
        {"field": "affected_context", "purpose": "Document who, where, and how the issue appeared.", "required": "yes"},
        {"field": "decision_trace", "purpose": "Preserve data, output, human action, and review history.", "required": "yes"},
        {"field": "remediation_status", "purpose": "Track correction, remedy, recurrence, and closure.", "required": "yes"},
        {"field": "recurrence_review", "purpose": "Determine whether source conditions have changed.", "required": "yes"},
    ]


def main() -> None:
    config = HarmResponsibilityConfig()
    contexts = harm_contexts()
    audits = [audit_harm(row, config) for row in contexts]
    taxonomy = harm_taxonomy()
    incidents = incident_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_harm_risk_score": round(mean(float(row["harm_risk_score"]) for row in audits), 6),
        "mean_responsibility_capacity": round(mean(float(row["responsibility_capacity"]) for row in audits), 6),
        "mean_remediation_gap": round(mean(float(row["remediation_gap"]) for row in audits), 6),
        "harm_taxonomy_entries": len(taxonomy),
        "incident_fields_required": len(incidents),
        "interpretation": "Institutional responsibility requires ownership, monitoring, appeal, repair, governance, incident reporting, and remediation capacity.",
    }

    write_csv(TABLES / "algorithmic_harm_contexts.csv", contexts)
    write_csv(TABLES / "harm_responsibility_audit.csv", audits)
    write_csv(TABLES / "algorithmic_harm_taxonomy.csv", taxonomy)
    write_csv(TABLES / "algorithmic_incident_register.csv", incidents)
    write_csv(TABLES / "harm_responsibility_summary.csv", [summary])

    write_json(JSON_DIR / "harm_responsibility_config.json", asdict(config))
    write_json(JSON_DIR / "harm_responsibility_audit.json", audits)
    write_json(JSON_DIR / "algorithmic_harm_taxonomy.json", taxonomy)
    write_json(JSON_DIR / "algorithmic_incident_register.json", incidents)
    write_json(JSON_DIR / "harm_responsibility_summary.json", summary)

    print("Algorithmic harm and institutional responsibility audit complete.")
    print(TABLES / "harm_responsibility_summary.csv")


if __name__ == "__main__":
    main()
