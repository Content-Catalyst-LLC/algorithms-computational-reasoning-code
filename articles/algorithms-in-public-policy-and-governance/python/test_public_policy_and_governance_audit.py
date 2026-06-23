from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_public_policy_and_governance_audit as audit


def test_detects_due_process_redesign_cases() -> None:
    config = audit.PublicGovernanceConfig()
    rows = [audit.score_use_case(row, config) for row in audit.public_algorithm_use_cases()]
    assert any(row["recommendation"] == "do_not_deploy_without_due_process_redesign" for row in rows)


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.PublicGovernanceConfig()
    row = audit.score_use_case(audit.public_algorithm_use_cases()[0], config)
    assert 0.0 <= row["procedural_readiness_score"] <= 1.0
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert row["public_algorithmic_risk_score"] >= 0.0


def test_register_has_due_process_plan() -> None:
    rows = audit.governance_register()
    assert any(row["control"] == "due_process_plan" for row in rows)


def main() -> None:
    test_detects_due_process_redesign_cases()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_due_process_plan()
    print("All algorithms in public policy and governance tests passed.")


if __name__ == "__main__":
    main()
