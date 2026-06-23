from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ada_lovelace_computation_imagination_map as lovelace


def test_core_threads_include_note_g_engine_computation_beyond_arithmetic() -> None:
    config = lovelace.LovelaceConfig()
    scored = [lovelace.score_theme(row, config) for row in lovelace.lovelace_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_lovelace_computation_thread"}
    assert "note_g_bernoulli_procedure" in core
    assert "analytical_engine_general_machine" in core
    assert "computation_beyond_arithmetic" in core


def test_scores_are_bounded() -> None:
    config = lovelace.LovelaceConfig()
    row = lovelace.score_theme(lovelace.lovelace_themes()[0], config)
    assert 0.0 <= row["imagination_score"] <= 1.0


def test_cautions_include_no_modern_software_projection() -> None:
    cautions = {row["caution"] for row in lovelace.interpretation_cautions()}
    assert "do_not_project_modern_software_backward" in cautions
    assert "do_not_overstate_machine_agency" in cautions


def main() -> None:
    test_core_threads_include_note_g_engine_computation_beyond_arithmetic()
    test_scores_are_bounded()
    test_cautions_include_no_modern_software_projection()
    print("All Lovelace computation-imagination tests passed.")


if __name__ == "__main__":
    main()
