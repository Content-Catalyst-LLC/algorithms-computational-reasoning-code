from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class TranslationCase:
    case_name: str
    pseudocode_goal: str
    program_context: str
    intent_clarity: float
    input_specification: float
    output_specification: float
    state_handling: float
    control_flow_fidelity: float
    edge_case_coverage: float
    error_handling: float
    test_coverage: float
    readability: float
    maintainability: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_cases(path: Path) -> list[TranslationCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            TranslationCase(
                case_name=row["case_name"],
                pseudocode_goal=row["pseudocode_goal"],
                program_context=row["program_context"],
                intent_clarity=float(row["intent_clarity"]),
                input_specification=float(row["input_specification"]),
                output_specification=float(row["output_specification"]),
                state_handling=float(row["state_handling"]),
                control_flow_fidelity=float(row["control_flow_fidelity"]),
                edge_case_coverage=float(row["edge_case_coverage"]),
                error_handling=float(row["error_handling"]),
                test_coverage=float(row["test_coverage"]),
                readability=float(row["readability"]),
                maintainability=float(row["maintainability"]),
            )
            for row in reader
        ]


def translation_quality(case: TranslationCase) -> float:
    return clamp(
        100.0 * (
            0.12 * case.intent_clarity
            + 0.10 * case.input_specification
            + 0.10 * case.output_specification
            + 0.10 * case.state_handling
            + 0.12 * case.control_flow_fidelity
            + 0.10 * case.edge_case_coverage
            + 0.10 * case.error_handling
            + 0.10 * case.test_coverage
            + 0.08 * case.readability
            + 0.08 * case.maintainability
        )
    )


def translation_risk(case: TranslationCase) -> float:
    weak_points = [
        1.0 - case.intent_clarity,
        1.0 - case.input_specification,
        1.0 - case.output_specification,
        1.0 - case.control_flow_fidelity,
        1.0 - case.edge_case_coverage,
        1.0 - case.error_handling,
        1.0 - case.test_coverage,
        1.0 - case.maintainability,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 80 and risk <= 25:
        return "strong translation from pseudocode to program"
    if quality >= 65 and risk <= 40:
        return "usable translation with review needs"
    if risk >= 55:
        return "high translation risk; implementation may not preserve pseudocode intent"
    return "partial translation; clarify edge cases, errors, tests, or maintainability"


def evaluate_cases(cases: list[TranslationCase]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for case in cases:
        quality = translation_quality(case)
        risk = translation_risk(case)
        rows.append({
            **asdict(case),
            "translation_quality": round(quality, 3),
            "translation_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return rows


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_translation_quality": round(mean(float(row["translation_quality"]) for row in rows), 3),
        "average_translation_risk": round(mean(float(row["translation_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["translation_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["translation_risk"]))["case_name"],
        "interpretation": "Pseudocode-to-program translation quality depends on intent clarity, input/output specification, state handling, control-flow fidelity, edge cases, errors, tests, readability, and maintainability."
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
    cases = load_cases(article_root / "data" / "synthetic_pseudocode_translation_cases.csv")
    rows = evaluate_cases(cases)
    summary = summarize(rows)

    write_csv(article_root / "outputs" / "tables" / "pseudocode_translation_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "pseudocode_translation_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "pseudocode_translation_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "pseudocode_translation_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
