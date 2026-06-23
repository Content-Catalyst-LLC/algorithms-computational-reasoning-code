from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_labor_management_and_organizational_systems_audit as audit


def test_detects_core_workplace_reviews() -> None:
    config = audit.WorkplaceAlgorithmConfig()
    rows = [audit.score_system(row, config) for row in audit.workplace_systems()]
    recommendations = {row["recommendation"] for row in rows}
    assert "contestability_and_appeal_review_required" in recommendations
    assert "workplace_privacy_review_required" in recommendations
    assert "workplace_equity_review_required" in recommendations
    assert "worker_impact_review_required" in recommendations


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.WorkplaceAlgorithmConfig()
    row = audit.score_system(audit.workplace_systems()[0], config)
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert 0.0 <= row["workplace_algorithm_risk_score"] <= 1.0
    assert row["impact_score"] >= 0.0


def test_register_has_contestability_and_privacy() -> None:
    rows = audit.workplace_governance_register()
    controls = {row["control"] for row in rows}
    assert "contestability_and_appeal" in controls
    assert "privacy_and_surveillance_review" in controls


def main() -> None:
    test_detects_core_workplace_reviews()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_contestability_and_privacy()
    print("All labor, management, and organizational systems tests passed.")


if __name__ == "__main__":
    main()
