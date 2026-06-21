from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ai_agents_tool_use_procedural_autonomy_audit as audit


def test_tool_registry_contains_high_risk_write_actions() -> None:
    registry = audit.tool_registry()
    tools = {row["tool"]: row for row in registry}
    assert tools["email_send"]["approval_required"] == 1
    assert tools["database_update"]["risk"] >= 0.85
    assert tools["shell_command"]["permission_scope"] == "blocked_by_default"


def test_audit_blocks_unapproved_high_risk_actions() -> None:
    config = audit.AgentAuditConfig()
    rows = audit.audit_actions(config)
    blocked = [row for row in rows if row["status"] == "blocked"]
    assert blocked
    assert any(row["tool"] == "email_send" for row in blocked)
    assert any(row["approval_violation"] == 1 for row in blocked)


def test_autonomy_profile_recommends_supervision_when_blocked() -> None:
    rows = audit.audit_actions(audit.AgentAuditConfig())
    profile = audit.autonomy_profile(rows)
    assert profile["blocked_actions"] >= 1
    assert profile["autonomy_recommendation"] == "supervised_action_only"


def main() -> None:
    test_tool_registry_contains_high_risk_write_actions()
    test_audit_blocks_unapproved_high_risk_actions()
    test_autonomy_profile_recommends_supervision_when_blocked()
    print("All agent tool-use tests passed.")


if __name__ == "__main__":
    main()
