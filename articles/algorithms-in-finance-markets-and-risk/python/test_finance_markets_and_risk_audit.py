from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_finance_markets_and_risk_audit as audit


def test_detects_consumer_and_market_review_cases() -> None:
    config = audit.FinancialAlgorithmConfig()
    rows = [audit.score_system(row, config) for row in audit.financial_systems()]
    recommendations = {row["recommendation"] for row in rows}
    assert "consumer_protection_review_required" in recommendations
    assert "market_stability_review_required" in recommendations


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.FinancialAlgorithmConfig()
    row = audit.score_system(audit.financial_systems()[0], config)
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert 0.0 <= row["financial_algorithm_risk_score"] <= 1.0
    assert row["impact_score"] >= 0.0


def test_register_has_validation_report() -> None:
    rows = audit.financial_governance_register()
    assert any(row["control"] == "validation_report" for row in rows)


def main() -> None:
    test_detects_consumer_and_market_review_cases()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_validation_report()
    print("All finance, markets, and risk tests passed.")


if __name__ == "__main__":
    main()
