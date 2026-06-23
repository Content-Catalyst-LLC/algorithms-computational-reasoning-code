from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import alonzo_church_lambda_calculus_map as church


def test_core_threads_include_lambda_effective_undecidability() -> None:
    config = church.ChurchConfig()
    scored = [church.score_theme(row, config) for row in church.church_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_church_formal_computation_thread"}
    assert "lambda_calculus_core" in core
    assert "effective_calculability" in core
    assert "entscheidungsproblem_undecidability" in core
    assert "church_turing_convergence" in core


def test_scores_are_bounded() -> None:
    config = church.ChurchConfig()
    row = church.score_theme(church.church_themes()[0], config)
    assert 0.0 <= row["formal_score"] <= 1.0


def test_cautions_include_binding_and_thesis() -> None:
    cautions = {row["caution"] for row in church.interpretation_cautions()}
    assert "do_not_ignore_binding_and_scope" in cautions
    assert "do_not_treat_church_turing_thesis_as_simple_theorem" in cautions


def main() -> None:
    test_core_threads_include_lambda_effective_undecidability()
    test_scores_are_bounded()
    test_cautions_include_binding_and_thesis()
    print("All Church formal-computation tests passed.")


if __name__ == "__main__":
    main()
