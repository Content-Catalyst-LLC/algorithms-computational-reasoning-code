from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_health_care_and_public_health_audit as audit


def test_detects_clinical_public_health_and_equity_reviews() -> None:
    config = audit.HealthAlgorithmConfig()
    rows = [audit.score_system(row, config) for row in audit.health_systems()]
    recommendations = {row["recommendation"] for row in rows}
    assert "clinical_safety_review_required" in recommendations
    assert "public_health_governance_review_required" in recommendations
    assert "health_equity_review_required" in recommendations


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.HealthAlgorithmConfig()
    row = audit.score_system(audit.health_systems()[0], config)
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert 0.0 <= row["health_algorithm_risk_score"] <= 1.0
    assert row["impact_score"] >= 0.0


def test_register_has_privacy_review() -> None:
    rows = audit.health_governance_register()
    assert any(row["control"] == "privacy_and_security_review" for row in rows)


def main() -> None:
    test_detects_clinical_public_health_and_equity_reviews()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_privacy_review()
    print("All health care and public health tests passed.")


if __name__ == "__main__":
    main()
