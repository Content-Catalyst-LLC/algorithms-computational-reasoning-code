from pathlib import Path
import json
from greedy_algorithms.workflow import run_workflow
from greedy_algorithms.examples import dijkstra, huffman_merge_order, interval_scheduling, nearest_neighbor_route

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "interval_scheduling": interval_scheduling([("A",0,6),("B",1,4),("C",3,5),("D",5,7)]),
        "dijkstra": dijkstra({"A":[("B",2),("C",5)],"B":[("C",1)],"C":[]}, "A"),
        "huffman_merge_order": huffman_merge_order({"A":5,"B":9,"C":12,"D":13}),
        "nearest_neighbor_route": nearest_neighbor_route(["A","B","C"], {("A","B"):3,("A","C"):5,("B","C"):1}, "A")
    }
    (root/"outputs"/"json"/"greedy_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Greedy algorithm workflow complete.")
