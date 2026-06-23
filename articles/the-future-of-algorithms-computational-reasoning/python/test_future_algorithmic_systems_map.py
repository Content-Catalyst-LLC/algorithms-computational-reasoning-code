from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import future_algorithmic_systems_map as future


def test_high_risk_governance_gaps_include_agents_and_public_policy() -> None:
    config = future.FutureAlgorithmsConfig()
    scored = [future.score_domain(row, config) for row in future.future_domains()]
    gaps = {row["domain_id"] for row in scored if row["future_status"] == "high_risk_governance_gap"}
    assert "ai_agents_and_tool_use" in gaps
    assert "public_policy_algorithmic_governance" in gaps


def test_future_cautions_include_capability_and_governance() -> None:
    cautions = {row["caution"] for row in future.future_cautions()}
    assert "do_not_confuse_capability_with_readiness" in cautions
    assert "do_not_automate_when_governance_is_absent" in cautions


def test_no_go_flag() -> None:
    assert future.no_go_flag(False, False, False, False, False) is False
    assert future.no_go_flag(False, True, False, False, False) is True
    assert future.no_go_flag(False, False, True, True, True) is True


def main() -> None:
    test_high_risk_governance_gaps_include_agents_and_public_policy()
    test_future_cautions_include_capability_and_governance()
    test_no_go_flag()
    print("All future algorithmic systems tests passed.")


if __name__ == "__main__":
    main()
