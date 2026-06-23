from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import banu_musa_mechanical_procedure_map as mech


def test_core_threads_include_valves_timing_hydraulics() -> None:
    config = mech.MechanicalProcedureConfig()
    scored = [mech.score_theme(row, config) for row in mech.mechanical_procedure_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_mechanical_procedure_thread"}
    assert "valves_floats_thresholds" in core
    assert "sequencing_and_timing" in core
    assert "hydraulic_material_logic" in core


def test_scores_are_bounded() -> None:
    config = mech.MechanicalProcedureConfig()
    row = mech.score_theme(mech.mechanical_procedure_themes()[0], config)
    assert 0.0 <= row["mechanical_score"] <= 1.0


def test_cautions_include_not_modern_robots_and_material_constraints() -> None:
    cautions = {row["caution"] for row in mech.interpretation_cautions()}
    assert "do_not_call_the_devices_modern_robots" in cautions
    assert "do_not_ignore_material_constraints" in cautions


def main() -> None:
    test_core_threads_include_valves_timing_hydraulics()
    test_scores_are_bounded()
    test_cautions_include_not_modern_robots_and_material_constraints()
    print("All mechanical procedure tests passed.")


if __name__ == "__main__":
    main()
