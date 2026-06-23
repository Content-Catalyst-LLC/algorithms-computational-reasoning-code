from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_in_media_platforms_and_attention_systems_audit as audit


def test_detects_redesign_case() -> None:
    config = audit.AttentionSystemConfig()
    rows = [audit.score_system(row, config) for row in audit.platform_systems()]
    assert any(row["recommendation"] == "redesign_before_scaling" for row in rows)


def test_scores_are_bounded_or_nonnegative() -> None:
    config = audit.AttentionSystemConfig()
    row = audit.score_system(audit.platform_systems()[0], config)
    assert 0.0 <= row["governance_readiness_score"] <= 1.0
    assert 0.0 <= row["attention_risk_score"] <= 1.0
    assert row["platform_risk_score"] >= 0.0


def test_register_has_appeals_control() -> None:
    rows = audit.platform_governance_register()
    assert any(row["control"] == "contestability_and_appeals" for row in rows)


def main() -> None:
    test_detects_redesign_case()
    test_scores_are_bounded_or_nonnegative()
    test_register_has_appeals_control()
    print("All media platforms and attention systems tests passed.")


if __name__ == "__main__":
    main()
