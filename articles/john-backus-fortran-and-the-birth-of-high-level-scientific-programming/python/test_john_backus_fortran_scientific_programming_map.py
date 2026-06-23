from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import john_backus_fortran_scientific_programming_map as backus


def test_core_threads_include_formula_compiler_hpc() -> None:
    config = backus.BackusConfig()
    scored = [backus.score_theme(row, config) for row in backus.backus_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_backus_fortran_scientific_programming_thread"}
    assert "formula_translation" in core
    assert "ibm_704_fortran_compiler" in core
    assert "fortran_scientific_computing_hpc" in core


def test_formula_translation_example() -> None:
    assert backus.formula_translation_example(2, 2, -3, 1) == 3
    assert backus.formula_translation_example(0, 2, -3, 1) == 1


def test_cautions_include_optimization_and_ai_review() -> None:
    cautions = {row["caution"] for row in backus.interpretation_cautions()}
    assert "do_not_ignore_optimization" in cautions
    assert "do_not_trust_generated_code_without_translation_review" in cautions


def main() -> None:
    test_core_threads_include_formula_compiler_hpc()
    test_formula_translation_example()
    test_cautions_include_optimization_and_ai_review()
    print("All Backus/FORTRAN scientific-programming tests passed.")


if __name__ == "__main__":
    main()
