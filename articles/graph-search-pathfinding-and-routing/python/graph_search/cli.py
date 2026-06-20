from pathlib import Path
import json
from graph_search.workflow import load_graph, bfs_path, dfs_order, dijkstra_path, edge_count, graph_density, run_workflow

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    graph=load_graph(root/"data"/"synthetic_graph_edges.csv")
    demos={
        "bfs_path":bfs_path(graph,"A","E"),
        "dfs_order":dfs_order(graph,"A"),
        "dijkstra_path":dijkstra_path(graph,"A","E"),
        "graph_density":graph_density(len(graph),edge_count(graph))
    }
    (root/"outputs"/"json"/"graph_search_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Graph search, pathfinding, and routing workflow complete.")
