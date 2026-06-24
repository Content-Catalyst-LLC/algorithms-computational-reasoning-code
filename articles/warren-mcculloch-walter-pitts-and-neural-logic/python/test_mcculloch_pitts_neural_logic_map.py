from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mcculloch_pitts_neural_logic_map as nl


def test_threshold_logic_and_or() -> None:
    assert nl.threshold_unit([1, 1], [1, 1], 2) == 1
    assert nl.threshold_unit([1, 0], [1, 1], 2) == 0
    assert nl.threshold_unit([1, 0], [1, 1], 1) == 1
    assert nl.threshold_unit([0, 0], [1, 1], 1) == 0


def test_core_threads_include_threshold_and_logical_network() -> None:
    config = nl.NeuralLogicConfig()
    scored = [nl.score_concept(row, config) for row in nl.concept_rows()]
    core = {row["concept_id"] for row in scored if row["interpretive_status"] == "core_neural_logic_thread"}
    assert "threshold_unit" in core
    assert "logical_network" in core


def test_cautions_include_modern_deep_learning_boundary() -> None:
    cautions = {row["caution"] for row in nl.interpretation_cautions()}
    assert "do_not_call_it_modern_deep_learning" in cautions


def main() -> None:
    test_threshold_logic_and_or()
    test_core_threads_include_threshold_and_logical_network()
    test_cautions_include_modern_deep_learning_boundary()
    print("All McCulloch-Pitts neural logic tests passed.")


if __name__ == "__main__":
    main()
