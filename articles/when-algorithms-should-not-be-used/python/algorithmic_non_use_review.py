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
class NonUseConfig:
    article: str = "when_algorithms_should_not_be_used"
    high_non_use_pressure_threshold: float = 0.70
    low_responsible_readiness_threshold: float = 0.65
    critical_stakes_threshold: float = 0.85


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


def candidate_use_cases() -> list[dict[str, object]]:
    return [
        {"use_case": "automated_benefits_denial", "target_legitimacy": 0.42, "data_legitimacy": 0.48, "contestability": 0.40, "human_judgment": 0.46, "governance_capacity": 0.44, "repairability": 0.38, "stakes": 0.94, "irreversibility": 0.78, "proxy_illegitimacy": 0.70},
        {"use_case": "routine_document_routing", "target_legitimacy": 0.86, "data_legitimacy": 0.82, "contestability": 0.78, "human_judgment": 0.72, "governance_capacity": 0.76, "repairability": 0.90, "stakes": 0.24, "irreversibility": 0.10, "proxy_illegitimacy": 0.12},
        {"use_case": "student_potential_score", "target_legitimacy": 0.30, "data_legitimacy": 0.44, "contestability": 0.42, "human_judgment": 0.48, "governance_capacity": 0.46, "repairability": 0.36, "stakes": 0.86, "irreversibility": 0.72, "proxy_illegitimacy": 0.82},
        {"use_case": "clinical_triage_support", "target_legitimacy": 0.76, "data_legitimacy": 0.72, "contestability": 0.70, "human_judgment": 0.84, "governance_capacity": 0.78, "repairability": 0.74, "stakes": 0.96, "irreversibility": 0.56, "proxy_illegitimacy": 0.30},
    ]


def score_use_case(row: dict[str, object], config: NonUseConfig) -> dict[str, object]:
    readiness = mean([
        float(row["target_legitimacy"]),
        float(row["data_legitimacy"]),
        float(row["contestability"]),
        float(row["human_judgment"]),
        float(row["governance_capacity"]),
        float(row["repairability"]),
    ])
    governance_weakness = 1.0 - float(row["governance_capacity"])
    non_use_pressure = mean([
        float(row["stakes"]),
        float(row["irreversibility"]),
        governance_weakness,
        float(row["proxy_illegitimacy"]),
    ])

    recommendation = "allow_with_governance_controls"
    if (
        non_use_pressure >= config.high_non_use_pressure_threshold
        and readiness < config.low_responsible_readiness_threshold
    ):
        recommendation = "do_not_use_algorithm"
    elif float(row["stakes"]) >= config.critical_stakes_threshold and readiness < config.low_responsible_readiness_threshold:
        recommendation = "human_led_or_refuse"
    elif float(row["stakes"]) >= config.critical_stakes_threshold:
        recommendation = "support_only_with_strong_review"
    elif readiness >= 0.75 and non_use_pressure < 0.40:
        recommendation = "limited_algorithmic_support_acceptable"

    status = "pass"
    if recommendation in {"support_only_with_strong_review", "human_led_or_refuse"}:
        status = "review"
    if recommendation == "do_not_use_algorithm":
        status = "refuse"

    return {
        "use_case": row["use_case"],
        "target_legitimacy": round(float(row["target_legitimacy"]), 6),
        "data_legitimacy": round(float(row["data_legitimacy"]), 6),
        "contestability": round(float(row["contestability"]), 6),
        "human_judgment": round(float(row["human_judgment"]), 6),
        "governance_capacity": round(float(row["governance_capacity"]), 6),
        "repairability": round(float(row["repairability"]), 6),
        "stakes": round(float(row["stakes"]), 6),
        "irreversibility": round(float(row["irreversibility"]), 6),
        "proxy_illegitimacy": round(float(row["proxy_illegitimacy"]), 6),
        "responsible_use_readiness_score": round(readiness, 6),
        "non_use_pressure_score": round(non_use_pressure, 6),
        "recommendation": recommendation,
        "status": status,
    }


def non_use_register() -> list[dict[str, str]]:
    return [
        {"criterion": "inappropriate_target", "review_question": "Is the thing being predicted or optimized legitimate?", "status": "required"},
        {"criterion": "illegitimate_proxy", "review_question": "Do available variables substitute for something they cannot responsibly measure?", "status": "required"},
        {"criterion": "high_irreparable_stakes", "review_question": "Could errors cause serious harm that cannot be repaired?", "status": "required"},
        {"criterion": "weak_contestability", "review_question": "Can affected people understand, challenge, and correct outcomes?", "status": "required"},
        {"criterion": "governance_gap", "review_question": "Can the institution monitor, audit, pause, rollback, and retire the system?", "status": "required"},
        {"criterion": "human_judgment_required", "review_question": "Does the decision require context, care, dialogue, or democratic legitimacy?", "status": "required"},
    ]


def main() -> None:
    config = NonUseConfig()
    use_cases = candidate_use_cases()
    audit = [score_use_case(row, config) for row in use_cases]
    register = non_use_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "use_cases_reviewed": len(audit),
        "use_cases_passed": sum(1 for row in audit if row["status"] == "pass"),
        "use_cases_requiring_review": sum(1 for row in audit if row["status"] == "review"),
        "use_cases_refused": sum(1 for row in audit if row["status"] == "refuse"),
        "mean_responsible_use_readiness_score": round(mean(float(row["responsible_use_readiness_score"]) for row in audit), 6),
        "mean_non_use_pressure_score": round(mean(float(row["non_use_pressure_score"]) for row in audit), 6),
        "non_use_criteria": len(register),
        "interpretation": "Algorithmic non-use review should connect target legitimacy, data legitimacy, contestability, human judgment, governance capacity, repairability, stakes, irreversibility, and proxy legitimacy.",
    }

    write_csv(TABLES / "candidate_use_cases.csv", use_cases)
    write_csv(TABLES / "algorithmic_non_use_audit.csv", audit)
    write_csv(TABLES / "algorithmic_non_use_register.csv", register)
    write_csv(TABLES / "algorithmic_non_use_summary.csv", [summary])

    write_json(JSON_DIR / "algorithmic_non_use_config.json", asdict(config))
    write_json(JSON_DIR / "algorithmic_non_use_audit.json", audit)
    write_json(JSON_DIR / "algorithmic_non_use_register.json", register)
    write_json(JSON_DIR / "algorithmic_non_use_summary.json", summary)

    print("Algorithmic non-use review complete.")
    print(TABLES / "algorithmic_non_use_summary.csv")


if __name__ == "__main__":
    main()
