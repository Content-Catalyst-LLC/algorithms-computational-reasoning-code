from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import grace_hopper_compiler_humanization_map as hopper


def test_core_threads_include_compiler_flowmatic_cobol() -> None:
    config = hopper.HopperConfig()
    scored = [hopper.score_theme(row, config) for row in hopper.hopper_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_hopper_compiler_humanization_thread"}
    assert "compiler_as_bridge" in core
    assert "flow_matic_english_like_programming" in core
    assert "cobol_business_computation" in core


def test_scores_are_bounded() -> None:
    config = hopper.HopperConfig()
    row = hopper.score_theme(hopper.hopper_themes()[0], config)
    assert 0.0 <= row["humanization_score"] <= 1.0


def test_cautions_include_ai_code_generation() -> None:
    cautions = {row["caution"] for row in hopper.interpretation_cautions()}
    assert "do_not_confuse_compilers_with_ai_code_generation" in cautions
    assert "do_not_treat_humanization_as_lack_of_rigor" in cautions


def main() -> None:
    test_core_threads_include_compiler_flowmatic_cobol()
    test_scores_are_bounded()
    test_cautions_include_ai_code_generation()
    print("All Hopper compiler-humanization tests passed.")


if __name__ == "__main__":
    main()
