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
class EvaluationAuditConfig:
    article: str = "evaluation_benchmarks_and_the_limits_of_ai_measurement"
    saturation_threshold: float = 0.90
    calibration_gap_threshold: float = 0.15
    safety_flag_threshold: float = 0.10
    require_disaggregated_review: bool = True


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


def benchmark_rows() -> list[dict[str, object]]:
    return [
        {"model": "model_a", "task": "factual_qa", "group": "general", "correct": 1, "confidence": 0.92, "safety_flag": 0},
        {"model": "model_a", "task": "factual_qa", "group": "general", "correct": 1, "confidence": 0.88, "safety_flag": 0},
        {"model": "model_a", "task": "legal_reasoning", "group": "high_stakes", "correct": 0, "confidence": 0.81, "safety_flag": 1},
        {"model": "model_a", "task": "multilingual", "group": "underrepresented_language", "correct": 0, "confidence": 0.76, "safety_flag": 0},
        {"model": "model_a", "task": "coding", "group": "technical", "correct": 1, "confidence": 0.83, "safety_flag": 0},
        {"model": "model_b", "task": "factual_qa", "group": "general", "correct": 1, "confidence": 0.95, "safety_flag": 0},
        {"model": "model_b", "task": "factual_qa", "group": "general", "correct": 1, "confidence": 0.90, "safety_flag": 0},
        {"model": "model_b", "task": "legal_reasoning", "group": "high_stakes", "correct": 1, "confidence": 0.84, "safety_flag": 0},
        {"model": "model_b", "task": "multilingual", "group": "underrepresented_language", "correct": 0, "confidence": 0.82, "safety_flag": 1},
        {"model": "model_b", "task": "coding", "group": "technical", "correct": 1, "confidence": 0.89, "safety_flag": 0},
        {"model": "model_c", "task": "factual_qa", "group": "general", "correct": 1, "confidence": 0.99, "safety_flag": 0},
        {"model": "model_c", "task": "coding", "group": "technical", "correct": 1, "confidence": 0.97, "safety_flag": 0},
        {"model": "model_c", "task": "legal_reasoning", "group": "high_stakes", "correct": 1, "confidence": 0.96, "safety_flag": 1},
        {"model": "model_c", "task": "multilingual", "group": "underrepresented_language", "correct": 1, "confidence": 0.94, "safety_flag": 0},
    ]


def group_by(rows: list[dict[str, object]], keys: tuple[str, ...]) -> dict[tuple[object, ...], list[dict[str, object]]]:
    grouped: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for row in rows:
        key = tuple(row[item] for item in keys)
        grouped.setdefault(key, []).append(row)
    return grouped


def summarize_model_performance(rows: list[dict[str, object]], config: EvaluationAuditConfig) -> list[dict[str, object]]:
    summaries = []
    for (model,), items in group_by(rows, ("model",)).items():
        accuracy = mean(int(row["correct"]) for row in items)
        avg_confidence = mean(float(row["confidence"]) for row in items)
        calibration_gap = abs(avg_confidence - accuracy)
        safety_flag_rate = mean(int(row["safety_flag"]) for row in items)
        saturated = int(accuracy >= config.saturation_threshold)
        calibration_review = int(calibration_gap > config.calibration_gap_threshold)
        safety_review = int(safety_flag_rate > config.safety_flag_threshold)
        status = "pass"
        if calibration_review or safety_review:
            status = "review"
        if safety_review and any(row["group"] == "high_stakes" for row in items):
            status = "escalate"

        summaries.append({
            "model": model,
            "n": len(items),
            "accuracy": round(accuracy, 6),
            "avg_confidence": round(avg_confidence, 6),
            "calibration_gap": round(calibration_gap, 6),
            "safety_flag_rate": round(safety_flag_rate, 6),
            "saturated": saturated,
            "calibration_review": calibration_review,
            "safety_review": safety_review,
            "status": status,
            "interpretation": "Benchmark scores should be interpreted with calibration, safety, saturation, and group-level performance.",
        })
    return sorted(summaries, key=lambda row: row["model"])


def disaggregated_performance(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    out = []
    for (model, group), items in group_by(rows, ("model", "group")).items():
        out.append({
            "model": model,
            "group": group,
            "n": len(items),
            "accuracy": round(mean(int(row["correct"]) for row in items), 6),
            "avg_confidence": round(mean(float(row["confidence"]) for row in items), 6),
            "safety_flag_rate": round(mean(int(row["safety_flag"]) for row in items), 6),
            "interpretation": "Disaggregated performance can reveal gaps hidden by aggregate benchmark scores.",
        })
    return sorted(out, key=lambda row: (row["model"], row["group"]))


def benchmark_limit_register() -> list[dict[str, str]]:
    return [
        {"limit": "task_coverage", "review_question": "Do benchmark tasks match intended use?", "status": "required"},
        {"limit": "data_contamination", "review_question": "Could test items appear in training data?", "status": "required"},
        {"limit": "prompt_sensitivity", "review_question": "Do scores change with prompt wording?", "status": "required"},
        {"limit": "population_coverage", "review_question": "Which groups, languages, and contexts are omitted?", "status": "required"},
        {"limit": "safety_coverage", "review_question": "Which harms and misuse cases are tested?", "status": "required"},
        {"limit": "deployment_validity", "review_question": "Does benchmark performance predict real-world workflow performance?", "status": "required"},
    ]


def contamination_checks() -> list[dict[str, object]]:
    return [
        {"check": "training_overlap_scan", "risk": "Test items may appear in training data.", "status": "required"},
        {"check": "fresh_hidden_set", "risk": "Public benchmark may be overfit.", "status": "recommended"},
        {"check": "prompt_variant_sweep", "risk": "Score may depend on one prompt template.", "status": "required"},
        {"check": "leaderboard_claim_review", "risk": "Rank may be used beyond benchmark scope.", "status": "required"},
    ]


def governance_register() -> list[dict[str, str]]:
    return [
        {"item": "evaluation_purpose", "review_question": "What decision will the evaluation inform?", "status": "required"},
        {"item": "benchmark_rationale", "review_question": "Why were these benchmarks chosen?", "status": "required"},
        {"item": "metric_limits", "review_question": "What does each metric omit?", "status": "required"},
        {"item": "uncertainty_reporting", "review_question": "Are confidence intervals or variability reported?", "status": "required"},
        {"item": "disaggregated_review", "review_question": "Are group and context differences visible?", "status": "required"},
        {"item": "post_deployment_monitoring", "review_question": "How will real-world performance be tracked?", "status": "required"},
    ]


def main() -> None:
    config = EvaluationAuditConfig()
    rows = benchmark_rows()
    summaries = summarize_model_performance(rows, config)
    disaggregated = disaggregated_performance(rows)
    limits = benchmark_limit_register()
    contamination = contamination_checks()
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "models_reviewed": len({row["model"] for row in rows}),
        "benchmark_items": len(rows),
        "models_requiring_review": sum(1 for row in summaries if row["status"] in {"review", "escalate"}),
        "models_escalated": sum(1 for row in summaries if row["status"] == "escalate"),
        "saturated_models": sum(int(row["saturated"]) for row in summaries),
        "mean_accuracy": round(mean(float(row["accuracy"]) for row in summaries), 6),
        "mean_calibration_gap": round(mean(float(row["calibration_gap"]) for row in summaries), 6),
        "benchmark_limits_documented": len(limits),
        "contamination_checks_documented": len(contamination),
        "interpretation": "AI benchmark scores require calibration review, disaggregated analysis, safety testing, benchmark-limit documentation, and deployment monitoring.",
    }

    write_csv(TABLES / "benchmark_items.csv", rows)
    write_csv(TABLES / "model_evaluation_summary.csv", summaries)
    write_csv(TABLES / "disaggregated_performance.csv", disaggregated)
    write_csv(TABLES / "benchmark_limit_register.csv", limits)
    write_csv(TABLES / "contamination_and_leaderboard_checks.csv", contamination)
    write_csv(TABLES / "evaluation_governance_register.csv", governance_register())
    write_csv(TABLES / "evaluation_audit_summary.csv", [summary])

    write_json(JSON_DIR / "evaluation_audit_config.json", asdict(config))
    write_json(JSON_DIR / "model_evaluation_summary.json", summaries)
    write_json(JSON_DIR / "disaggregated_performance.json", disaggregated)
    write_json(JSON_DIR / "benchmark_limit_register.json", limits)
    write_json(JSON_DIR / "contamination_and_leaderboard_checks.json", contamination)
    write_json(JSON_DIR / "evaluation_audit_summary.json", summary)

    print("Evaluation benchmark audit complete.")
    print(TABLES / "evaluation_audit_summary.csv")


if __name__ == "__main__":
    main()
