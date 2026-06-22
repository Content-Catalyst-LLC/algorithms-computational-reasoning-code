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
class ProxyAuditConfig:
    article: str = "proxy_variables_and_measurement_error"
    validity_gap_threshold: float = 0.30
    missingness_threshold: float = 0.20
    differential_error_threshold: float = 0.15
    label_error_threshold: float = 0.10


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


def proxy_cases() -> list[dict[str, object]]:
    return [
        {"case_id": "health_spending_as_need", "construct": "health_need", "proxy": "health_spending", "proxy_validity": 0.58, "missingness_rate": 0.12, "differential_error": 0.24, "label_error": 0.08},
        {"case_id": "clicks_as_value", "construct": "user_value", "proxy": "click_rate", "proxy_validity": 0.51, "missingness_rate": 0.05, "differential_error": 0.18, "label_error": 0.12},
        {"case_id": "test_scores_as_learning", "construct": "learning", "proxy": "standardized_score", "proxy_validity": 0.67, "missingness_rate": 0.08, "differential_error": 0.16, "label_error": 0.05},
        {"case_id": "expert_label_as_truth", "construct": "true_category", "proxy": "expert_label", "proxy_validity": 0.82, "missingness_rate": 0.03, "differential_error": 0.06, "label_error": 0.07},
        {"case_id": "arrest_record_as_risk", "construct": "future_harm_risk", "proxy": "prior_arrest_record", "proxy_validity": 0.45, "missingness_rate": 0.10, "differential_error": 0.31, "label_error": 0.14},
        {"case_id": "complaints_as_quality", "construct": "service_quality", "proxy": "complaint_count", "proxy_validity": 0.54, "missingness_rate": 0.28, "differential_error": 0.22, "label_error": 0.09},
    ]


def audit_proxy(row: dict[str, object], config: ProxyAuditConfig) -> dict[str, object]:
    validity = float(row["proxy_validity"])
    missingness = float(row["missingness_rate"])
    differential = float(row["differential_error"])
    label_error = float(row["label_error"])

    validity_gap = 1.0 - validity
    weak_validity = int(validity_gap >= config.validity_gap_threshold)
    high_missingness = int(missingness >= config.missingness_threshold)
    high_differential_error = int(differential >= config.differential_error_threshold)
    high_label_error = int(label_error >= config.label_error_threshold)

    measurement_risk = mean([validity_gap, missingness, differential, label_error])
    status = "pass"
    if weak_validity or high_differential_error or high_label_error:
        status = "review"
    if weak_validity and (high_differential_error or high_missingness or high_label_error):
        status = "escalate"

    return {
        "case_id": row["case_id"],
        "construct": row["construct"],
        "proxy": row["proxy"],
        "proxy_validity": round(validity, 6),
        "validity_gap": round(validity_gap, 6),
        "missingness_rate": round(missingness, 6),
        "differential_error": round(differential, 6),
        "label_error": round(label_error, 6),
        "weak_validity": weak_validity,
        "high_missingness": high_missingness,
        "high_differential_error": high_differential_error,
        "high_label_error": high_label_error,
        "measurement_risk_score": round(measurement_risk, 6),
        "status": status,
        "interpretation": "Proxy risk rises when construct validity is weak, missingness is high, differential error is large, or labels are unreliable.",
    }


def sensitivity_grid() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for error_rate in [0.00, 0.05, 0.10, 0.20, 0.30]:
        attenuation = 1.0 / (1.0 + error_rate)
        rows.append({
            "error_rate": error_rate,
            "attenuation_factor": round(attenuation, 6),
            "interpretation": "Higher measurement error can attenuate observed relationships and weaken model validity.",
        })
    return rows


def measurement_governance_register() -> list[dict[str, str]]:
    return [
        {"item": "construct_definition", "review_question": "What concept is the variable supposed to measure?", "status": "required"},
        {"item": "proxy_rationale", "review_question": "Why is this proxy appropriate?", "status": "required"},
        {"item": "data_provenance", "review_question": "Where did the data come from and how were they recorded?", "status": "required"},
        {"item": "error_analysis", "review_question": "What random, systematic, or differential errors are likely?", "status": "required"},
        {"item": "missingness_review", "review_question": "Who or what is missing from the record?", "status": "required"},
        {"item": "validation_plan", "review_question": "How will the proxy be validated against stronger evidence?", "status": "required"},
        {"item": "use_boundary", "review_question": "Which decisions should not rely on this proxy?", "status": "required"},
    ]


def main() -> None:
    config = ProxyAuditConfig()
    cases = proxy_cases()
    audits = [audit_proxy(row, config) for row in cases]
    sensitivity = sensitivity_grid()
    governance = measurement_governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "proxy_cases_reviewed": len(audits),
        "cases_passed": sum(1 for row in audits if row["status"] == "pass"),
        "cases_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "cases_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "mean_measurement_risk_score": round(mean(float(row["measurement_risk_score"]) for row in audits), 6),
        "mean_validity_gap": round(mean(float(row["validity_gap"]) for row in audits), 6),
        "sensitivity_scenarios": len(sensitivity),
        "governance_items": len(governance),
        "interpretation": "Proxy variables should be reviewed through construct validity, missingness, differential error, label error, validation, sensitivity analysis, and use boundaries.",
    }

    write_csv(TABLES / "proxy_variable_cases.csv", cases)
    write_csv(TABLES / "proxy_measurement_error_audit.csv", audits)
    write_csv(TABLES / "measurement_error_sensitivity_grid.csv", sensitivity)
    write_csv(TABLES / "measurement_governance_register.csv", governance)
    write_csv(TABLES / "proxy_audit_summary.csv", [summary])

    write_json(JSON_DIR / "proxy_audit_config.json", asdict(config))
    write_json(JSON_DIR / "proxy_measurement_error_audit.json", audits)
    write_json(JSON_DIR / "measurement_error_sensitivity_grid.json", sensitivity)
    write_json(JSON_DIR / "measurement_governance_register.json", governance)
    write_json(JSON_DIR / "proxy_audit_summary.json", summary)

    print("Proxy measurement-error audit complete.")
    print(TABLES / "proxy_audit_summary.csv")


if __name__ == "__main__":
    main()
