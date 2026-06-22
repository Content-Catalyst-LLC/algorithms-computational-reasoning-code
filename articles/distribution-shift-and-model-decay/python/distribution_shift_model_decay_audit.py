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
class DriftDecayConfig:
    article: str = "distribution_shift_and_model_decay"
    input_drift_threshold: float = 0.25
    label_drift_threshold: float = 0.15
    performance_decay_threshold: float = 0.08
    calibration_drift_threshold: float = 0.10
    subgroup_gap_threshold: float = 0.12
    override_rate_threshold: float = 0.12


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


def deployment_snapshots() -> list[dict[str, object]]:
    return [
        {"period": "baseline", "input_drift": 0.00, "label_drift": 0.00, "accuracy": 0.86, "calibration_gap": 0.05, "subgroup_gap": 0.07, "override_rate": 0.04},
        {"period": "month_1", "input_drift": 0.12, "label_drift": 0.04, "accuracy": 0.84, "calibration_gap": 0.06, "subgroup_gap": 0.08, "override_rate": 0.05},
        {"period": "month_2", "input_drift": 0.23, "label_drift": 0.10, "accuracy": 0.81, "calibration_gap": 0.09, "subgroup_gap": 0.11, "override_rate": 0.07},
        {"period": "month_3", "input_drift": 0.31, "label_drift": 0.16, "accuracy": 0.76, "calibration_gap": 0.14, "subgroup_gap": 0.15, "override_rate": 0.11},
        {"period": "month_4", "input_drift": 0.38, "label_drift": 0.19, "accuracy": 0.73, "calibration_gap": 0.18, "subgroup_gap": 0.18, "override_rate": 0.16},
        {"period": "month_5", "input_drift": 0.42, "label_drift": 0.23, "accuracy": 0.70, "calibration_gap": 0.21, "subgroup_gap": 0.22, "override_rate": 0.19},
    ]


def audit_snapshot(row: dict[str, object], baseline: dict[str, object], config: DriftDecayConfig) -> dict[str, object]:
    input_drift = float(row["input_drift"])
    label_drift = float(row["label_drift"])
    accuracy = float(row["accuracy"])
    calibration_gap = float(row["calibration_gap"])
    subgroup_gap = float(row["subgroup_gap"])
    override_rate = float(row["override_rate"])
    baseline_accuracy = float(baseline["accuracy"])

    performance_decay = baseline_accuracy - accuracy
    high_input_drift = int(input_drift >= config.input_drift_threshold)
    high_label_drift = int(label_drift >= config.label_drift_threshold)
    high_performance_decay = int(performance_decay >= config.performance_decay_threshold)
    high_calibration_drift = int(calibration_gap >= config.calibration_drift_threshold)
    high_subgroup_gap = int(subgroup_gap >= config.subgroup_gap_threshold)
    high_override_rate = int(override_rate >= config.override_rate_threshold)

    decay_risk_score = mean([input_drift, label_drift, max(0.0, performance_decay), calibration_gap, subgroup_gap, override_rate])

    status = "pass"
    if high_input_drift or high_label_drift or high_performance_decay or high_calibration_drift or high_subgroup_gap or high_override_rate:
        status = "review"
    if (high_performance_decay and high_calibration_drift) or (high_input_drift and high_subgroup_gap) or (high_override_rate and high_label_drift):
        status = "escalate"

    return {
        "period": row["period"],
        "input_drift": round(input_drift, 6),
        "label_drift": round(label_drift, 6),
        "accuracy": round(accuracy, 6),
        "performance_decay": round(performance_decay, 6),
        "calibration_gap": round(calibration_gap, 6),
        "subgroup_gap": round(subgroup_gap, 6),
        "override_rate": round(override_rate, 6),
        "high_input_drift": high_input_drift,
        "high_label_drift": high_label_drift,
        "high_performance_decay": high_performance_decay,
        "high_calibration_drift": high_calibration_drift,
        "high_subgroup_gap": high_subgroup_gap,
        "high_override_rate": high_override_rate,
        "decay_risk_score": round(decay_risk_score, 6),
        "status": status,
        "interpretation": "Model decay risk rises when data drift, label drift, performance loss, calibration drift, subgroup gaps, or override rates increase.",
    }


def response_register() -> list[dict[str, str]]:
    return [
        {"response": "recalibrate", "when_useful": "Confidence is unreliable but ranking still has value.", "risk": "May hide deeper concept drift."},
        {"response": "adjust_threshold", "when_useful": "Base rates or decision costs changed.", "risk": "May shift harms across groups."},
        {"response": "retrain", "when_useful": "Representative and validated new data are available.", "risk": "May learn feedback-shaped or contaminated patterns."},
        {"response": "rollback", "when_useful": "A new model or update causes incidents.", "risk": "Old model may also be unsafe."},
        {"response": "suspend", "when_useful": "Risk exceeds acceptable bounds.", "risk": "Requires fallback workflow and accountability."},
        {"response": "retire", "when_useful": "Use case no longer matches model assumptions.", "risk": "Requires replacement or process redesign."},
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "deployment_scope", "review_question": "Where is this model approved for use?", "status": "required"},
        {"item": "input_monitoring", "review_question": "How are input distributions tracked?", "status": "required"},
        {"item": "label_monitoring", "review_question": "How are outcome frequencies and definitions tracked?", "status": "required"},
        {"item": "performance_monitoring", "review_question": "How are accuracy and error patterns monitored over time?", "status": "required"},
        {"item": "calibration_monitoring", "review_question": "How is confidence reliability monitored?", "status": "required"},
        {"item": "subgroup_monitoring", "review_question": "How is decay tracked by group and context?", "status": "required"},
        {"item": "rollback_plan", "review_question": "When can the model be paused, rolled back, or retired?", "status": "required"},
    ]


def main() -> None:
    config = DriftDecayConfig()
    snapshots = deployment_snapshots()
    baseline = snapshots[0]
    audits = [audit_snapshot(row, baseline, config) for row in snapshots]
    responses = response_register()
    governance = governance_register()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "snapshots_reviewed": len(audits),
        "snapshots_passed": sum(1 for row in audits if row["status"] == "pass"),
        "snapshots_requiring_review": sum(1 for row in audits if row["status"] == "review"),
        "snapshots_escalated": sum(1 for row in audits if row["status"] == "escalate"),
        "latest_status": audits[-1]["status"],
        "latest_accuracy": audits[-1]["accuracy"],
        "latest_performance_decay": audits[-1]["performance_decay"],
        "mean_decay_risk_score": round(mean(float(row["decay_risk_score"]) for row in audits), 6),
        "response_options": len(responses),
        "governance_items": len(governance),
        "interpretation": "Model deployment should be monitored through input drift, label drift, performance decay, calibration drift, subgroup gaps, override rates, and rollback triggers.",
    }

    write_csv(TABLES / "deployment_snapshots.csv", snapshots)
    write_csv(TABLES / "drift_decay_audit.csv", audits)
    write_csv(TABLES / "drift_decay_response_register.csv", responses)
    write_csv(TABLES / "drift_decay_governance_register.csv", governance)
    write_csv(TABLES / "drift_decay_summary.csv", [summary])

    write_json(JSON_DIR / "drift_decay_config.json", asdict(config))
    write_json(JSON_DIR / "drift_decay_audit.json", audits)
    write_json(JSON_DIR / "drift_decay_response_register.json", responses)
    write_json(JSON_DIR / "drift_decay_governance_register.json", governance)
    write_json(JSON_DIR / "drift_decay_summary.json", summary)

    print("Distribution shift and model decay audit complete.")
    print(TABLES / "drift_decay_summary.csv")


if __name__ == "__main__":
    main()
