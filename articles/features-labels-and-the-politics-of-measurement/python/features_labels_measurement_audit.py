from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class MeasurementAuditConfig:
    experiment_name: str
    seed: int
    n: int
    threshold: float
    missingness_multiplier: float


@dataclass(frozen=True)
class FeatureRecord:
    feature_name: str
    construct_role: str
    source_process: str
    proxy_risk: str
    review_question: str


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


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


def default_config() -> MeasurementAuditConfig:
    return MeasurementAuditConfig(
        experiment_name="features_labels_measurement_audit",
        seed=2026,
        n=900,
        threshold=0.55,
        missingness_multiplier=0.14,
    )


def generate_synthetic_records(config: MeasurementAuditConfig) -> list[dict[str, object]]:
    rng = random.Random(config.seed)
    rows: list[dict[str, object]] = []
    for unit_id in range(1, config.n + 1):
        group = "A" if rng.random() < 0.58 else "B"
        prior_access = max(0.0, min(1.0, rng.gauss(0.62 if group == "A" else 0.47, 0.16)))
        latent_need = max(0.0, min(1.0, rng.gauss(0.48 + (0.12 if group == "B" else 0.02) - 0.18 * prior_access, 0.18)))
        engagement_count = max(0.0, rng.gauss(5.5 + 5.0 * prior_access - 1.8 * latent_need, 2.1))
        application_completeness = max(0.0, min(1.0, rng.gauss(0.64 + 0.22 * prior_access - 0.10 * latent_need, 0.15)))
        delay_days = max(0.0, rng.gauss(12.0 + 17.0 * latent_need - 4.0 * prior_access + (3.0 if group == "B" else 0.0), 5.5))
        missing_probability = min(0.45, config.missingness_multiplier + (0.10 if group == "B" else 0.02) + 0.10 * latent_need)
        prior_access_observed = None if rng.random() < missing_probability else prior_access
        proxy_score = sigmoid(-1.15 + 0.16 * engagement_count + 1.05 * application_completeness + 0.045 * delay_days - 0.60 * (prior_access_observed if prior_access_observed is not None else 0.40))
        true_construct_positive = 1 if latent_need >= config.threshold else 0
        label_noise_probability = 0.07 + (0.08 if group == "B" else 0.02) + (0.06 if prior_access_observed is None else 0.0)
        observed_label = 1 if proxy_score >= config.threshold else 0
        if rng.random() < label_noise_probability:
            observed_label = 1 - observed_label
        rows.append({
            "unit_id": unit_id,
            "group": group,
            "latent_need": round(latent_need, 6),
            "true_construct_positive": true_construct_positive,
            "prior_access": "" if prior_access_observed is None else round(prior_access_observed, 6),
            "prior_access_missing": 1 if prior_access_observed is None else 0,
            "engagement_count": round(engagement_count, 6),
            "application_completeness": round(application_completeness, 6),
            "delay_days": round(delay_days, 6),
            "proxy_score": round(proxy_score, 6),
            "observed_label": observed_label,
            "label_disagrees_with_construct": 1 if observed_label != true_construct_positive else 0,
            "interpretation": "Synthetic record for teaching feature, label, proxy, and measurement audits.",
        })
    return rows


def feature_register() -> list[dict[str, object]]:
    records = [
        FeatureRecord("engagement_count", "behavioral proxy", "platform or administrative log", "medium", "Does engagement reflect capacity, access, surveillance, or genuine interest?"),
        FeatureRecord("application_completeness", "documentation proxy", "form-processing workflow", "high", "Does completeness measure need or ability to navigate institutional paperwork?"),
        FeatureRecord("delay_days", "process timing variable", "case-management workflow", "medium", "Does delay reflect need, institutional backlog, geography, or staffing?"),
        FeatureRecord("prior_access", "historical access variable", "legacy service record", "high", "Does prior access encode historical advantage or institutional exclusion?"),
        FeatureRecord("observed_label", "training target", "thresholded administrative decision", "high", "Does the label measure the construct or reproduce a prior decision rule?"),
    ]
    return [asdict(item) for item in records]


def confusion_counts(rows: list[dict[str, object]], group: str | None = None) -> dict[str, int]:
    selected = rows if group is None else [row for row in rows if row["group"] == group]
    counts = {"tp": 0, "fp": 0, "tn": 0, "fn": 0}
    for row in selected:
        label = int(row["observed_label"])
        truth = int(row["true_construct_positive"])
        if label == 1 and truth == 1:
            counts["tp"] += 1
        elif label == 1 and truth == 0:
            counts["fp"] += 1
        elif label == 0 and truth == 0:
            counts["tn"] += 1
        else:
            counts["fn"] += 1
    return counts


def safe_rate(num: int, den: int) -> float:
    return 0.0 if den == 0 else num / den


def measurement_metrics(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for group in ["ALL", "A", "B"]:
        selected = rows if group == "ALL" else [row for row in rows if row["group"] == group]
        counts = confusion_counts(rows, None if group == "ALL" else group)
        tp, fp, tn, fn = counts["tp"], counts["fp"], counts["tn"], counts["fn"]
        out.append({
            "group": group,
            "n": len(selected),
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
            "label_positive_rate": round(mean(int(row["observed_label"]) for row in selected), 6),
            "construct_positive_rate": round(mean(int(row["true_construct_positive"]) for row in selected), 6),
            "label_disagreement_rate": round(mean(int(row["label_disagrees_with_construct"]) for row in selected), 6),
            "sensitivity": round(safe_rate(tp, tp + fn), 6),
            "specificity": round(safe_rate(tn, tn + fp), 6),
            "false_positive_rate": round(safe_rate(fp, fp + tn), 6),
            "false_negative_rate": round(safe_rate(fn, fn + tp), 6),
            "missing_prior_access_rate": round(mean(int(row["prior_access_missing"]) for row in selected), 6),
            "interpretation": "Measurement metrics compare observed labels with a latent synthetic construct for teaching purposes.",
        })
    return out


def feature_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    features = ["engagement_count", "application_completeness", "delay_days", "proxy_score"]
    out: list[dict[str, object]] = []
    for feature in features:
        values = [float(row[feature]) for row in rows]
        out.append({
            "feature": feature,
            "mean": round(mean(values), 6),
            "standard_deviation": round(pstdev(values), 6),
            "minimum": round(min(values), 6),
            "maximum": round(max(values), 6),
            "interpretation": "Feature summary supports review of scale, spread, and proxy behavior.",
        })
    observed_prior = [float(row["prior_access"]) for row in rows if row["prior_access"] != ""]
    out.append({
        "feature": "prior_access_observed_only",
        "mean": round(mean(observed_prior), 6),
        "standard_deviation": round(pstdev(observed_prior), 6),
        "minimum": round(min(observed_prior), 6),
        "maximum": round(max(observed_prior), 6),
        "interpretation": "Prior access excludes missing values, so interpretation must include missingness review.",
    })
    return out


def group_gap_rows(metrics: list[dict[str, object]]) -> list[dict[str, object]]:
    by_group = {row["group"]: row for row in metrics if row["group"] in {"A", "B"}}
    gap_rows: list[dict[str, object]] = []
    for metric in ["label_positive_rate", "construct_positive_rate", "label_disagreement_rate", "false_positive_rate", "false_negative_rate", "missing_prior_access_rate"]:
        a = float(by_group["A"][metric])
        b = float(by_group["B"][metric])
        gap_rows.append({
            "metric": metric,
            "group_A": round(a, 6),
            "group_B": round(b, 6),
            "absolute_gap": round(abs(a - b), 6),
            "interpretation": "Group gaps in measurement are audit signals, not proof of real-world difference.",
        })
    return gap_rows


def governance_checklist(metrics: list[dict[str, object]]) -> list[dict[str, object]]:
    all_metrics = next(row for row in metrics if row["group"] == "ALL")
    return [
        {
            "check": "label_disagreement",
            "status": "needs_review" if float(all_metrics["label_disagreement_rate"]) > 0.20 else "monitor",
            "review_question": "Is the training label close enough to the intended construct?",
        },
        {
            "check": "prior_access_missingness",
            "status": "needs_review" if float(all_metrics["missing_prior_access_rate"]) > 0.15 else "monitor",
            "review_question": "Is missingness patterned by institutional access or group membership?",
        },
        {
            "check": "construct_definition",
            "status": "required",
            "review_question": "Has the construct been defined independently of easy-to-measure proxies?",
        },
        {
            "check": "use_boundary",
            "status": "required",
            "review_question": "Where is measurement too weak for model deployment or automated action?",
        },
    ]


def main() -> None:
    config = default_config()
    rows = generate_synthetic_records(config)
    features = feature_register()
    metrics = measurement_metrics(rows)
    feature_stats = feature_summary(rows)
    gaps = group_gap_rows(metrics)
    checklist = governance_checklist(metrics)
    summary = {
        "article": "features_labels_and_the_politics_of_measurement",
        "timestamp_utc": timestamp_utc(),
        "n": config.n,
        "threshold": config.threshold,
        "overall_label_disagreement_rate": next(row for row in metrics if row["group"] == "ALL")["label_disagreement_rate"],
        "largest_group_measurement_gap": max(float(row["absolute_gap"]) for row in gaps),
        "governance_items_requiring_review": sum(1 for row in checklist if row["status"] in {"needs_review", "required"}),
        "interpretation": "Feature and label choices are measurement decisions. Model quality depends on whether measured variables validly represent the intended construct and whether error is distributed responsibly.",
    }
    write_csv(TABLES / "synthetic_measurement_records.csv", rows)
    write_csv(TABLES / "feature_register.csv", features)
    write_csv(TABLES / "feature_summary.csv", feature_stats)
    write_csv(TABLES / "measurement_metrics_by_group.csv", metrics)
    write_csv(TABLES / "group_measurement_gaps.csv", gaps)
    write_csv(TABLES / "measurement_governance_checklist.csv", checklist)
    write_csv(TABLES / "measurement_audit_summary.csv", [summary])
    write_json(JSON_DIR / "measurement_audit_config.json", asdict(config))
    write_json(JSON_DIR / "synthetic_measurement_records.json", rows)
    write_json(JSON_DIR / "feature_register.json", features)
    write_json(JSON_DIR / "measurement_metrics_by_group.json", metrics)
    write_json(JSON_DIR / "group_measurement_gaps.json", gaps)
    write_json(JSON_DIR / "measurement_governance_checklist.json", checklist)
    write_json(JSON_DIR / "measurement_audit_summary.json", summary)
    print("Feature, label, and measurement audit complete.")
    print(TABLES / "measurement_audit_summary.csv")


if __name__ == "__main__":
    main()
