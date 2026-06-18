#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(vertices: int, edges: int) -> dict[str, object]:
    matrix = vertices * vertices
    adj_list = vertices + edges
    return {
        "vertices": vertices,
        "edges": edges,
        "adjacency_matrix_units": matrix,
        "adjacency_list_units": adj_list,
        "matrix_to_list_ratio": round(matrix / max(adj_list, 1), 3),
        "interpretation": "Sparse graphs often require far less memory with adjacency lists than adjacency matrices."
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--vertices",type=int,default=1000)
    p.add_argument("--edges",type=int,default=5000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.vertices,a.edges)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"graph_storage_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
