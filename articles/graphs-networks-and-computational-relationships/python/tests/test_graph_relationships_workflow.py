from pathlib import Path
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE_ROOT / "python"))

from graph_relationships.workflow import GraphRelationshipCase, graph_reasoning_quality, relationship_overclaim_risk
from graph_relationships.examples import adjacency_list, bfs_distances, detect_cycle_dfs, dijkstra, demo_graph
from calculators.graph_reasoning_quality_calculator import compute


def test_graph_scores_in_range():
    case = GraphRelationshipCase("Test", "Context", "Choice", 0.8, 0.8, 0.8, 0.75, 0.75, 0.75, 0.8, 0.75, 0.8, 0.8)
    assert 0 <= graph_reasoning_quality(case) <= 100
    assert 0 <= relationship_overclaim_risk(case) <= 100


def test_bfs_and_cycle_detection():
    graph = adjacency_list([("A", "B"), ("B", "C")])
    assert bfs_distances(graph, "A")["C"] == 2
    assert detect_cycle_dfs(graph) is False
    assert detect_cycle_dfs(adjacency_list([("A", "B"), ("B", "A")])) is True


def test_dijkstra_distance():
    graph = {"A": [("B", 1.0), ("C", 5.0)], "B": [("C", 1.0)], "C": []}
    assert dijkstra(graph, "A")["C"] == 2.0


def test_demo_and_calculator():
    assert demo_graph()["contains_directed_cycle"] is False
    assert "interpretation" in compute([0.75] * 10)
