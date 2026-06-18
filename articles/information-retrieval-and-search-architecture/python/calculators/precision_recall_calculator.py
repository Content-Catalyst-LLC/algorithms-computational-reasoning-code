#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(relevant: str, retrieved: str):
    relevant_set=set(x.strip() for x in relevant.split(",") if x.strip())
    retrieved_list=[x.strip() for x in retrieved.split(",") if x.strip()]
    retrieved_set=set(retrieved_list)
    tp=len(relevant_set & retrieved_set)
    precision=tp/len(retrieved_list) if retrieved_list else 0.0
    recall=tp/len(relevant_set) if relevant_set else 0.0
    return {"precision": round(precision,4), "recall": round(recall,4), "true_positive": tp}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--relevant",default="doc_1,doc_4")
    p.add_argument("--retrieved",default="doc_4,doc_2,doc_1")
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.relevant,a.retrieved)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"precision_recall_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
