from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import programming_language_history_map as history


def test_core_threads_include_fortran_c_sql_ai() -> None:
    config = history.LanguageHistoryConfig()
    scored = [history.score_tradition(row, config) for row in history.language_traditions()]
    core = {row["tradition_id"] for row in scored if row["interpretive_status"] == "core_programming_language_history_thread"}
    assert "fortran_scientific_programming" in core
    assert "c_systems_programming" in core
    assert "sql_database_languages" in core
    assert "ai_generated_code_layer" in core


def test_cautions_include_progress_and_ai() -> None:
    cautions = {row["caution"] for row in history.interpretation_cautions()}
    assert "do_not_treat_language_history_as_progress_only" in cautions
    assert "do_not_treat_ai_code_generation_as_the_end_of_languages" in cautions


def test_language_family_edges_exist() -> None:
    edges = history.language_family_edges()
    assert len(edges) >= 5
    assert any(edge["target"] == "ai_generated_code_layer" for edge in edges)


def main() -> None:
    test_core_threads_include_fortran_c_sql_ai()
    test_cautions_include_progress_and_ai()
    test_language_family_edges_exist()
    print("All programming-language history tests passed.")


if __name__ == "__main__":
    main()
