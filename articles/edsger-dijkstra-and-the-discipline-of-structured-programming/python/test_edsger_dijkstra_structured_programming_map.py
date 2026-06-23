from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import edsger_dijkstra_structured_programming_map as dijkstra


def test_core_threads_include_structure_correctness_ai() -> None:
    config = dijkstra.DijkstraConfig()
    scored = [dijkstra.score_theme(row, config) for row in dijkstra.dijkstra_themes()]
    core = {row["theme_id"] for row in scored if row["interpretive_status"] == "core_dijkstra_structured_programming_thread"}
    assert "structured_control_flow" in core
    assert "program_correctness" in core
    assert "ai_generated_code_review" in core


def test_dijkstra_shortest_paths() -> None:
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("B", 1), ("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }
    distances = dijkstra.dijkstra_shortest_paths(graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 3
    assert distances["D"] == 8
    assert distances["E"] == 10


def test_cautions_include_testing_and_ai() -> None:
    cautions = {row["caution"] for row in dijkstra.interpretation_cautions()}
    assert "do_not_confuse_testing_with_proof" in cautions
    assert "do_not_accept_ai_generated_code_without_reasoning" in cautions


def main() -> None:
    test_core_threads_include_structure_correctness_ai()
    test_dijkstra_shortest_paths()
    test_cautions_include_testing_and_ai()
    print("All Dijkstra structured-programming tests passed.")


if __name__ == "__main__":
    main()
