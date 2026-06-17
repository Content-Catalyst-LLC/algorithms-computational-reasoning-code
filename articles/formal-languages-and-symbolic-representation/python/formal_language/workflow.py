from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import csv
import json
from statistics import mean


@dataclass(frozen=True)
class FormalLanguageCase:
    case_name: str
    representation_context: str
    symbolic_structure: str
    alphabet_clarity: float
    grammar_explicitness: float
    syntax_validation: float
    semantic_clarity: float
    parser_readiness: float
    schema_support: float
    error_reporting: float
    testability: float
    interoperability: float
    governance_readiness: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def representation_quality(case: FormalLanguageCase) -> float:
    return clamp(100.0 * (
        0.10 * case.alphabet_clarity
        + 0.12 * case.grammar_explicitness
        + 0.12 * case.syntax_validation
        + 0.12 * case.semantic_clarity
        + 0.10 * case.parser_readiness
        + 0.10 * case.schema_support
        + 0.10 * case.error_reporting
        + 0.08 * case.testability
        + 0.08 * case.interoperability
        + 0.08 * case.governance_readiness
    ))


def representation_risk(case: FormalLanguageCase) -> float:
    weak_points = [
        1.0 - case.alphabet_clarity,
        1.0 - case.grammar_explicitness,
        1.0 - case.syntax_validation,
        1.0 - case.semantic_clarity,
        1.0 - case.parser_readiness,
        1.0 - case.schema_support,
        1.0 - case.error_reporting,
        1.0 - case.interoperability,
    ]
    return clamp(100.0 * mean(weak_points))


def diagnose(quality: float, risk: float) -> str:
    if quality >= 80 and risk <= 25:
        return "strong symbolic representation with clear grammar, validation, and interpretation"
    if quality >= 65 and risk <= 40:
        return "usable symbolic representation with review needs"
    if risk >= 55:
        return "high representation risk; language, grammar, schema, or semantics may be unclear"
    return "partial symbolic representation; improve grammar, semantics, validation, or governance"


def load_cases(path: Path) -> list[FormalLanguageCase]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        return [
            FormalLanguageCase(
                row["case_name"],
                row["representation_context"],
                row["symbolic_structure"],
                float(row["alphabet_clarity"]),
                float(row["grammar_explicitness"]),
                float(row["syntax_validation"]),
                float(row["semantic_clarity"]),
                float(row["parser_readiness"]),
                float(row["schema_support"]),
                float(row["error_reporting"]),
                float(row["testability"]),
                float(row["interoperability"]),
                float(row["governance_readiness"]),
            )
            for row in rows
        ]


def evaluate_cases(cases: list[FormalLanguageCase]) -> list[dict[str, object]]:
    out = []
    for case in cases:
        quality = representation_quality(case)
        risk = representation_risk(case)
        out.append({
            **asdict(case),
            "representation_quality": round(quality, 3),
            "representation_risk": round(risk, 3),
            "diagnostic": diagnose(quality, risk),
        })
    return out


def summarize(rows: list[dict[str, object]]) -> dict[str, object]:
    return {
        "case_count": len(rows),
        "average_representation_quality": round(mean(float(row["representation_quality"]) for row in rows), 3),
        "average_representation_risk": round(mean(float(row["representation_risk"]) for row in rows), 3),
        "highest_quality_case": max(rows, key=lambda row: float(row["representation_quality"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda row: float(row["representation_risk"]))["case_name"],
        "interpretation": "Symbolic representation quality depends on grammar, syntax, semantics, validation, interoperability, and governance.",
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
    rows = evaluate_cases(load_cases(article_root / "data" / "synthetic_formal_language_cases.csv"))
    summary = summarize(rows)
    write_csv(article_root / "outputs" / "tables" / "formal_language_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "formal_language_audit_summary.csv", [summary])
    write_json(article_root / "outputs" / "json" / "formal_language_audit.json", rows)
    write_json(article_root / "outputs" / "json" / "formal_language_audit_summary.json", summary)


if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
