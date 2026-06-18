from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from knowledge_graphs.workflow import build_adjacency, shortest_path, neighborhood, hybrid_score, graph_path_score

def test_shortest_path():
    edges=[("A","to","B"),("B","to","C")]
    assert shortest_path(edges,"A","C") == ["A","B","C"]

def test_neighborhood():
    edges=[("A","to","B"),("B","to","C")]
    assert len(neighborhood(edges,"A",radius=2)) == 2

def test_hybrid_score():
    assert hybrid_score(1,1,1,1)["hybrid_score"] == 100.0

def test_graph_path_score():
    assert graph_path_score(1,1,1,1)["graph_path_score"] == 100.0

def test_adjacency():
    assert build_adjacency([("A","to","B")])["A"] == [("to","B")]
