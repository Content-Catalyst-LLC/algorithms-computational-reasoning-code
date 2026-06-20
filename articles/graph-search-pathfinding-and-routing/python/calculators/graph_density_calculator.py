#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--edge-csv",default="data/synthetic_graph_edges.csv")
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    nodes=set(); edges=0
    with Path(a.edge_csv).open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            nodes.add(r["source"]); nodes.add(r["target"]); edges += 1
    possible=len(nodes)*(len(nodes)-1)
    result={"node_count":len(nodes),"directed_edge_count":edges,"density":round(edges/possible,6) if possible else 0.0}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"graph_density_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
