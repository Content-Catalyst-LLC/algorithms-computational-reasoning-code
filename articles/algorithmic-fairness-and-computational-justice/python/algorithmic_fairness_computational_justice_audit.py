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
class FairnessJusticeConfig:
    article: str = "algorithmic_fairness_and_computational_justice"
    selection_gap_threshold: float = 0.10
    error_gap_threshold: float = 0.10
    calibration_gap_threshold: float = 0.08
    low_justice_capacity_threshold: float = 0.65


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


def group_records() -> list[dict[str, object]]:
    return [
        {"group": "A", "n": 1000, "selected": 420, "true_positive": 260, "false_positive": 160, "false_negative": 140, "true_negative": 440, "mean_score": 0.62, "observed_rate": 0.58, "measurement_validity": 0.72, "contestability": 0.66, "remediation": 0.60},
        {"group": "B", "n": 1000, "selected": 310, "true_positive": 210, "false_positive": 100, "false_negative": 210, "true_negative": 480, "mean_score": 0.61, "observed_rate": 0.49, "measurement_validity": 0.58, "contestability": 0.44, "remediation": 0.42},
        {"group": "C", "n": 1000, "selected": 360, "true_positive": 230, "false_positive": 130, "false_negative": 170, "true_negative": 470, "mean_score": 0.59, "observed_rate": 0.54, "measurement_validity": 0.64, "contestability": 0.52, "remediation": 0.50},
    ]


def safe_rate(numerator: float, denominator: float) -> float:
    return 0.0 if denominator == 0 else numerator / denominator


def compute_group_metrics(row: dict[str, object]) -> dict[str, object]:
    tp = float(row["true_positive"])
    fp = float(row["false_positive"])
    fn = float(row["false_negative"])
    tn = float(row["true_negative"])
    n = float(row["n"])
    selected = float(row["selected"])
    mean_score = float(row["mean_score"])
    observed_rate = float(row["observed_rate"])

    actual_positive = tp + fn
    actual_negative = fp + tn

    selection_rate = safe_rate(selected, n)
    false_positive_rate = safe_rate(fp, actual_negative)
    false_negative_rate = safe_rate(fn, actual_positive)
    true_positive_rate = safe_rate(tp, actual_positive)
    calibration_gap = abs(mean_score - observed_rate)
    fairness_evidence = 1.0 - mean([false_positive_rate, false_negative_rate, calibration_gap])
    justice_capacity = mean([
        max(0.0, fairness_evidence),
        float(row["measurement_validity"]),
        float(row["contestability"]),
        float(row["remediation"]),
    ])

    return {
        "group": row["group"],
        "n": int(n),
        "selected": int(selected),
        "selection_rate": round(selection_rate, 6),
        "false_positive_rate": round(false_positive_rate, 6),
        "false_negative_rate": round(false_negative_rate, 6),
        "true_positive_rate": round(true_positive_rate, 6),
        "mean_score": round(mean_score, 6),
        "observed_rate": round(observed_rate, 6),
        "calibration_gap": round(calibration_gap, 6),
        "measurement_validity": round(float(row["measurement_validity"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "remediation": round(float(row["remediation"]), 6),
        "fairness_evidence_score": round(max(0.0, fairness_evidence), 6),
        "justice_capacity_score": round(justice_capacity, 6),
    }


def audit_fairness(metrics: list[dict[str, object]], config: FairnessJusticeConfig) -> dict[str, object]:
    selection_rates = [float(row["selection_rate"]) for row in metrics]
    fpr = [float(row["false_positive_rate"]) for row in metrics]
    fnr = [float(row["false_negative_rate"]) for row in metrics]
    tpr = [float(row["true_positive_rate"]) for row in metrics]
    calibration = [float(row["calibration_gap"]) for row in metrics]
    justice = [float(row["justice_capacity_score"]) for row in metrics]

    selection_gap = max(selection_rates) - min(selection_rates)
    false_positive_gap = max(fpr) - min(fpr)
    false_negative_gap = max(fnr) - min(fnr)
    true_positive_gap = max(tpr) - min(tpr)
    max_calibration_gap = max(calibration)
    mean_justice_capacity = mean(justice)

    status = "pass"
    if (
        selection_gap >= config.selection_gap_threshold
        or false_positive_gap >= config.error_gap_threshold
        or false_negative_gap >= config.error_gap_threshold
        or max_calibration_gap >= config.calibration_gap_threshold
        or mean_justice_capacity < config.low_justice_capacity_threshold
    ):
        status = "review"
    if (
        (false_negative_gap >= config.error_gap_threshold and mean_justice_capacity < config.low_justice_capacity_threshold)
        or (selection_gap >= config.selection_gap_threshold and max_calibration_gap >= config.calibration_gap_threshold)
    ):
        status = "escalate"

    return {
        "selection_gap": round(selection_gap, 6),
        "false_positive_gap": round(false_positive_gap, 6),
        "false_negative_gap": round(false_negative_gap, 6),
        "true_positive_gap": round(true_positive_gap, 6),
        "max_calibration_gap": round(max_calibration_gap, 6),
        "mean_justice_capacity_score": round(mean_justice_capacity, 6),
        "status": status,
        "interpretation": "Fairness review should compare selection, error, calibration, measurement validity, contestability, remediation, and governance together.",
    }


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "metric_choice", "review_question": "Which fairness definitions are used and why?", "status": "required"},
        {"item": "measurement_validity", "review_question": "Do labels and proxies validly represent the construct?", "status": "required"},
        {"item": "subgroup_analysis", "review_question": "Are outcomes and errors reviewed across relevant groups?", "status": "required"},
        {"item": "contestability", "review_question": "Can affected people understand and challenge outcomes?", "status": "required"},
        {"item": "remediation", "review_question": "Can errors and harms be corrected and repaired?", "status": "required"},
        {"item": "accountability", "review_question": "Who owns fairness monitoring and system change?", "status": "required"},
    ]


def main() -> None:
    config = FairnessJusticeConfig()
    records = group_records()
    metrics = [compute_group_metrics(row) for row in records]
    audit = audit_fairness(metrics, config)
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "groups_reviewed": len(metrics),
        "status": audit["status"],
        "selection_gap": audit["selection_gap"],
        "false_positive_gap": audit["false_positive_gap"],
        "false_negative_gap": audit["false_negative_gap"],
        "true_positive_gap": audit["true_positive_gap"],
        "max_calibration_gap": audit["max_calibration_gap"],
        "mean_justice_capacity_score": audit["mean_justice_capacity_score"],
        "governance_items": len(governance),
        "interpretation": audit["interpretation"],
    }

    write_csv(TABLES / "fairness_group_records.csv", records)
    write_csv(TABLES / "fairness_group_metrics.csv", metrics)
    write_csv(TABLES / "fairness_audit_summary.csv", [summary])
    write_csv(TABLES / "fairness_governance_register.csv", governance)

    write_json(JSON_DIR / "fairness_justice_config.json", asdict(config))
    write_json(JSON_DIR / "fairness_group_metrics.json", metrics)
    write_json(JSON_DIR / "fairness_audit_summary.json", summary)
    write_json(JSON_DIR / "fairness_governance_register.json", governance)

    print("Algorithmic fairness and computational justice audit complete.")
    print(TABLES / "fairness_audit_summary.csv")


if __name__ == "__main__":
    main()
