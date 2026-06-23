from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import donald_knuth_art_of_computer_programming_map as knuth


def test_core_threads_include_taocp_analysis_literate() -> None:
    config = knuth.KnuthConfig()
    scored = [knuth.score_theme(row, config) for row in knuth.knuth_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_knuth_algorithmic_art_thread"}
    assert "art_of_computer_programming" in core
    assert "analysis_of_algorithms" in core
    assert "literate_programming_web_cweb" in core


def test_sort_lower_bound_positive() -> None:
    assert knuth.comparison_sort_lower_bound(4) > 0
    assert knuth.comparison_sort_lower_bound(1) == 0


def test_cautions_include_generated_code() -> None:
    cautions = {row["caution"] for row in knuth.interpretation_cautions()}
    assert "do_not_confuse_code_generation_with_understanding" in cautions
    assert "do_not_skip_exposition" in cautions


def main() -> None:
    test_core_threads_include_taocp_analysis_literate()
    test_sort_lower_bound_positive()
    test_cautions_include_generated_code()
    print("All Knuth algorithmic-art tests passed.")


if __name__ == "__main__":
    main()
