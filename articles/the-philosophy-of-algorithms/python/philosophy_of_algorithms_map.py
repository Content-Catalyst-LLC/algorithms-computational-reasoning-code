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
class AlgorithmicPhilosophyConfig:
    article: str = "the_philosophy_of_algorithms"
    review_threshold: float = 0.75
    high_consequence_threshold: float = 0.85


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


def philosophical_domains() -> list[dict[str, object]]:
    return [
        {"domain_id": "search_and_retrieval", "formalization_intensity": 0.82, "abstraction_risk": 0.76, "representation_risk": 0.88, "delegation_level": 0.72, "opacity": 0.74, "optimization_pressure": 0.86, "contestability_need": 0.78, "institutional_consequence": 0.82, "human_judgment_requirement": 0.76, "governance_urgency": 0.84},
        {"domain_id": "classification_and_scoring", "formalization_intensity": 0.90, "abstraction_risk": 0.92, "representation_risk": 0.94, "delegation_level": 0.88, "opacity": 0.82, "optimization_pressure": 0.88, "contestability_need": 0.96, "institutional_consequence": 0.96, "human_judgment_requirement": 0.94, "governance_urgency": 0.98},
        {"domain_id": "ranking_and_recommendation", "formalization_intensity": 0.86, "abstraction_risk": 0.88, "representation_risk": 0.90, "delegation_level": 0.90, "opacity": 0.86, "optimization_pressure": 0.96, "contestability_need": 0.86, "institutional_consequence": 0.94, "human_judgment_requirement": 0.84, "governance_urgency": 0.96},
        {"domain_id": "optimization_and_allocation", "formalization_intensity": 0.94, "abstraction_risk": 0.86, "representation_risk": 0.86, "delegation_level": 0.88, "opacity": 0.78, "optimization_pressure": 0.98, "contestability_need": 0.92, "institutional_consequence": 0.96, "human_judgment_requirement": 0.92, "governance_urgency": 0.96},
        {"domain_id": "scientific_modeling", "formalization_intensity": 0.92, "abstraction_risk": 0.84, "representation_risk": 0.82, "delegation_level": 0.62, "opacity": 0.66, "optimization_pressure": 0.70, "contestability_need": 0.78, "institutional_consequence": 0.82, "human_judgment_requirement": 0.92, "governance_urgency": 0.84},
        {"domain_id": "automated_decision_systems", "formalization_intensity": 0.94, "abstraction_risk": 0.96, "representation_risk": 0.96, "delegation_level": 0.98, "opacity": 0.88, "optimization_pressure": 0.90, "contestability_need": 0.98, "institutional_consequence": 0.98, "human_judgment_requirement": 0.98, "governance_urgency": 0.99},
        {"domain_id": "ai_generated_outputs", "formalization_intensity": 0.78, "abstraction_risk": 0.90, "representation_risk": 0.92, "delegation_level": 0.86, "opacity": 0.94, "optimization_pressure": 0.84, "contestability_need": 0.88, "institutional_consequence": 0.90, "human_judgment_requirement": 0.98, "governance_urgency": 0.96},
        {"domain_id": "agentic_tool_use", "formalization_intensity": 0.84, "abstraction_risk": 0.90, "representation_risk": 0.90, "delegation_level": 0.96, "opacity": 0.90, "optimization_pressure": 0.86, "contestability_need": 0.94, "institutional_consequence": 0.96, "human_judgment_requirement": 0.98, "governance_urgency": 0.99},
    ]


def score_domain(row: dict[str, object], config: AlgorithmicPhilosophyConfig) -> dict[str, object]:
    review_score = mean([
        float(row["formalization_intensity"]),
        float(row["abstraction_risk"]),
        float(row["representation_risk"]),
        float(row["delegation_level"]),
        float(row["opacity"]),
        float(row["optimization_pressure"]),
        float(row["contestability_need"]),
        float(row["institutional_consequence"]),
        float(row["human_judgment_requirement"]),
        float(row["governance_urgency"]),
    ])

    if review_score >= config.review_threshold and float(row["institutional_consequence"]) >= config.high_consequence_threshold:
        review_status = "high_priority_philosophical_review"
    elif review_score >= config.review_threshold:
        review_status = "philosophical_review_needed"
    else:
        review_status = "routine_conceptual_review"

    scored = {key: round(float(row[key]), 6) for key in [
        "formalization_intensity", "abstraction_risk", "representation_risk",
        "delegation_level", "opacity", "optimization_pressure", "contestability_need",
        "institutional_consequence", "human_judgment_requirement", "governance_urgency"
    ]}
    scored.update({"domain_id": row["domain_id"], "review_score": round(review_score, 6), "review_status": review_status})
    return scored


def philosophical_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_confuse_formalization_with_reality", "meaning": "Algorithms operate on representations, not the full world."},
        {"caution": "do_not_confuse_consistency_with_neutrality", "meaning": "A consistent procedure can still encode biased categories, data, objectives, or thresholds."},
        {"caution": "do_not_confuse_prediction_with_justification", "meaning": "A predicted outcome does not automatically justify an institutional action."},
        {"caution": "do_not_confuse_explanation_with_legitimacy", "meaning": "Explaining a system does not by itself make the system fair, lawful, or appropriate."},
        {"caution": "do_not_confuse_ai_output_with_accountable_reasoning", "meaning": "Generated output must be reviewed, sourced, tested, and governed before use."},
    ]


def delegation_risk(decision_severity: float, automation_level: float, opacity: float) -> float:
    return max(0.0, min(1.0, decision_severity * automation_level * opacity))


def main() -> None:
    config = AlgorithmicPhilosophyConfig()
    domains = philosophical_domains()
    scored = [score_domain(row, config) for row in domains]
    cautions = philosophical_cautions()
    delegation_rows = [
        {"case_id": "low_risk_calculation", "decision_severity": 0.20, "automation_level": 0.60, "opacity": 0.20, "delegation_risk": round(delegation_risk(0.20, 0.60, 0.20), 6)},
        {"case_id": "decision_support_score", "decision_severity": 0.70, "automation_level": 0.60, "opacity": 0.50, "delegation_risk": round(delegation_risk(0.70, 0.60, 0.50), 6)},
        {"case_id": "automated_eligibility_decision", "decision_severity": 0.95, "automation_level": 0.95, "opacity": 0.80, "delegation_risk": round(delegation_risk(0.95, 0.95, 0.80), 6)},
        {"case_id": "agentic_tool_workflow", "decision_severity": 0.85, "automation_level": 0.90, "opacity": 0.85, "delegation_risk": round(delegation_risk(0.85, 0.90, 0.85), 6)},
    ]
    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "domains_reviewed": len(scored),
        "high_priority_reviews": sum(1 for row in scored if row["review_status"] == "high_priority_philosophical_review"),
        "review_needed": sum(1 for row in scored if row["review_status"] == "philosophical_review_needed"),
        "routine_reviews": sum(1 for row in scored if row["review_status"] == "routine_conceptual_review"),
        "mean_review_score": round(mean(float(row["review_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "delegation_cases": len(delegation_rows),
        "interpretation": "The philosophy of algorithms examines procedure, formalization, abstraction, representation, delegation, explanation, limits, institutions, and responsibility.",
    }

    write_csv(TABLES / "philosophical_domains.csv", domains)
    write_csv(TABLES / "algorithmic_philosophy_review_map.csv", scored)
    write_csv(TABLES / "delegation_risk_examples.csv", delegation_rows)
    write_csv(TABLES / "philosophical_cautions.csv", cautions)
    write_csv(TABLES / "algorithmic_philosophy_summary.csv", [summary])
    write_json(JSON_DIR / "algorithmic_philosophy_config.json", asdict(config))
    write_json(JSON_DIR / "algorithmic_philosophy_review_map.json", scored)
    write_json(JSON_DIR / "delegation_risk_examples.json", delegation_rows)
    write_json(JSON_DIR / "philosophical_cautions.json", cautions)
    write_json(JSON_DIR / "algorithmic_philosophy_summary.json", summary)

    print("Algorithmic philosophy map complete.")
    print(TABLES / "algorithmic_philosophy_summary.csv")


if __name__ == "__main__":
    main()
