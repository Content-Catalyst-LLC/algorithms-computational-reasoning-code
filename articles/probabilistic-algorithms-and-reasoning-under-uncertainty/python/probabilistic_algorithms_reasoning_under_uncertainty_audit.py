from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, pstdev
import csv
import json
import math
import random
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ProbabilisticAuditConfig:
    experiment_name: str
    seed: int
    trial_batches: int
    threshold: float
    true_probability: float
    loss_false_positive: float
    loss_false_negative: float


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


def quantile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[int(position)]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def default_config() -> ProbabilisticAuditConfig:
    return ProbabilisticAuditConfig(
        experiment_name="probabilistic_algorithms_reasoning_under_uncertainty",
        seed=2026,
        trial_batches=200,
        threshold=0.60,
        true_probability=0.57,
        loss_false_positive=1.0,
        loss_false_negative=3.0,
    )


def bernoulli_trials(rng: random.Random, sample_size: int, probability: float) -> list[int]:
    return [1 if rng.random() < probability else 0 for _ in range(sample_size)]


def standard_error(p_hat: float, n: int) -> float:
    return math.sqrt(max(p_hat * (1.0 - p_hat), 0.0) / n)


def run_sampling_experiments(config: ProbabilisticAuditConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sample_size in [25, 50, 100, 250, 500, 1000]:
        for batch in range(1, config.trial_batches + 1):
            seed = config.seed + sample_size * 1000 + batch
            rng = random.Random(seed)
            trials = bernoulli_trials(rng, sample_size, config.true_probability)
            p_hat = sum(trials) / len(trials)
            se = standard_error(p_hat, sample_size)
            lower = max(0.0, p_hat - 1.96 * se)
            upper = min(1.0, p_hat + 1.96 * se)
            decision = 1 if p_hat >= config.threshold else 0
            rows.append({
                "experiment_name": config.experiment_name,
                "sample_size": sample_size,
                "batch": batch,
                "seed": seed,
                "true_probability": config.true_probability,
                "estimate": round(p_hat, 6),
                "standard_error": round(se, 6),
                "interval_lower": round(lower, 6),
                "interval_upper": round(upper, 6),
                "threshold": config.threshold,
                "decision": decision,
                "absolute_error": round(abs(p_hat - config.true_probability), 6),
                "interpretation": "Repeated probabilistic estimates show how sample size affects error and threshold decisions.",
            })
    return rows


def summarize_by_sample_size(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for sample_size in sorted(set(int(row["sample_size"]) for row in rows)):
        subset = [row for row in rows if int(row["sample_size"]) == sample_size]
        estimates = [float(row["estimate"]) for row in subset]
        errors = [float(row["absolute_error"]) for row in subset]
        decisions = [int(row["decision"]) for row in subset]
        output.append({
            "sample_size": sample_size,
            "batches": len(subset),
            "mean_estimate": round(mean(estimates), 6),
            "std_estimate": round(pstdev(estimates), 6),
            "p05_estimate": round(quantile(estimates, 0.05), 6),
            "median_estimate": round(quantile(estimates, 0.50), 6),
            "p95_estimate": round(quantile(estimates, 0.95), 6),
            "mean_absolute_error": round(mean(errors), 6),
            "max_absolute_error": round(max(errors), 6),
            "decision_rate": round(sum(decisions) / len(decisions), 6),
            "interpretation": "Larger samples usually reduce estimate variance, but threshold decisions may still vary near boundaries.",
        })
    return output


def randomized_quicksort_count(values: list[int], rng: random.Random) -> tuple[list[int], int]:
    if len(values) <= 1:
        return values, 0
    pivot = rng.choice(values)
    less = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    greater = [value for value in values if value > pivot]
    left_sorted, left_comparisons = randomized_quicksort_count(less, rng)
    right_sorted, right_comparisons = randomized_quicksort_count(greater, rng)
    comparisons = len(values) - 1 + left_comparisons + right_comparisons
    return left_sorted + equal + right_sorted, comparisons


def run_randomized_sort_audit(config: ProbabilisticAuditConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    base_values = list(range(1, 101))
    reversed_values = list(reversed(base_values))
    for run_id in range(1, 101):
        seed = config.seed + 50_000 + run_id
        rng = random.Random(seed)
        sorted_values, comparisons = randomized_quicksort_count(reversed_values, rng)
        rows.append({
            "algorithm": "randomized_quicksort",
            "run_id": run_id,
            "seed": seed,
            "n": len(reversed_values),
            "comparisons": comparisons,
            "is_sorted": int(sorted_values == base_values),
            "interpretation": "Randomized pivot choice changes comparison count while preserving sorted correctness.",
        })
    return rows


def summarize_sort_audit(rows: list[dict[str, object]]) -> dict[str, object]:
    comparisons = [int(row["comparisons"]) for row in rows]
    return {
        "algorithm": "randomized_quicksort",
        "runs": len(rows),
        "n": int(rows[0]["n"]),
        "all_runs_sorted": all(int(row["is_sorted"]) == 1 for row in rows),
        "mean_comparisons": round(mean(comparisons), 6),
        "std_comparisons": round(pstdev(comparisons), 6),
        "min_comparisons": min(comparisons),
        "max_comparisons": max(comparisons),
        "interpretation": "This Las Vegas-style example preserves correctness while runtime-related comparisons vary by random choices.",
    }


def expected_loss_decisions(config: ProbabilisticAuditConfig) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for probability in [0.10, 0.20, 0.35, 0.50, 0.60, 0.70, 0.85]:
        act_loss = (1.0 - probability) * config.loss_false_positive
        no_act_loss = probability * config.loss_false_negative
        rows.append({
            "event_probability": probability,
            "loss_false_positive": config.loss_false_positive,
            "loss_false_negative": config.loss_false_negative,
            "expected_loss_if_act": round(act_loss, 6),
            "expected_loss_if_do_not_act": round(no_act_loss, 6),
            "choose_action": int(act_loss <= no_act_loss),
            "interpretation": "Expected loss connects probabilistic evidence with asymmetric consequences.",
        })
    return rows


def probability_review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "probabilistic_method_defined", "status": "complete", "question": "Is the probabilistic procedure or inference task clearly described?"},
        {"check": "random_distribution_documented", "status": "complete", "question": "Are random draws, distributions, and sampling assumptions documented?"},
        {"check": "seed_policy_recorded", "status": "complete", "question": "Are random seeds recorded for reproducibility?"},
        {"check": "multi_seed_or_repeated_trials_used", "status": "complete", "question": "Are repeated trials used to estimate variability?"},
        {"check": "error_or_uncertainty_reported", "status": "complete", "question": "Are error bounds, standard errors, intervals, or variability reported?"},
        {"check": "threshold_sensitivity_reviewed", "status": "partial", "question": "Are decision thresholds tested across plausible values?"},
        {"check": "calibration_validated", "status": "needs_review", "question": "Are probability estimates calibrated against observed outcomes?"},
        {"check": "governance_implications_documented", "status": "partial", "question": "Are probability outputs connected to action rules, review, appeal, and use limits?"},
    ]


def main() -> None:
    config = default_config()
    sampling_rows = run_sampling_experiments(config)
    sample_summary_rows = summarize_by_sample_size(sampling_rows)
    sort_rows = run_randomized_sort_audit(config)
    sort_summary = summarize_sort_audit(sort_rows)
    expected_loss_rows = expected_loss_decisions(config)
    checklist_rows = probability_review_checklist()
    smallest_sample = min(sample_summary_rows, key=lambda row: int(row["sample_size"]))
    largest_sample = max(sample_summary_rows, key=lambda row: int(row["sample_size"]))
    audit_summary = {
        "article": "probabilistic_algorithms_and_reasoning_under_uncertainty",
        "timestamp_utc": timestamp_utc(),
        "true_probability": config.true_probability,
        "decision_threshold": config.threshold,
        "trial_batches": config.trial_batches,
        "smallest_sample_size": smallest_sample["sample_size"],
        "smallest_sample_mean_absolute_error": smallest_sample["mean_absolute_error"],
        "largest_sample_size": largest_sample["sample_size"],
        "largest_sample_mean_absolute_error": largest_sample["mean_absolute_error"],
        "randomized_sort_all_runs_correct": sort_summary["all_runs_sorted"],
        "randomized_sort_mean_comparisons": sort_summary["mean_comparisons"],
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Probabilistic algorithm audits should record random procedure, seeds, distributions, repeated trials, error summaries, threshold effects, and governance implications.",
    }
    write_csv(TABLES / "probabilistic_sampling_trials.csv", sampling_rows)
    write_csv(TABLES / "probabilistic_sampling_summary.csv", sample_summary_rows)
    write_csv(TABLES / "randomized_sort_audit.csv", sort_rows)
    write_csv(TABLES / "randomized_sort_summary.csv", [sort_summary])
    write_csv(TABLES / "expected_loss_decisions.csv", expected_loss_rows)
    write_csv(TABLES / "probability_review_checklist.csv", checklist_rows)
    write_csv(TABLES / "probabilistic_algorithm_audit_summary.csv", [audit_summary])
    write_json(JSON_DIR / "probabilistic_audit_config.json", asdict(config))
    write_json(JSON_DIR / "probabilistic_sampling_trials.json", sampling_rows)
    write_json(JSON_DIR / "probabilistic_sampling_summary.json", sample_summary_rows)
    write_json(JSON_DIR / "randomized_sort_audit.json", sort_rows)
    write_json(JSON_DIR / "randomized_sort_summary.json", sort_summary)
    write_json(JSON_DIR / "expected_loss_decisions.json", expected_loss_rows)
    write_json(JSON_DIR / "probability_review_checklist.json", checklist_rows)
    write_json(JSON_DIR / "probabilistic_algorithm_audit_summary.json", audit_summary)
    print("Probabilistic algorithm audit complete.")
    print(TABLES / "probabilistic_algorithm_audit_summary.csv")


if __name__ == "__main__":
    main()
