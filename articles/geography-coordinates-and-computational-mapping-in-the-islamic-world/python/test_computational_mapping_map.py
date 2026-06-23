from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import geography_coordinates_computational_mapping_map as mapping


def test_core_threads_include_coordinates_al_khwarizmi_qibla() -> None:
    config = mapping.ComputationalMappingConfig()
    scored = [mapping.score_theme(row, config) for row in mapping.computational_mapping_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_computational_mapping_thread"}
    assert "coordinates_as_spatial_data" in core
    assert "al_khwarizmi_geographical_tables" in core
    assert "qibla_and_directional_calculation" in core


def test_scores_are_bounded() -> None:
    config = mapping.ComputationalMappingConfig()
    row = mapping.score_theme(mapping.computational_mapping_themes()[0], config)
    assert 0.0 <= row["mapping_score"] <= 1.0


def test_cautions_include_maps_not_mirrors_and_not_modern_gis() -> None:
    cautions = {row["caution"] for row in mapping.interpretation_cautions()}
    assert "do_not_treat_maps_as_mirrors" in cautions
    assert "do_not_project_modern_gis_backward" in cautions


def main() -> None:
    test_core_threads_include_coordinates_al_khwarizmi_qibla()
    test_scores_are_bounded()
    test_cautions_include_maps_not_mirrors_and_not_modern_gis()
    print("All computational mapping tests passed.")


if __name__ == "__main__":
    main()
