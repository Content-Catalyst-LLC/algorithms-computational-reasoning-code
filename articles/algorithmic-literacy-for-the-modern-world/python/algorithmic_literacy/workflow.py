from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class LiteracyCase:
    case_name: str
    system_context: str
    user_group: str
    procedural_transparency: float
    data_visibility: float
    output_interpretability: float
    uncertainty_communication: float
    contestability: float
    governance_readiness: float
    impact_awareness: float
    human_judgment_support: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[LiteracyCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            LiteracyCase(
                case_name=row["case_name"],
                system_context=row["system_context"],
                user_group=row["user_group"],
                procedural_transparency=float(row["procedural_transparency"]),
                data_visibility=float(row["data_visibility"]),
                output_interpretability=float(row["output_interpretability"]),
                uncertainty_communication=float(row["uncertainty_communication"]),
                contestability=float(row["contestability"]),
                governance_readiness=float(row["governance_readiness"]),
                impact_awareness=float(row["impact_awareness"]),
                human_judgment_support=float(row["human_judgment_support"]),
            )
            for row in reader
        ]


def literacy_support_score(case: LiteracyCase) -> float:
    return clamp(
        100.0 * (
            0.14 * case.procedural_transparency
            + 0.12 * case.data_visibility
            + 0.14 * case.output_interpretability
            + 0.12 * case.uncertainty_communication
            + 0.12 * case.contestability
            + 0.12 * case.governance_readiness
            + 0.12 * case.impact_awareness
            + 0.12 * case.human_judgment_support
        )
    )


def literacy_gap_score(case: LiteracyCase) -> float:
    weak_points = [
        1.0 - case.procedural_transparency,
        1.0 - case.data_visibility,
        1.0 - case.output_interpretability,
        1.0 - case.uncertainty_communication,
        1.0 - case.contestability,
        1.0 - case.governance_readiness,
        1.0 - case.impact_awareness,
        1.0 - case.human_judgment_support,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(support: float, gap: float) -> str:
    if support >= 80 and gap <= 25:
        return "strong literacy support"
    if support >= 65 and gap <= 40:
        return "moderate literacy support with review needs"
    if gap >= 55:
        return "high literacy gap; users may struggle to interpret or contest the system"
    return "partial literacy support; transparency, uncertainty, or governance should improve"


def evaluate_cases(cases: list[LiteracyCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        support = literacy_support_score(case)
        gap = literacy_gap_score(case)
        rows.append({
            **asdict(case),
            "literacy_support_score": round(support, 3),
            "literacy_gap_score": round(gap, 3),
            "diagnostic": diagnose(support, gap),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_literacy_support_score": round(mean(float(row["literacy_support_score"]) for row in rows), 3),
        "average_literacy_gap_score": round(mean(float(row["literacy_gap_score"]) for row in rows), 3),
        "highest_support_case": max(rows, key=lambda row: float(row["literacy_support_score"]))["case_name"],
        "highest_gap_case": max(rows, key=lambda row: float(row["literacy_gap_score"]))["case_name"],
        "interpretation": "Algorithmic literacy support depends on transparency, data visibility, interpretability, uncertainty communication, contestability, governance, impact awareness, and human judgment."
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
    cases = load_cases(article_root / "data" / "synthetic_algorithmic_literacy_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "algorithmic_literacy_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "algorithmic_literacy_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "algorithmic_literacy_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "algorithmic_literacy_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
