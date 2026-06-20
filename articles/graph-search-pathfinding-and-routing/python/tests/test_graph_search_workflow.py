from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"python"))
from graph_search.workflow import load_graph, bfs_path, dijkstra_path, edge_count, graph_density

def test_bfs_path():
    graph=load_graph(ROOT/"data"/"synthetic_graph_edges.csv")
    assert bfs_path(graph,"A","E") == ["A","C","E"]

def test_dijkstra_path():
    graph=load_graph(ROOT/"data"/"synthetic_graph_edges.csv")
    assert dijkstra_path(graph,"A","E")["cost"] == 5.5

def test_density():
    graph=load_graph(ROOT/"data"/"synthetic_graph_edges.csv")
    assert graph_density(len(graph), edge_count(graph)) == 0.35
