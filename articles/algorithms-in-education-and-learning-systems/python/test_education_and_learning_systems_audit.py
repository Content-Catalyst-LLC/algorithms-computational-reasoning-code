from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_education_and_learning_systems_audit as audit


def test_detects_pedagogical_student_and_equity_reviews() -> None:
    config = audit.LearningSystemConfig()
    rows = [audit.score_system(row, config) for row in audit.learning_systems()]
    recommendations = {row["recommendation"] for row in rows}
    assert "pedagogical_validity_review_required" in recommendations
    assert "student_impact_review_required" in recommendations
    assert "educational_equity_review_required" in recommendations


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.LearningSystemConfig()
    row = audit.score_system(audit.learning_systems()[0], config)
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert 0.0 <= row["learning_system_risk_score"] <= 1.0
    assert row["impact_score"] >= 0.0


def test_register_has_privacy_and_accessibility_review() -> None:
    rows = audit.learning_governance_register()
    controls = {row["control"] for row in rows}
    assert "student_privacy_review" in controls
    assert "accessibility_review" in controls


def main() -> None:
    test_detects_pedagogical_student_and_equity_reviews()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_privacy_and_accessibility_review()
    print("All education and learning systems tests passed.")


if __name__ == "__main__":
    main()
