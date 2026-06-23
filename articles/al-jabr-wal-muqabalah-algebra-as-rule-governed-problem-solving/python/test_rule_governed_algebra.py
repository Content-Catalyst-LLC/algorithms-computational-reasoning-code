from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import al_jabr_wal_muqabalah_rule_governed_algebra_map as algebra


def test_core_threads_include_restoration_balancing_and_square_completion() -> None:
    config = algebra.AlgebraProcedureConfig()
    scored = [algebra.score_theme(row, config) for row in algebra.algebraic_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_rule_governed_algebra_thread"}
    assert "restoration_al_jabr" in core
    assert "balancing_al_muqabalah" in core
    assert "completing_the_square" in core


def test_scores_are_bounded() -> None:
    config = algebra.AlgebraProcedureConfig()
    row = algebra.score_theme(algebra.algebraic_themes()[0], config)
    assert 0.0 <= row["procedure_score"] <= 1.0


def test_cautions_include_symbolic_projection_and_single_origin() -> None:
    cautions = {row["caution"] for row in algebra.interpretation_cautions()}
    assert "do_not_project_symbolic_notation_backward" in cautions
    assert "do_not_claim_single_origin" in cautions


def main() -> None:
    test_core_threads_include_restoration_balancing_and_square_completion()
    test_scores_are_bounded()
    test_cautions_include_symbolic_projection_and_single_origin()
    print("All rule-governed algebra tests passed.")


if __name__ == "__main__":
    main()
