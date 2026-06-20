# identity_access_calculator.py
# Educational calculator for identity and access governance scoring.

from __future__ import annotations

import csv
from pathlib import Path

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUT = ARTICLE_ROOT / "calculators" / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

WEIGHTS = {
    "authentication_strength": 0.10,
    "authorization_granularity": 0.11,
    "least_privilege_alignment": 0.11,
    "session_token_control": 0.09,
    "machine_identity_governance": 0.09,
    "audit_logging": 0.10,
    "access_lifecycle_review": 0.09,
    "privilege_escalation_controls": 0.09,
    "privacy_and_inclusion_review": 0.08,
    "incident_response": 0.06,
    "governance_ownership": 0.06,
    "communication_clarity": 0.02,
}

SCENARIOS = [
    {
        "scenario": "mature_identity_governance",
        "authentication_strength": 0.88,
        "authorization_granularity": 0.84,
        "least_privilege_alignment": 0.80,
        "session_token_control": 0.82,
        "machine_identity_governance": 0.78,
        "audit_logging": 0.90,
        "access_lifecycle_review": 0.82,
        "privilege_escalation_controls": 0.80,
        "privacy_and_inclusion_review": 0.76,
        "incident_response": 0.82,
        "governance_ownership": 0.84,
        "communication_clarity": 0.78,
    },
    {
        "scenario": "legacy_overprivileged_access",
        "authentication_strength": 0.36,
        "authorization_granularity": 0.24,
        "least_privilege_alignment": 0.20,
        "session_token_control": 0.28,
        "machine_identity_governance": 0.18,
        "audit_logging": 0.30,
        "access_lifecycle_review": 0.22,
        "privilege_escalation_controls": 0.20,
        "privacy_and_inclusion_review": 0.30,
        "incident_response": 0.28,
        "governance_ownership": 0.24,
        "communication_clarity": 0.34,
    },
]


def score(row: dict[str, float]) -> float:
    return round(100.0 * sum(float(row[k]) * w for k, w in WEIGHTS.items()), 3)


def risk(row: dict[str, float]) -> float:
    weak = [1.0 - float(row[k]) for k in WEIGHTS if k != "communication_clarity"]
    return round(100.0 * sum(weak) / len(weak), 3)


def main() -> None:
    rows = []
    for item in SCENARIOS:
        calculated = dict(item)
        calculated["identity_access_score"] = score(item)
        calculated["identity_access_risk"] = risk(item)
        rows.append(calculated)

    path = OUT / "identity_access_calculator_results.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
