from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import argparse
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
DATA_DIR = ARTICLE_ROOT / "data"


@dataclass(frozen=True)
class ClassificationGovernanceCase:
    case_name: str
    system_context: str
    decision_goal: str
    rule_documentation: float
    threshold_rationale: float
    feature_documentation: float
    score_interpretability: float
    calibration_review: float
    error_cost_review: float
    fairness_review: float
    human_review_path: float
    appeal_path: float
    traceability: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def classification_governance_score(case: ClassificationGovernanceCase) -> float:
    return clamp(
        100.0 * (
            0.09 * case.rule_documentation
            + 0.10 * case.threshold_rationale
            + 0.09 * case.feature_documentation
            + 0.09 * case.score_interpretability
            + 0.09 * case.calibration_review
            + 0.10 * case.error_cost_review
            + 0.10 * case.fairness_review
            + 0.09 * case.human_review_path
            + 0.08 * case.appeal_path
            + 0.08 * case.traceability
            + 0.06 * case.governance_review
            + 0.03 * case.communication_clarity
        )
    )


def classification_governance_risk(case: ClassificationGovernanceCase) -> float:
    weak_points = [
        1.0 - case.rule_documentation,
        1.0 - case.threshold_rationale,
        1.0 - case.feature_documentation,
        1.0 - case.score_interpretability,
        1.0 - case.calibration_review,
        1.0 - case.error_cost_review,
        1.0 - case.fairness_review,
        1.0 - case.human_review_path,
        1.0 - case.appeal_path,
        1.0 - case.traceability,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong decision-rule governance"
    if score >= 70 and risk <= 35:
        return "usable classification system with review needs"
    if risk >= 55:
        return "high risk; rules, thresholds, features, scores, error costs, review paths, fairness, or governance may be underdefined"
    return "partial discipline; strengthen threshold rationale, calibration, error-cost review, fairness, traceability, appeals, and governance"


def classify(score: float, threshold: float) -> int:
    return 1 if score >= threshold else 0


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def read_classification_rows(path: Path | None = None) -> list[dict[str, object]]:
    source = path or DATA_DIR / "classification_cases.csv"
    with source.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def confusion_counts(rows: list[dict[str, object]], threshold: float) -> dict[str, int]:
    counts = {"TP": 0, "FP": 0, "TN": 0, "FN": 0}

    for row in rows:
        predicted = classify(float(row["score"]), threshold)
        actual = int(row["actual"])

        if predicted == 1 and actual == 1:
            counts["TP"] += 1
        elif predicted == 1 and actual == 0:
            counts["FP"] += 1
        elif predicted == 0 and actual == 0:
            counts["TN"] += 1
        elif predicted == 0 and actual == 1:
            counts["FN"] += 1

    return counts


def classification_metrics(counts: dict[str, int]) -> dict[str, float]:
    tp = counts["TP"]
    fp = counts["FP"]
    tn = counts["TN"]
    fn = counts["FN"]

    return {
        "precision": round(safe_divide(tp, tp + fp), 6),
        "recall": round(safe_divide(tp, tp + fn), 6),
        "specificity": round(safe_divide(tn, tn + fp), 6),
        "false_positive_rate": round(safe_divide(fp, fp + tn), 6),
        "false_negative_rate": round(safe_divide(fn, fn + tp), 6),
        "accuracy": round(safe_divide(tp + tn, tp + tn + fp + fn), 6),
    }


def threshold_cost(counts: dict[str, int], false_positive_cost: float, false_negative_cost: float) -> float:
    return round(false_positive_cost * counts["FP"] + false_negative_cost * counts["FN"], 6)


def threshold_report(threshold: float, fp_cost: float = 1.0, fn_cost: float = 3.0) -> dict[str, object]:
    rows = read_classification_rows()
    counts = confusion_counts(rows, threshold)
    metrics = classification_metrics(counts)
    return {
        "threshold": threshold,
        **counts,
        **metrics,
        "error_cost": threshold_cost(counts, fp_cost, fn_cost),
        "false_positive_cost": fp_cost,
        "false_negative_cost": fn_cost,
    }


def threshold_examples() -> list[dict[str, object]]:
    return [threshold_report(threshold) for threshold in [0.30, 0.50, 0.70]]


def read_governance_cases(path: Path | None = None) -> list[ClassificationGovernanceCase]:
    source = path or DATA_DIR / "governance_cases.csv"
    cases: list[ClassificationGovernanceCase] = []

    with source.open("r", newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            cases.append(
                ClassificationGovernanceCase(
                    case_name=row["case_name"],
                    system_context=row["system_context"],
                    decision_goal=row["decision_goal"],
                    rule_documentation=float(row["rule_documentation"]),
                    threshold_rationale=float(row["threshold_rationale"]),
                    feature_documentation=float(row["feature_documentation"]),
                    score_interpretability=float(row["score_interpretability"]),
                    calibration_review=float(row["calibration_review"]),
                    error_cost_review=float(row["error_cost_review"]),
                    fairness_review=float(row["fairness_review"]),
                    human_review_path=float(row["human_review_path"]),
                    appeal_path=float(row["appeal_path"]),
                    traceability=float(row["traceability"]),
                    governance_review=float(row["governance_review"]),
                    communication_clarity=float(row["communication_clarity"]),
                )
            )

    return cases


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for case in read_governance_cases():
        score = classification_governance_score(case)
        risk = classification_governance_risk(case)
        rows.append({
            **asdict(case),
            "classification_governance_score": round(score, 3),
            "classification_governance_risk": round(risk, 3),
            "diagnostic": diagnose(score, risk),
        })

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_classification_governance_score": round(mean(float(row["classification_governance_score"]) for row in rows), 3),
        "average_classification_governance_risk": round(mean(float(row["classification_governance_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["classification_governance_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["classification_governance_risk"]))["case_name"],
        "interpretation": "Classification governance depends on rule documentation, threshold rationale, feature documentation, score interpretability, calibration review, error-cost review, fairness review, human review paths, appeal paths, traceability, governance review, and communication clarity."
    }


def main() -> None:
    audit_rows = run_audit()
    summary = summarize(audit_rows)
    thresholds = threshold_examples()

    write_csv(TABLES / "decision_rules_thresholds_classification_audit.csv", audit_rows)
    write_csv(TABLES / "decision_rules_thresholds_classification_audit_summary.csv", [summary])
    write_csv(TABLES / "decision_rules_thresholds_classification_threshold_examples.csv", thresholds)

    write_json(JSON_DIR / "decision_rules_thresholds_classification_audit.json", audit_rows)
    write_json(JSON_DIR / "decision_rules_thresholds_classification_audit_summary.json", summary)
    write_json(JSON_DIR / "decision_rules_thresholds_classification_threshold_examples.json", thresholds)

    print("Decision rules, thresholds, and classification audit complete.")
    print(TABLES / "decision_rules_thresholds_classification_audit.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Run the full audit. Default behavior also runs the audit.")
    parser.parse_args()
    main()
