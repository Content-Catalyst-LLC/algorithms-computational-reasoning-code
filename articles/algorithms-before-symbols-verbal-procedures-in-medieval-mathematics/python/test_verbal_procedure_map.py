from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algorithms_before_symbols_verbal_procedure_map as verbal


def test_core_threads_include_rhetorical_algebra_examples_and_classification() -> None:
    config = verbal.VerbalProcedureConfig()
    scored = [verbal.score_theme(row, config) for row in verbal.verbal_procedure_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_verbal_procedure_thread"}
    assert "rhetorical_algebra" in core
    assert "problem_classification" in core
    assert "worked_examples" in core


def test_scores_are_bounded() -> None:
    config = verbal.VerbalProcedureConfig()
    row = verbal.score_theme(verbal.verbal_procedure_themes()[0], config)
    assert 0.0 <= row["verbal_procedure_score"] <= 1.0


def test_cautions_include_verbal_not_vague_and_not_code() -> None:
    cautions = {row["caution"] for row in verbal.interpretation_cautions()}
    assert "do_not_confuse_verbal_with_vague" in cautions
    assert "do_not_equate_procedure_with_programming" in cautions


def main() -> None:
    test_core_threads_include_rhetorical_algebra_examples_and_classification()
    test_scores_are_bounded()
    test_cautions_include_verbal_not_vague_and_not_code()
    print("All verbal procedure map tests passed.")


if __name__ == "__main__":
    main()
