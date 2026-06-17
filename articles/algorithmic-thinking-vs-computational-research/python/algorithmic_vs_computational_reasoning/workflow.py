from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class ReasoningProfile:
    name: str
    step_clarity: float
    decomposition: float
    control_flow: float
    testability: float
    representation_quality: float
    data_context: float
    complexity_awareness: float
    interpretability: float
    governance_readiness: float
    stakeholder_awareness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_profiles(path: Path) -> list[ReasoningProfile]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            ReasoningProfile(
                name=row["name"],
                step_clarity=float(row["step_clarity"]),
                decomposition=float(row["decomposition"]),
                control_flow=float(row["control_flow"]),
                testability=float(row["testability"]),
                representation_quality=float(row["representation_quality"]),
                data_context=float(row["data_context"]),
                complexity_awareness=float(row["complexity_awareness"]),
                interpretability=float(row["interpretability"]),
                governance_readiness=float(row["governance_readiness"]),
                stakeholder_awareness=float(row["stakeholder_awareness"]),
            )
            for row in reader
        ]


def score_algorithmic_thinking(profile: ReasoningProfile) -> float:
    return clamp(
        100.0 * (
            0.28 * profile.step_clarity
            + 0.24 * profile.decomposition
            + 0.24 * profile.control_flow
            + 0.24 * profile.testability
        )
    )


def score_computational_reasoning(profile: ReasoningProfile) -> float:
    return clamp(
        100.0 * (
            0.11 * profile.step_clarity
            + 0.10 * profile.decomposition
            + 0.09 * profile.control_flow
            + 0.10 * profile.testability
            + 0.13 * profile.representation_quality
            + 0.12 * profile.data_context
            + 0.11 * profile.complexity_awareness
            + 0.12 * profile.interpretability
            + 0.12 * profile.governance_readiness
            + 0.10 * profile.stakeholder_awareness
        )
    )


def diagnose(algorithmic_score: float, computational_score: float) -> str:
    gap = computational_score - algorithmic_score
    if algorithmic_score >= 75 and computational_score >= 75:
        return "strong procedural clarity and broad computational reasoning"
    if algorithmic_score >= 75 and computational_score < 60:
        return "procedure is clear but context, representation, or governance is weak"
    if algorithmic_score < 60 and computational_score >= 70:
        return "broad concerns are visible but executable procedure needs clarification"
    if gap >= 15:
        return "computational framing is stronger than procedural design"
    if gap <= -15:
        return "procedural design is stronger than broader reasoning"
    return "mixed profile requiring refinement"


def evaluate_profiles(profiles: list[ReasoningProfile]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for profile in profiles:
        algorithmic_score = score_algorithmic_thinking(profile)
        computational_score = score_computational_reasoning(profile)
        rows.append({
            **asdict(profile),
            "algorithmic_thinking_score": round(algorithmic_score, 3),
            "computational_reasoning_score": round(computational_score, 3),
            "reasoning_gap": round(computational_score - algorithmic_score, 3),
            "diagnostic": diagnose(algorithmic_score, computational_score),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "scenario_count": len(rows),
        "average_algorithmic_thinking_score": round(mean(float(row["algorithmic_thinking_score"]) for row in rows), 3),
        "average_computational_reasoning_score": round(mean(float(row["computational_reasoning_score"]) for row in rows), 3),
        "average_reasoning_gap": round(mean(float(row["reasoning_gap"]) for row in rows), 3),
        "strongest_algorithmic_thinking": max(rows, key=lambda row: float(row["algorithmic_thinking_score"]))["name"],
        "strongest_computational_reasoning": max(rows, key=lambda row: float(row["computational_reasoning_score"]))["name"],
        "interpretation": "Algorithmic thinking emphasizes procedural clarity; computational reasoning adds representation, context, complexity, interpretation, stakeholders, and governance."
    }


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_workflow(article_root: Path) -> None:
    profiles = load_profiles(article_root / "data" / "synthetic_reasoning_profiles.csv")
    rows = evaluate_profiles(profiles)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "algorithmic_vs_computational_reasoning.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "algorithmic_vs_computational_reasoning_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "algorithmic_vs_computational_reasoning.json", rows)
    write_json(article_root / "outputs" / "json" / "algorithmic_vs_computational_reasoning_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
