#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(entity: float, relationship: float, predicate: float, join: float, keys: float, missingness: float):
    score=100*(0.18*entity+0.18*relationship+0.18*predicate+0.18*join+0.14*keys+0.14*missingness)
    return {"query_logic_core_score": round(score,3), "diagnostic": "strong core query logic" if score >= 84 else "review entities, relationships, predicates, joins, keys, and missingness"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--entity",type=float,default=0.88)
    p.add_argument("--relationship",type=float,default=0.86)
    p.add_argument("--predicate",type=float,default=0.84)
    p.add_argument("--join",type=float,default=0.82)
    p.add_argument("--keys",type=float,default=0.84)
    p.add_argument("--missingness",type=float,default=0.80)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.entity,a.relationship,a.predicate,a.join,a.keys,a.missingness)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"query_logic_score_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
