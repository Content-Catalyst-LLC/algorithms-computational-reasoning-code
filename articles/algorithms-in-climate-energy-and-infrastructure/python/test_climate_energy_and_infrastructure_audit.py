from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_climate_energy_and_infrastructure_audit as audit


def test_detects_reliability_and_climate_equity_reviews() -> None:
    config = audit.InfrastructureAlgorithmConfig()
    rows = [audit.score_system(row, config) for row in audit.infrastructure_systems()]
    recommendations = {row["recommendation"] for row in rows}
    assert "reliability_and_safety_review_required" in recommendations
    assert "climate_equity_review_required" in recommendations


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.InfrastructureAlgorithmConfig()
    row = audit.score_system(audit.infrastructure_systems()[0], config)
    assert 0.0 <= row["governance_score"] <= 1.0
    assert 0.0 <= row["resilience_risk_score"] <= 1.0
    assert row["impact_score"] >= 0.0


def test_register_has_uncertainty_review() -> None:
    rows = audit.infrastructure_governance_register()
    assert any(row["control"] == "uncertainty_and_scenario_review" for row in rows)


def main() -> None:
    test_detects_reliability_and_climate_equity_reviews()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_uncertainty_review()
    print("All climate, energy, and infrastructure tests passed.")


if __name__ == "__main__":
    main()
