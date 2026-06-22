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
class DueProcessConfig:
    article: str = "contestability_appeals_and_algorithmic_due_process"
    minimum_contestability: float = 0.70
    high_stakes_threshold: float = 0.75
    high_burden_threshold: float = 0.60
    maximum_resolution_days: int = 14


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


def decision_contexts() -> list[dict[str, object]]:
    return [
        {"case_id": "public_benefits_eligibility", "domain": "public_administration", "stakes": 0.94, "notice": 0.70, "reasons": 0.62, "evidence_access": 0.48, "human_review": 0.55, "correction_capacity": 0.52, "remedy_capacity": 0.44, "appeal_burden": 0.72, "resolution_days": 21},
        {"case_id": "content_moderation_account_restriction", "domain": "platform", "stakes": 0.66, "notice": 0.74, "reasons": 0.58, "evidence_access": 0.42, "human_review": 0.50, "correction_capacity": 0.62, "remedy_capacity": 0.45, "appeal_burden": 0.54, "resolution_days": 8},
        {"case_id": "credit_application_review", "domain": "finance", "stakes": 0.82, "notice": 0.80, "reasons": 0.75, "evidence_access": 0.70, "human_review": 0.68, "correction_capacity": 0.72, "remedy_capacity": 0.61, "appeal_burden": 0.46, "resolution_days": 12},
        {"case_id": "hiring_screening_rank", "domain": "employment", "stakes": 0.78, "notice": 0.40, "reasons": 0.35, "evidence_access": 0.30, "human_review": 0.42, "correction_capacity": 0.35, "remedy_capacity": 0.20, "appeal_burden": 0.68, "resolution_days": 30},
        {"case_id": "health_risk_decision_support", "domain": "health", "stakes": 0.90, "notice": 0.76, "reasons": 0.72, "evidence_access": 0.74, "human_review": 0.86, "correction_capacity": 0.78, "remedy_capacity": 0.70, "appeal_burden": 0.38, "resolution_days": 6},
        {"case_id": "platform_visibility_rank", "domain": "creator_platform", "stakes": 0.58, "notice": 0.46, "reasons": 0.40, "evidence_access": 0.35, "human_review": 0.44, "correction_capacity": 0.48, "remedy_capacity": 0.28, "appeal_burden": 0.59, "resolution_days": 18},
    ]


def audit_context(row: dict[str, object], config: DueProcessConfig) -> dict[str, object]:
    safeguards = [
        float(row["notice"]),
        float(row["reasons"]),
        float(row["evidence_access"]),
        float(row["human_review"]),
        float(row["correction_capacity"]),
        float(row["remedy_capacity"]),
    ]
    contestability = mean(safeguards)
    stakes = float(row["stakes"])
    burden = float(row["appeal_burden"])
    resolution_days = int(row["resolution_days"])

    procedural_risk = stakes * (1.0 - contestability)
    appeal_effectiveness = mean([
        float(row["notice"]),
        float(row["reasons"]),
        float(row["human_review"]),
        float(row["correction_capacity"]),
        1.0 - burden,
        max(0.0, 1.0 - (resolution_days / max(1, config.maximum_resolution_days * 2))),
    ])

    high_stakes = int(stakes >= config.high_stakes_threshold)
    weak_contestability = int(contestability < config.minimum_contestability)
    high_burden = int(burden >= config.high_burden_threshold)
    slow_resolution = int(resolution_days > config.maximum_resolution_days)

    status = "pass"
    if weak_contestability or high_burden or slow_resolution:
        status = "review"
    if (high_stakes and weak_contestability) or (high_burden and slow_resolution):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "domain": row["domain"],
        "stakes": round(stakes, 6),
        "notice": round(float(row["notice"]), 6),
        "reasons": round(float(row["reasons"]), 6),
        "evidence_access": round(float(row["evidence_access"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "correction_capacity": round(float(row["correction_capacity"]), 6),
        "remedy_capacity": round(float(row["remedy_capacity"]), 6),
        "appeal_burden": round(burden, 6),
        "resolution_days": resolution_days,
        "contestability_score": round(contestability, 6),
        "appeal_effectiveness_score": round(appeal_effectiveness, 6),
        "procedural_risk_score": round(procedural_risk, 6),
        "high_stakes": high_stakes,
        "weak_contestability": weak_contestability,
        "high_burden": high_burden,
        "slow_resolution": slow_resolution,
        "status": status,
        "interpretation": "Procedural risk rises when high-stakes decisions have weak notice, reasons, evidence access, human review, correction, remedy, or accessible appeal.",
    }


def appeal_outcome_scenarios() -> list[dict[str, object]]:
    return [
        {"scenario": "low_appeal_low_reversal", "appeal_rate": 0.02, "reversal_rate": 0.01, "interpretation": "May indicate few errors, but also may indicate weak notice or inaccessible appeals."},
        {"scenario": "high_appeal_high_reversal", "appeal_rate": 0.22, "reversal_rate": 0.48, "interpretation": "May indicate systemic decision errors or poor initial review."},
        {"scenario": "high_appeal_low_reversal", "appeal_rate": 0.25, "reversal_rate": 0.04, "interpretation": "May indicate legitimate disagreement, unclear reasons, or ineffective appeal review."},
        {"scenario": "moderate_appeal_moderate_reversal", "appeal_rate": 0.10, "reversal_rate": 0.18, "interpretation": "Requires review of correction quality and subgroup patterns."},
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "notice", "review_question": "Do affected people know automation influenced the decision?", "status": "required"},
        {"item": "reasons", "review_question": "Are decision-specific reasons understandable and actionable?", "status": "required"},
        {"item": "evidence_access", "review_question": "Can affected people see or correct relevant records?", "status": "required"},
        {"item": "appeal_channel", "review_question": "Is there an accessible pathway to challenge the decision?", "status": "required"},
        {"item": "human_review", "review_question": "Can a reviewer meaningfully change the outcome?", "status": "required"},
        {"item": "correction_and_remedy", "review_question": "Are errors corrected in both decision and underlying records?", "status": "required"},
        {"item": "audit_trail", "review_question": "Are decision, model, data, and review histories preserved?", "status": "required"},
        {"item": "equity_monitoring", "review_question": "Are appeal access, burden, and outcomes monitored across groups?", "status": "required"},
    ]


def main() -> None:
    config = DueProcessConfig()
    contexts = decision_contexts()
    audits = [audit_context(row, config) for row in contexts]
    scenarios = appeal_outcome_scenarios()
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_contestability_score": round(mean(float(row["contestability_score"]) for row in audits), 6),
        "mean_appeal_effectiveness_score": round(mean(float(row["appeal_effectiveness_score"]) for row in audits), 6),
        "mean_procedural_risk_score": round(mean(float(row["procedural_risk_score"]) for row in audits), 6),
        "mean_appeal_burden": round(mean(float(row["appeal_burden"]) for row in audits), 6),
        "appeal_outcome_scenarios": len(scenarios),
        "governance_items": len(governance),
        "interpretation": "Algorithmic due process should be monitored through notice, reasons, evidence access, appeal burden, human review, correction, remedy, timeliness, and audit trails.",
    }

    write_csv(TABLES / "algorithmic_due_process_contexts.csv", contexts)
    write_csv(TABLES / "contestability_appeals_audit.csv", audits)
    write_csv(TABLES / "appeal_outcome_scenarios.csv", scenarios)
    write_csv(TABLES / "due_process_governance_register.csv", governance)
    write_csv(TABLES / "due_process_summary.csv", [summary])

    write_json(JSON_DIR / "due_process_config.json", asdict(config))
    write_json(JSON_DIR / "contestability_appeals_audit.json", audits)
    write_json(JSON_DIR / "appeal_outcome_scenarios.json", scenarios)
    write_json(JSON_DIR / "due_process_governance_register.json", governance)
    write_json(JSON_DIR / "due_process_summary.json", summary)

    print("Contestability, appeals, and algorithmic due process audit complete.")
    print(TABLES / "due_process_summary.csv")


if __name__ == "__main__":
    main()
