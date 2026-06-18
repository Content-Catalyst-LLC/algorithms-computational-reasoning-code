#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(relevant: str, ranked: str, k: int):
    rel=set(x.strip() for x in relevant.split(",") if x.strip())
    ranking=[x.strip() for x in ranked.split(",") if x.strip()]
    top=ranking[:k]
    score=len(set(top) & rel)/len(top) if top else 0.0
    return {"k": k, "precision_at_k": round(score,4), "relevant_in_top_k": len(set(top) & rel)}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--relevant",default="doc_1,doc_4")
    p.add_argument("--ranked",default="doc_4,doc_2,doc_1,doc_3")
    p.add_argument("--k",type=int,default=3)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.relevant,a.ranked,a.k)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"precision_at_k_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
