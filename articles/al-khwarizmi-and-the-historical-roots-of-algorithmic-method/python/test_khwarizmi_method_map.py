from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import al_khwarizmi_algorithmic_method_map as khwarizmi


def test_core_threads_include_algorism_algebra_reception() -> None:
    config = khwarizmi.KhwarizmiMethodConfig()
    scored = [khwarizmi.score_theme(row, config) for row in khwarizmi.khwarizmi_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_khwarizmi_algorithmic_method_thread"}
    assert "algorism_written_calculation" in core
    assert "algebra_case_based_method" in core
    assert "latin_reception_word_algorithm" in core


def test_scores_are_bounded() -> None:
    config = khwarizmi.KhwarizmiMethodConfig()
    row = khwarizmi.score_theme(khwarizmi.khwarizmi_themes()[0], config)
    assert 0.0 <= row["method_score"] <= 1.0


def test_cautions_include_no_invented_all_algorithms() -> None:
    cautions = {row["caution"] for row in khwarizmi.interpretation_cautions()}
    assert "do_not_claim_al_khwarizmi_invented_all_algorithms" in cautions
    assert "do_not_project_modern_code_backward" in cautions


def main() -> None:
    test_core_threads_include_algorism_algebra_reception()
    test_scores_are_bounded()
    test_cautions_include_no_invented_all_algorithms()
    print("All al-Khwārizmī method tests passed.")


if __name__ == "__main__":
    main()
