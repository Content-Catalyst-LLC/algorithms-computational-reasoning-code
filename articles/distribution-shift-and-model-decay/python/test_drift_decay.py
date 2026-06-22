from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distribution_shift_model_decay_audit as audit


def test_decay_audit_detects_escalations() -> None:
    config = audit.DriftDecayConfig()
    snapshots = audit.deployment_snapshots()
    baseline = snapshots[0]
    rows = [audit.audit_snapshot(row, baseline, config) for row in snapshots]
    assert any(row["status"] == "escalate" for row in rows)


def test_performance_decay_is_baseline_minus_current() -> None:
    config = audit.DriftDecayConfig()
    snapshots = audit.deployment_snapshots()
    row = audit.audit_snapshot(snapshots[2], snapshots[0], config)
    assert abs(row["performance_decay"] - (snapshots[0]["accuracy"] - snapshots[2]["accuracy"])) < 1e-9


def test_governance_register_has_rollback_plan() -> None:
    rows = audit.governance_register()
    assert any(row["item"] == "rollback_plan" for row in rows)


def main() -> None:
    test_decay_audit_detects_escalations()
    test_performance_decay_is_baseline_minus_current()
    test_governance_register_has_rollback_plan()
    print("All drift and decay tests passed.")


if __name__ == "__main__":
    main()
