from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import baghdad_latin_europe_algorism_algebra_reception_map as reception


def test_core_threads_include_algorism_algebra_numerals() -> None:
    config = reception.ReceptionConfig()
    scored = [reception.score_theme(row, config) for row in reception.reception_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_algorism_algebra_reception_thread"}
    assert "algorism_written_arithmetic" in core
    assert "algebra_rule_governed_problem_solving" in core
    assert "hindu_arabic_numerals_place_value_zero" in core


def test_scores_are_bounded() -> None:
    config = reception.ReceptionConfig()
    row = reception.score_theme(reception.reception_themes()[0], config)
    assert 0.0 <= row["reception_score"] <= 1.0


def test_cautions_include_not_fibonacci_only_and_not_etymology_only() -> None:
    cautions = {row["caution"] for row in reception.interpretation_cautions()}
    assert "do_not_claim_fibonacci_singlehandedly_introduced_numerals" in cautions
    assert "do_not_reduce_algorithm_to_etymology" in cautions


def main() -> None:
    test_core_threads_include_algorism_algebra_numerals()
    test_scores_are_bounded()
    test_cautions_include_not_fibonacci_only_and_not_etymology_only()
    print("All algorism, algebra, and reception tests passed.")


if __name__ == "__main__":
    main()
