from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
import math
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"

@dataclass(frozen=True)
class PriorScenario:
    name: str
    alpha: float
    beta: float
    rationale: str

@dataclass(frozen=True)
class EvidenceBatch:
    batch_id: int
    observations: int
    successes: int
    evidence_note: str

@dataclass(frozen=True)
class BayesianAuditConfig:
    article: str
    threshold: float
    credible_mass: float

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

def beta_mean(alpha: float, beta: float) -> float:
    return alpha / (alpha + beta)

def beta_variance(alpha: float, beta: float) -> float:
    return (alpha * beta) / (((alpha + beta) ** 2) * (alpha + beta + 1.0))

def beta_pdf_unnormalized(x: float, alpha: float, beta: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return (x ** (alpha - 1.0)) * ((1.0 - x) ** (beta - 1.0))

def approximate_beta_cdf(x: float, alpha: float, beta: float, grid_size: int = 5000) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    step = 1.0 / grid_size
    total = 0.0
    partial = 0.0
    for i in range(1, grid_size + 1):
        midpoint = (i - 0.5) * step
        density = beta_pdf_unnormalized(midpoint, alpha, beta)
        total += density
        if midpoint <= x:
            partial += density
    return 0.0 if total == 0.0 else partial / total

def approximate_beta_quantile(q: float, alpha: float, beta: float) -> float:
    lo, hi = 0.0, 1.0
    for _ in range(50):
        mid = (lo + hi) / 2.0
        if approximate_beta_cdf(mid, alpha, beta) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

def read_prior_scenarios() -> list[PriorScenario]:
    path = ARTICLE_ROOT / "data" / "bayesian_prior_scenarios.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return [PriorScenario(row["name"], float(row["alpha"]), float(row["beta"]), row["rationale"]) for row in csv.DictReader(handle)]

def read_evidence_batches() -> list[EvidenceBatch]:
    path = ARTICLE_ROOT / "data" / "bayesian_evidence_batches.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        return [EvidenceBatch(int(row["batch_id"]), int(row["observations"]), int(row["successes"]), row["evidence_note"]) for row in csv.DictReader(handle)]

def summarize_distribution(scenario_name: str, alpha: float, beta: float, threshold: float, stage: str, observations: int, successes: int) -> dict[str, object]:
    variance_value = beta_variance(alpha, beta)
    return {
        "scenario": scenario_name,
        "stage": stage,
        "alpha": round(alpha, 6),
        "beta": round(beta, 6),
        "observations_added": observations,
        "successes_added": successes,
        "posterior_mean": round(beta_mean(alpha, beta), 6),
        "posterior_variance": round(variance_value, 8),
        "posterior_sd": round(math.sqrt(variance_value), 6),
        "p05": round(approximate_beta_quantile(0.05, alpha, beta), 6),
        "posterior_median": round(approximate_beta_quantile(0.50, alpha, beta), 6),
        "p95": round(approximate_beta_quantile(0.95, alpha, beta), 6),
        "threshold": threshold,
        "probability_above_threshold": round(1.0 - approximate_beta_cdf(threshold, alpha, beta), 6),
        "interpretation": "Posterior summaries show how evidence updates belief and uncertainty under the selected prior.",
    }

def sequential_update_rows(priors: list[PriorScenario], batches: list[EvidenceBatch], threshold: float) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for prior in priors:
        alpha, beta = prior.alpha, prior.beta
        rows.append({**summarize_distribution(prior.name, alpha, beta, threshold, "start_prior", 0, 0), "evidence_note": "Initial prior before sequential evidence."})
        for batch in batches:
            alpha += batch.successes
            beta += batch.observations - batch.successes
            rows.append({**summarize_distribution(prior.name, alpha, beta, threshold, f"after_batch_{batch.batch_id}", batch.observations, batch.successes), "evidence_note": batch.evidence_note})
    return rows

def final_posterior_rows(priors: list[PriorScenario], batches: list[EvidenceBatch], threshold: float) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    total_successes = sum(batch.successes for batch in batches)
    total_failures = sum(batch.observations - batch.successes for batch in batches)
    total_observations = sum(batch.observations for batch in batches)
    for prior in priors:
        alpha = prior.alpha + total_successes
        beta = prior.beta + total_failures
        rows.append({
            **summarize_distribution(prior.name, alpha, beta, threshold, "final_posterior", total_observations, total_successes),
            "prior_rationale": prior.rationale,
        })
    return rows

def prior_summary_rows(priors: list[PriorScenario], threshold: float) -> list[dict[str, object]]:
    return [{**summarize_distribution(prior.name, prior.alpha, prior.beta, threshold, "prior", 0, 0), "prior_rationale": prior.rationale} for prior in priors]

def prior_sensitivity_rows(final_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    means = [float(row["posterior_mean"]) for row in final_rows]
    probabilities = [float(row["probability_above_threshold"]) for row in final_rows]
    return [
        {"metric": "posterior_mean_range_across_priors", "min_value": round(min(means), 6), "max_value": round(max(means), 6), "range": round(max(means) - min(means), 6), "interpretation": "Large ranges indicate that prior assumptions remain influential after evidence."},
        {"metric": "threshold_probability_range_across_priors", "min_value": round(min(probabilities), 6), "max_value": round(max(probabilities), 6), "range": round(max(probabilities) - min(probabilities), 6), "interpretation": "Large ranges indicate that action-relevant posterior probability depends on prior choice."},
    ]

def posterior_decision_rows(final_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in final_rows:
        p_above = float(row["probability_above_threshold"])
        expected_loss_act = (1.0 - p_above) * 1.0
        expected_loss_wait = p_above * 2.5
        rows.append({
            "scenario": row["scenario"],
            "posterior_mean": row["posterior_mean"],
            "probability_above_threshold": round(p_above, 6),
            "expected_loss_if_act": round(expected_loss_act, 6),
            "expected_loss_if_wait": round(expected_loss_wait, 6),
            "recommended_action_under_synthetic_loss": "act" if expected_loss_act <= expected_loss_wait else "wait_for_more_evidence",
        })
    return rows

def posterior_predictive_rows(final_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [{"scenario": row["scenario"], "future_observations": 50, "posterior_mean_probability": row["posterior_mean"], "predictive_mean_successes": round(50 * float(row["posterior_mean"]), 6)} for row in final_rows]

def review_checklist() -> list[dict[str, object]]:
    return [
        {"check": "prior_rationale_documented", "status": "complete", "question": "Are priors named and justified?"},
        {"check": "likelihood_assumption_documented", "status": "partial", "question": "Is the evidence-generating model clearly explained?"},
        {"check": "sequential_updates_recorded", "status": "complete", "question": "Can each belief update be reconstructed?"},
        {"check": "posterior_uncertainty_reported", "status": "complete", "question": "Are posterior intervals or uncertainty summaries reported?"},
        {"check": "prior_sensitivity_tested", "status": "complete", "question": "Are conclusions compared across plausible priors?"},
        {"check": "posterior_predictive_validation", "status": "needs_review", "question": "Does the model reproduce or forecast observed patterns?"},
        {"check": "decision_rule_documented", "status": "partial", "question": "Are thresholds, losses, and action rules justified?"},
        {"check": "governance_and_contestability", "status": "needs_review", "question": "Can affected users or reviewers challenge evidence, priors, or posterior use?"},
    ]

def main() -> None:
    config = BayesianAuditConfig("bayesian_computation_and_updating_beliefs", 0.60, 0.90)
    priors = read_prior_scenarios()
    batches = read_evidence_batches()
    prior_rows = prior_summary_rows(priors, config.threshold)
    update_rows = sequential_update_rows(priors, batches, config.threshold)
    final_rows = final_posterior_rows(priors, batches, config.threshold)
    sensitivity_rows = prior_sensitivity_rows(final_rows)
    decision_rows = posterior_decision_rows(final_rows)
    predictive_rows = posterior_predictive_rows(final_rows)
    checklist_rows = review_checklist()
    audit_summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "threshold": config.threshold,
        "credible_mass": config.credible_mass,
        "prior_scenarios": len(priors),
        "evidence_batches": len(batches),
        "total_observations": sum(batch.observations for batch in batches),
        "total_successes": sum(batch.successes for batch in batches),
        "posterior_mean_range_across_priors": sensitivity_rows[0]["range"],
        "threshold_probability_range_across_priors": sensitivity_rows[1]["range"],
        "review_items_needing_attention": sum(1 for row in checklist_rows if row["status"] in {"partial", "needs_review"}),
        "interpretation": "Bayesian computation should document priors, evidence, posterior updates, prior sensitivity, decision rules, validation gaps, and governance implications.",
    }
    outputs = {
        "bayesian_prior_summaries": prior_rows,
        "bayesian_sequential_updates": update_rows,
        "bayesian_final_posteriors": final_rows,
        "bayesian_prior_sensitivity": sensitivity_rows,
        "bayesian_posterior_decisions": decision_rows,
        "bayesian_posterior_predictive_summary": predictive_rows,
        "bayesian_review_checklist": checklist_rows,
        "bayesian_computation_audit_summary": [audit_summary],
    }
    for name, rows in outputs.items():
        write_csv(TABLES / f"{name}.csv", rows)
        write_json(JSON_DIR / f"{name}.json", rows if name != "bayesian_computation_audit_summary" else audit_summary)
    write_json(JSON_DIR / "bayesian_audit_config.json", asdict(config))
    print("Bayesian computation audit complete.")
    print(TABLES / "bayesian_computation_audit_summary.csv")

if __name__ == "__main__":
    main()
