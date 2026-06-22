from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_systems_modeling_audit as audit


def test_systems_modeling_detects_escalation() -> None:
    config = audit.SystemsModelingConfig()
    rows = [audit.score_scenario(row, config) for row in audit.system_scenarios()]
    assert any(row["recommendation"] == "stress_test_and_escalate" for row in rows)


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.SystemsModelingConfig()
    row = audit.score_scenario(audit.system_scenarios()[0], config)
    assert 0.0 <= row["system_vulnerability_score"] <= 1.0
    assert 0.0 <= row["model_readiness_score"] <= 1.0
    assert row["system_modeling_risk_score"] >= 0.0


def test_register_has_boundary_statement() -> None:
    rows = audit.systems_modeling_register()
    assert any(row["control"] == "boundary_statement" for row in rows)


def main() -> None:
    test_systems_modeling_detects_escalation()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_boundary_statement()
    print("All algorithms in systems modeling tests passed.")


if __name__ == "__main__":
    main()
