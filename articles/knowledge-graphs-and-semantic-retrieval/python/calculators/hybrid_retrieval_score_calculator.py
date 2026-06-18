#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(lexical: float, vector: float, graph: float, provenance: float):
    score=100*(0.25*lexical+0.25*vector+0.25*graph+0.25*provenance)
    return {"lexical": lexical, "vector": vector, "graph": graph, "provenance": provenance, "hybrid_retrieval_score": round(score,3), "diagnostic": "strong hybrid retrieval balance" if score >= 84 else "review lexical, vector, graph, and provenance balance"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--lexical",type=float,default=0.82)
    p.add_argument("--vector",type=float,default=0.78)
    p.add_argument("--graph",type=float,default=0.88)
    p.add_argument("--provenance",type=float,default=0.90)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.lexical,a.vector,a.graph,a.provenance)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"hybrid_retrieval_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
