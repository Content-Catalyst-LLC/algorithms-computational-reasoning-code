from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import al_khwarizmi_algorism_procedural_legacy_map as legacy


def test_core_threads_include_name_algorism_and_algebra() -> None:
    config = legacy.ProceduralLegacyConfig()
    scored = [legacy.score_theme(row, config) for row in legacy.legacy_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_procedural_legacy"}
    assert "name_to_algorithm" in core
    assert "algorism_written_arithmetic" in core
    assert "algebraic_restoration_balancing" in core


def test_scores_are_bounded() -> None:
    config = legacy.ProceduralLegacyConfig()
    row = legacy.score_theme(legacy.legacy_themes()[0], config)
    assert 0.0 <= row["legacy_score"] <= 1.0


def test_cautions_include_single_invention_and_modern_projection() -> None:
    cautions = {row["caution"] for row in legacy.interpretation_cautions()}
    assert "do_not_claim_single_invention" in cautions
    assert "do_not_project_modern_code_backwards" in cautions


def main() -> None:
    test_core_threads_include_name_algorism_and_algebra()
    test_scores_are_bounded()
    test_cautions_include_single_invention_and_modern_projection()
    print("All al-Khwārizmī procedural legacy tests passed.")


if __name__ == "__main__":
    main()
