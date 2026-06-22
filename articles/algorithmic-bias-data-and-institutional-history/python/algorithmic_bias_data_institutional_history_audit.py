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
class BiasHistoryConfig:
    article: str = "algorithmic_bias_data_and_institutional_history"
    selection_gap_threshold: float = 0.10
    representation_gap_threshold: float = 0.15
    label_gap_threshold: float = 0.08
    high_historical_risk_threshold: float = 0.55


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


def group_history_records() -> list[dict[str, object]]:
    return [
        {"group_id": "A", "data_share": 0.42, "deployment_share": 0.38, "selection_rate": 0.46, "label_positive_rate": 0.44, "verified_positive_rate": 0.41, "provenance_risk": 0.38, "measurement_weakness": 0.30, "proxy_risk": 0.36, "remediation": 0.68},
        {"group_id": "B", "data_share": 0.28, "deployment_share": 0.36, "selection_rate": 0.31, "label_positive_rate": 0.33, "verified_positive_rate": 0.43, "provenance_risk": 0.66, "measurement_weakness": 0.58, "proxy_risk": 0.62, "remediation": 0.42},
        {"group_id": "C", "data_share": 0.30, "deployment_share": 0.26, "selection_rate": 0.37, "label_positive_rate": 0.39, "verified_positive_rate": 0.42, "provenance_risk": 0.50, "measurement_weakness": 0.44, "proxy_risk": 0.48, "remediation": 0.54},
    ]


def compute_group_bias_metrics(row: dict[str, object]) -> dict[str, object]:
    data_share = float(row["data_share"])
    deployment_share = float(row["deployment_share"])
    label_positive_rate = float(row["label_positive_rate"])
    verified_positive_rate = float(row["verified_positive_rate"])
    remediation = float(row["remediation"])

    representation_gap = abs(data_share - deployment_share)
    label_gap = abs(label_positive_rate - verified_positive_rate)
    historical_risk = mean([
        float(row["provenance_risk"]),
        float(row["measurement_weakness"]),
        float(row["proxy_risk"]),
        1.0 - remediation,
    ])

    return {
        "group_id": row["group_id"],
        "data_share": round(data_share, 6),
        "deployment_share": round(deployment_share, 6),
        "representation_gap": round(representation_gap, 6),
        "selection_rate": round(float(row["selection_rate"]), 6),
        "label_positive_rate": round(label_positive_rate, 6),
        "verified_positive_rate": round(verified_positive_rate, 6),
        "label_gap": round(label_gap, 6),
        "provenance_risk": round(float(row["provenance_risk"]), 6),
        "measurement_weakness": round(float(row["measurement_weakness"]), 6),
        "proxy_risk": round(float(row["proxy_risk"]), 6),
        "remediation": round(remediation, 6),
        "historical_risk_score": round(historical_risk, 6),
    }


def audit_bias(metrics: list[dict[str, object]], config: BiasHistoryConfig) -> dict[str, object]:
    selection_gap = max(float(row["selection_rate"]) for row in metrics) - min(float(row["selection_rate"]) for row in metrics)
    total_representation_gap = sum(float(row["representation_gap"]) for row in metrics)
    max_label_gap = max(float(row["label_gap"]) for row in metrics)
    mean_historical_risk = mean(float(row["historical_risk_score"]) for row in metrics)
    max_historical_risk = max(float(row["historical_risk_score"]) for row in metrics)

    status = "pass"
    if (
        selection_gap >= config.selection_gap_threshold
        or total_representation_gap >= config.representation_gap_threshold
        or max_label_gap >= config.label_gap_threshold
        or max_historical_risk >= config.high_historical_risk_threshold
    ):
        status = "review"
    if selection_gap >= config.selection_gap_threshold and max_historical_risk >= config.high_historical_risk_threshold:
        status = "escalate"

    return {
        "selection_gap": round(selection_gap, 6),
        "total_representation_gap": round(total_representation_gap, 6),
        "max_label_gap": round(max_label_gap, 6),
        "mean_historical_risk_score": round(mean_historical_risk, 6),
        "max_historical_risk_score": round(max_historical_risk, 6),
        "status": status,
        "interpretation": "Bias review should connect selection gaps, representation gaps, label gaps, provenance risk, measurement weakness, proxy risk, remediation, and governance.",
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "data_provenance", "review_question": "Where did the data come from and what institutional history do they encode?", "status": "required"},
        {"item": "representation_review", "review_question": "Who is missing, overrepresented, or poorly represented?", "status": "required"},
        {"item": "measurement_validity", "review_question": "Do features and labels validly measure the intended constructs?", "status": "required"},
        {"item": "proxy_review", "review_question": "Which features carry historical inequality indirectly?", "status": "required"},
        {"item": "fairness_metrics", "review_question": "How do outcomes and errors differ across groups and contexts?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people challenge and correct outcomes?", "status": "required"},
        {"item": "remediation", "review_question": "What changes when bias is found?", "status": "required"},
    ]


def main() -> None:
    config = BiasHistoryConfig()
    records = group_history_records()
    metrics = [compute_group_bias_metrics(row) for row in records]
    audit = audit_bias(metrics, config)
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "groups_reviewed": len(metrics),
        "status": audit["status"],
        "selection_gap": audit["selection_gap"],
        "total_representation_gap": audit["total_representation_gap"],
        "max_label_gap": audit["max_label_gap"],
        "mean_historical_risk_score": audit["mean_historical_risk_score"],
        "max_historical_risk_score": audit["max_historical_risk_score"],
        "governance_items": len(governance),
        "interpretation": audit["interpretation"],
    }

    write_csv(TABLES / "bias_history_group_records.csv", records)
    write_csv(TABLES / "bias_history_group_metrics.csv", metrics)
    write_csv(TABLES / "bias_history_audit_summary.csv", [summary])
    write_csv(TABLES / "bias_history_governance_register.csv", governance)

    write_json(JSON_DIR / "bias_history_config.json", asdict(config))
    write_json(JSON_DIR / "bias_history_group_metrics.json", metrics)
    write_json(JSON_DIR / "bias_history_audit_summary.json", summary)
    write_json(JSON_DIR / "bias_history_governance_register.json", governance)

    print("Algorithmic bias, data, and institutional history audit complete.")
    print(TABLES / "bias_history_audit_summary.csv")


if __name__ == "__main__":
    main()
