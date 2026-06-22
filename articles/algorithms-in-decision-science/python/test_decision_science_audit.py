from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_decision_science_audit as audit


def test_decision_science_detects_non_automation_case() -> None:
    config = audit.DecisionScienceConfig()
    rows = [audit.score_decision(row, config) for row in audit.candidate_decisions()]
    assert any(row["recommendation"] == "do_not_automate_action" for row in rows)


def test_scores_have_expected_ranges() -> None:
    config = audit.DecisionScienceConfig()
    row = audit.score_decision(audit.candidate_decisions()[0], config)
    assert 0.0 <= row["predicted_probability"] <= 1.0
    assert 0.0 <= row["decision_support_readiness_score"] <= 1.0
    assert row["recommendation"] in {
        "monitor_or_defer",
        "support_action_with_review",
        "escalate_to_human_review",
        "do_not_automate_action",
        "review_despite_below_threshold",
    }


def test_governance_register_has_threshold_rationale() -> None:
    rows = audit.decision_governance_register()
    assert any(row["control"] == "threshold_rationale" for row in rows)


def main() -> None:
    test_decision_science_detects_non_automation_case()
    test_scores_have_expected_ranges()
    test_governance_register_has_threshold_rationale()
    print("All algorithms in decision science tests passed.")


if __name__ == "__main__":
    main()
