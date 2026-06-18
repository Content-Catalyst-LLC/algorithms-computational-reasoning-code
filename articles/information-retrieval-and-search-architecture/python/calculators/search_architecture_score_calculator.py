#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(collection: float, metadata: float, indexing: float, ranking: float, evaluation: float, provenance: float):
    score=100*(0.18*collection+0.18*metadata+0.18*indexing+0.16*ranking+0.15*evaluation+0.15*provenance)
    return {"search_architecture_core_score": round(score,3), "diagnostic": "strong search architecture core" if score >= 84 else "review collection coverage, metadata, indexing, ranking, evaluation, and provenance"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--collection",type=float,default=0.88)
    p.add_argument("--metadata",type=float,default=0.90)
    p.add_argument("--indexing",type=float,default=0.84)
    p.add_argument("--ranking",type=float,default=0.76)
    p.add_argument("--evaluation",type=float,default=0.74)
    p.add_argument("--provenance",type=float,default=0.86)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.collection,a.metadata,a.indexing,a.ranking,a.evaluation,a.provenance)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"search_architecture_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
