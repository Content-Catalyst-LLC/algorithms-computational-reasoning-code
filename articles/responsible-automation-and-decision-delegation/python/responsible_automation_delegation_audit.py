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
class DelegationConfig:
    article: str = "responsible_automation_and_decision_delegation"
    low_readiness_threshold: float = 0.70
    high_delegation_risk_threshold: float = 0.30
    high_automation_reliance_threshold: float = 0.85


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


def delegation_contexts() -> list[dict[str, object]]:
    return [
        {"context_id": "benefits_eligibility_denial", "evidence_quality": 0.62, "validation": 0.58, "reversibility": 0.46, "contestability": 0.52, "governance": 0.60, "human_review": 0.58, "automated_final_actions": 760, "total_decisions": 1000, "stakes": 0.92},
        {"context_id": "document_routing_support", "evidence_quality": 0.84, "validation": 0.82, "reversibility": 0.90, "contestability": 0.76, "governance": 0.78, "human_review": 0.74, "automated_final_actions": 80, "total_decisions": 1000, "stakes": 0.28},
        {"context_id": "content_visibility_ranking", "evidence_quality": 0.68, "validation": 0.64, "reversibility": 0.54, "contestability": 0.42, "governance": 0.56, "human_review": 0.44, "automated_final_actions": 930, "total_decisions": 1000, "stakes": 0.72},
        {"context_id": "clinical_triage_support", "evidence_quality": 0.78, "validation": 0.76, "reversibility": 0.70, "contestability": 0.68, "governance": 0.74, "human_review": 0.82, "automated_final_actions": 120, "total_decisions": 1000, "stakes": 0.96},
    ]


def score_context(row: dict[str, object], config: DelegationConfig) -> dict[str, object]:
    readiness = mean([
        float(row["evidence_quality"]),
        float(row["validation"]),
        float(row["reversibility"]),
        float(row["contestability"]),
        float(row["governance"]),
        float(row["human_review"]),
    ])
    total_decisions = float(row["total_decisions"])
    automation_reliance = 0.0 if total_decisions == 0 else float(row["automated_final_actions"]) / total_decisions
    delegation_risk = float(row["stakes"]) * (1.0 - readiness)

    recommendation = "delegate_with_controls"
    if readiness < config.low_readiness_threshold and float(row["stakes"]) >= 0.70:
        recommendation = "do_not_delegate_final_decision"
    elif delegation_risk >= config.high_delegation_risk_threshold:
        recommendation = "assist_only_or_escalate"
    elif automation_reliance >= config.high_automation_reliance_threshold and float(row["stakes"]) >= 0.60:
        recommendation = "reduce_automation_authority"
    elif float(row["stakes"]) <= 0.35 and readiness >= 0.75:
        recommendation = "constrained_automation_acceptable"

    status = "pass"
    if recommendation not in {"delegate_with_controls", "constrained_automation_acceptable"}:
        status = "review"
    if recommendation == "do_not_delegate_final_decision":
        status = "escalate"

    return {
        "context_id": row["context_id"],
        "evidence_quality": round(float(row["evidence_quality"]), 6),
        "validation": round(float(row["validation"]), 6),
        "reversibility": round(float(row["reversibility"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "governance": round(float(row["governance"]), 6),
        "human_review": round(float(row["human_review"]), 6),
        "automation_reliance_score": round(automation_reliance, 6),
        "stakes": round(float(row["stakes"]), 6),
        "delegation_readiness_score": round(readiness, 6),
        "delegation_risk_score": round(delegation_risk, 6),
        "recommendation": recommendation,
        "status": status,
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "use_case_legitimacy", "review_question": "Should this task be automated or delegated at all?", "status": "required"},
        {"item": "delegation_boundary", "review_question": "What authority is delegated and where must automation stop?", "status": "required"},
        {"item": "reversibility", "review_question": "Can errors be detected, corrected, remedied, and prevented from recurring?", "status": "required"},
        {"item": "human_escalation", "review_question": "Do uncertainty, high stakes, or disputes trigger meaningful human review?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people challenge delegated outcomes?", "status": "required"},
        {"item": "rollback_retirement", "review_question": "Can the institution pause, rollback, or retire unsafe automation?", "status": "required"},
    ]


def main() -> None:
    config = DelegationConfig()
    contexts = delegation_contexts()
    audit = [score_context(row, config) for row in contexts]
    governance = governance_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "contexts_reviewed": len(audit),
        "contexts_passed": sum(1 for row in audit if row["status"] == "pass"),
        "contexts_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "contexts_escalated": sum(1 for row in audit if row["status"] == "escalate"),
        "mean_delegation_readiness_score": round(mean(float(row["delegation_readiness_score"]) for row in audit), 6),
        "mean_delegation_risk_score": round(mean(float(row["delegation_risk_score"]) for row in audit), 6),
        "mean_automation_reliance_score": round(mean(float(row["automation_reliance_score"]) for row in audit), 6),
        "governance_items": len(governance),
        "interpretation": "Delegation review should connect evidence, validation, reversibility, contestability, governance, human review, automation reliance, and stakes.",
    }

    write_csv(TABLES / "delegation_contexts.csv", contexts)
    write_csv(TABLES / "delegation_readiness_audit.csv", audit)
    write_csv(TABLES / "delegation_governance_register.csv", governance)
    write_csv(TABLES / "delegation_audit_summary.csv", [summary])

    write_json(JSON_DIR / "delegation_config.json", asdict(config))
    write_json(JSON_DIR / "delegation_readiness_audit.json", audit)
    write_json(JSON_DIR / "delegation_governance_register.json", governance)
    write_json(JSON_DIR / "delegation_audit_summary.json", summary)

    print("Responsible automation and decision delegation audit complete.")
    print(TABLES / "delegation_audit_summary.csv")


if __name__ == "__main__":
    main()
