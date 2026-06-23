from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import data_structures_algorithm_analysis_history_map as ds


def test_core_threads_include_graphs_asymptotic_ai() -> None:
    config = ds.DataStructureHistoryConfig()
    scored = [ds.score_tradition(row, config) for row in ds.structure_traditions()]
    core = {row["tradition_id"] for row in scored if row["interpretive_status"] == "core_data_structure_analysis_history_thread"}
    assert "graphs_relational_structure" in core
    assert "asymptotic_algorithm_analysis" in core
    assert "ai_infrastructure_structures" in core


def test_binary_search_steps() -> None:
    assert ds.binary_search_steps(0) == 0
    assert ds.binary_search_steps(1) == 1
    assert ds.binary_search_steps(100) == 7


def test_graph_memory_model() -> None:
    row = ds.adjacency_memory_nodes_edges(10, 20)
    assert row["adjacency_matrix_cells"] == 100
    assert row["adjacency_list_units"] == 30


def test_cautions_include_big_o_and_ai_audit() -> None:
    cautions = {row["caution"] for row in ds.interpretation_cautions()}
    assert "do_not_treat_big_o_as_the_only_truth" in cautions
    assert "do_not_build_ai_systems_without_data_structure_audits" in cautions


def main() -> None:
    test_core_threads_include_graphs_asymptotic_ai()
    test_binary_search_steps()
    test_graph_memory_model()
    test_cautions_include_big_o_and_ai_audit()
    print("All data-structure and algorithm-analysis history tests passed.")


if __name__ == "__main__":
    main()
