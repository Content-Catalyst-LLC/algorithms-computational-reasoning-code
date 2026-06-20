from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
import math

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"
DATA_DIR = ARTICLE_ROOT / "data"


@dataclass(frozen=True)
class RankingCase:
    case_name: str
    system_context: str
    ranking_goal: str
    candidate_transparency: float
    filter_documentation: float
    signal_documentation: float
    score_traceability: float
    alternative_visibility: float
    diversity_review: float
    feedback_loop_awareness: float
    personalization_clarity: float
    fairness_review: float
    governance_review: float
    communication_clarity: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def ranking_system_score(case: RankingCase) -> float:
    return clamp(
        100.0 * (
            0.10 * case.candidate_transparency
            + 0.10 * case.filter_documentation
            + 0.11 * case.signal_documentation
            + 0.11 * case.score_traceability
            + 0.08 * case.alternative_visibility
            + 0.09 * case.diversity_review
            + 0.10 * case.feedback_loop_awareness
            + 0.08 * case.personalization_clarity
            + 0.09 * case.fairness_review
            + 0.09 * case.governance_review
            + 0.05 * case.communication_clarity
        )
    )


def ranking_system_risk(case: RankingCase) -> float:
    weak_points = [
        1.0 - case.candidate_transparency,
        1.0 - case.filter_documentation,
        1.0 - case.signal_documentation,
        1.0 - case.score_traceability,
        1.0 - case.alternative_visibility,
        1.0 - case.diversity_review,
        1.0 - case.feedback_loop_awareness,
        1.0 - case.personalization_clarity,
        1.0 - case.fairness_review,
        1.0 - case.governance_review,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong ranking-governance discipline"
    if score >= 70 and risk <= 35:
        return "usable ranking system with review needs"
    if risk >= 55:
        return "high risk; candidates, filters, signals, scoring, diversity, feedback loops, fairness, or governance may be underdefined"
    return "partial discipline; strengthen candidate sourcing, filter logs, signal documentation, score traces, diversity review, fairness, and governance"


def read_cases(path: Path = DATA_DIR / "ranking_cases.csv") -> list[RankingCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        cases: list[RankingCase] = []
        for row in rows:
            numeric = {k: float(row[k]) for k in [
                "candidate_transparency", "filter_documentation", "signal_documentation",
                "score_traceability", "alternative_visibility", "diversity_review",
                "feedback_loop_awareness", "personalization_clarity", "fairness_review",
                "governance_review", "communication_clarity"
            ]}
            cases.append(RankingCase(row["case_name"], row["system_context"], row["ranking_goal"], **numeric))
    return cases


def cosine_similarity(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def score_candidate(candidate: dict[str, object], weights: dict[str, float]) -> float:
    return (
        weights["text_match"] * float(candidate["text_match"])
        + weights["quality"] * float(candidate["quality"])
        + weights["freshness"] * float(candidate["freshness"])
        + weights["diversity_bonus"] * float(candidate["diversity_bonus"])
        - weights["risk_penalty"] * float(candidate["risk_penalty"])
    )


def read_candidates(path: Path = DATA_DIR / "candidates.csv") -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        candidates: list[dict[str, object]] = []
        for row in rows:
            candidates.append({
                "candidate_id": row["candidate_id"],
                "title": row["title"],
                "eligible": row["eligible"].lower() == "true",
                "text_match": float(row["text_match"]),
                "quality": float(row["quality"]),
                "freshness": float(row["freshness"]),
                "diversity_bonus": float(row["diversity_bonus"]),
                "risk_penalty": float(row["risk_penalty"]),
                "source_type": row["source_type"],
            })
    return candidates


def rank_candidates(candidates: list[dict[str, object]], weights: dict[str, float]) -> list[dict[str, object]]:
    filtered = [candidate for candidate in candidates if bool(candidate["eligible"])]
    ranked = sorted(filtered, key=lambda candidate: score_candidate(candidate, weights), reverse=True)
    return [{**candidate, "ranking_score": round(score_candidate(candidate, weights), 6)} for candidate in ranked]


def run_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in read_cases():
        score = ranking_system_score(case)
        risk = ranking_system_risk(case)
        rows.append({**asdict(case), "ranking_system_score": round(score, 3), "ranking_system_risk": round(risk, 3), "diagnostic": diagnose(score, risk)})
    return rows


def calculator_examples() -> list[dict[str, object]]:
    weights = {"text_match": 0.36, "quality": 0.30, "freshness": 0.16, "diversity_bonus": 0.14, "risk_penalty": 0.20}
    ranked = rank_candidates(read_candidates(), weights)
    rows: list[dict[str, object]] = [{
        "example": "cosine_similarity",
        "left_vector": "[0.8, 0.2, 0.4]",
        "right_vector": "[0.7, 0.3, 0.5]",
        "similarity": round(cosine_similarity([0.8, 0.2, 0.4], [0.7, 0.3, 0.5]), 6),
    }]
    for index, candidate in enumerate(ranked):
        rows.append({"example": "ranked_candidate", "rank": index + 1, "candidate_id": candidate["candidate_id"], "title": candidate["title"], "ranking_score": candidate["ranking_score"]})
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_ranking_system_score": round(mean(float(row["ranking_system_score"]) for row in rows), 3),
        "average_ranking_system_risk": round(mean(float(row["ranking_system_risk"]) for row in rows), 3),
        "highest_score_case": max(rows, key=lambda row: float(row["ranking_system_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["ranking_system_risk"]))["case_name"],
        "interpretation": "Ranking-system reliability depends on candidate transparency, filter documentation, signal documentation, score traceability, alternative visibility, diversity review, feedback-loop awareness, personalization clarity, fairness review, governance review, and communication clarity."
    }


def main() -> None:
    audit_rows = run_audit()
    summary = summarize(audit_rows)
    calc_rows = calculator_examples()
    write_csv(TABLES / "ranking_filtering_recommendation_audit.csv", audit_rows)
    write_csv(TABLES / "ranking_filtering_recommendation_audit_summary.csv", [summary])
    write_csv(TABLES / "ranking_filtering_recommendation_calculator_examples.csv", calc_rows)
    write_json(JSON_DIR / "ranking_filtering_recommendation_audit.json", audit_rows)
    write_json(JSON_DIR / "ranking_filtering_recommendation_audit_summary.json", summary)
    write_json(JSON_DIR / "ranking_filtering_recommendation_calculator_examples.json", calc_rows)
    print("Ranking, filtering, and recommendation audit complete.")
    print(TABLES / "ranking_filtering_recommendation_audit.csv")


if __name__ == "__main__":
    main()
