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
class GoodhartAuditConfig:
    article: str = "metrics_objectives_and_goodharts_law"
    high_pressure_threshold: float = 0.70
    proxy_gap_threshold: float = 0.20
    gaming_risk_threshold: float = 0.60
    guardrail_minimum: int = 2


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


def metric_cases() -> list[dict[str, object]]:
    return [
        {"case_id": "platform_engagement", "objective": "user_value", "metric": "watch_time", "proxy_alignment": 0.62, "optimization_pressure": 0.88, "gaming_risk": 0.72, "guardrails": 2},
        {"case_id": "model_benchmark", "objective": "deployment_reliability", "metric": "public_benchmark_score", "proxy_alignment": 0.55, "optimization_pressure": 0.91, "gaming_risk": 0.70, "guardrails": 1},
        {"case_id": "service_speed", "objective": "care_quality", "metric": "turnaround_time", "proxy_alignment": 0.66, "optimization_pressure": 0.76, "gaming_risk": 0.48, "guardrails": 2},
        {"case_id": "safety_reporting", "objective": "actual_safety", "metric": "reported_incidents", "proxy_alignment": 0.58, "optimization_pressure": 0.83, "gaming_risk": 0.65, "guardrails": 1},
        {"case_id": "calibrated_accuracy", "objective": "reliable_prediction", "metric": "calibrated_error_rate", "proxy_alignment": 0.86, "optimization_pressure": 0.52, "gaming_risk": 0.25, "guardrails": 3},
        {"case_id": "productivity_dashboard", "objective": "high_quality_work", "metric": "ticket_count", "proxy_alignment": 0.50, "optimization_pressure": 0.80, "gaming_risk": 0.67, "guardrails": 1},
    ]


def audit_case(row: dict[str, object], config: GoodhartAuditConfig) -> dict[str, object]:
    alignment = float(row["proxy_alignment"])
    pressure = float(row["optimization_pressure"])
    gaming = float(row["gaming_risk"])
    guardrails = int(row["guardrails"])

    proxy_gap = 1.0 - alignment
    high_pressure = int(pressure >= config.high_pressure_threshold)
    weak_proxy = int(proxy_gap >= config.proxy_gap_threshold)
    high_gaming = int(gaming >= config.gaming_risk_threshold)
    weak_guardrails = int(guardrails < config.guardrail_minimum)

    risk_score = mean([proxy_gap, pressure, gaming, 1.0 if weak_guardrails else 0.0])
    status = "pass"
    if high_pressure and weak_proxy:
        status = "review"
    if high_pressure and weak_proxy and (high_gaming or weak_guardrails):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "objective": row["objective"],
        "metric": row["metric"],
        "proxy_alignment": round(alignment, 6),
        "proxy_gap": round(proxy_gap, 6),
        "optimization_pressure": round(pressure, 6),
        "gaming_risk": round(gaming, 6),
        "guardrails": guardrails,
        "high_pressure": high_pressure,
        "weak_proxy": weak_proxy,
        "high_gaming": high_gaming,
        "weak_guardrails": weak_guardrails,
        "goodhart_risk_score": round(risk_score, 6),
        "status": status,
        "interpretation": "Goodhart risk rises when proxy alignment is weak, optimization pressure is high, gaming risk is high, and guardrails are thin.",
    }


def guardrail_register() -> list[dict[str, str]]:
    return [
        {"guardrail": "quality_review", "purpose": "Protect unmeasured quality from quantity optimization.", "status": "recommended"},
        {"guardrail": "equity_metric", "purpose": "Detect uneven harms across groups or contexts.", "status": "recommended"},
        {"guardrail": "drift_monitor", "purpose": "Track whether proxy-goal alignment changes over time.", "status": "required"},
        {"guardrail": "gaming_anomaly_check", "purpose": "Detect strategic manipulation of the metric.", "status": "required"},
        {"guardrail": "qualitative_review", "purpose": "Capture context that numbers omit.", "status": "recommended"},
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "goal_statement", "review_question": "What real objective should the metric represent?", "status": "required"},
        {"item": "proxy_validation", "review_question": "What evidence links the metric to the objective?", "status": "required"},
        {"item": "optimization_pressure", "review_question": "How strongly are people or algorithms pushed to improve the metric?", "status": "required"},
        {"item": "gaming_monitoring", "review_question": "How will strategic adaptation be detected?", "status": "required"},
        {"item": "guardrail_metrics", "review_question": "What counter-metrics prevent harmful optimization?", "status": "required"},
        {"item": "sunset_policy", "review_question": "When should the metric be revised or retired?", "status": "required"},
    ]


def main() -> None:
    config = GoodhartAuditConfig()
    cases = metric_cases()
    audits = [audit_case(row, config) for row in cases]
    guardrails = guardrail_register()
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_goodhart_risk_score": round(mean(float(row["goodhart_risk_score"]) for row in audits), 6),
        "mean_proxy_gap": round(mean(float(row["proxy_gap"]) for row in audits), 6),
        "guardrails_documented": len(guardrails),
        "governance_items": len(governance),
        "interpretation": "Metric governance should track proxy validity, optimization pressure, gaming risk, guardrails, and review triggers.",
    }

    write_csv(TABLES / "metric_objective_cases.csv", cases)
    write_csv(TABLES / "goodhart_risk_audit.csv", audits)
    write_csv(TABLES / "guardrail_metric_register.csv", guardrails)
    write_csv(TABLES / "metric_governance_register.csv", governance)
    write_csv(TABLES / "goodhart_audit_summary.csv", [summary])

    write_json(JSON_DIR / "goodhart_audit_config.json", asdict(config))
    write_json(JSON_DIR / "goodhart_risk_audit.json", audits)
    write_json(JSON_DIR / "guardrail_metric_register.json", guardrails)
    write_json(JSON_DIR / "metric_governance_register.json", governance)
    write_json(JSON_DIR / "goodhart_audit_summary.json", summary)

    print("Goodhart risk audit complete.")
    print(TABLES / "goodhart_audit_summary.csv")


if __name__ == "__main__":
    main()
