from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import automated_reasoning_symbolic_ai_hybrid_systems_audit as audit


def test_inference_derives_expected_conclusions() -> None:
    known, trace = audit.infer(audit.facts(), audit.rules())
    assert "traceable_system" in known
    assert "reviewable_system" in known
    assert "hybrid_system" in known
    assert "requires_escalation_review" in known
    assert "conditionally_approvable" in known
    assert len(trace) == 5


def test_contradiction_checks_have_expected_shape() -> None:
    known, _ = audit.infer(audit.facts(), audit.rules())
    checks = audit.contradiction_checks(known)
    assert len(checks) >= 3
    assert all("conflict_detected" in row for row in checks)


def test_constraints_are_all_satisfied_for_reference_case() -> None:
    known, _ = audit.infer(audit.facts(), audit.rules())
    constraints = audit.constraint_review(known)
    assert all(int(row["satisfied"]) == 1 for row in constraints)


def main() -> None:
    test_inference_derives_expected_conclusions()
    test_contradiction_checks_have_expected_shape()
    test_constraints_are_all_satisfied_for_reference_case()
    print("All symbolic reasoning tests passed.")


if __name__ == "__main__":
    main()
