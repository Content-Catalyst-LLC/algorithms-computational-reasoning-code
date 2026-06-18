#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from statistics import mean
FIELDS=["state_clarity","recurrence_validity","base_case_clarity","overlapping_subproblem_evidence","optimal_substructure_evidence","transition_clarity","storage_strategy_quality","edge_case_coverage","traceability","governance_readiness"]
WEIGHTS=[0.12,0.12,0.10,0.10,0.10,0.10,0.10,0.10,0.08,0.08]
def compute(vals):
    q=max(0,min(100,100*sum(v*w for v,w in zip(vals,WEIGHTS))))
    r=max(0,min(100,100*mean(1-v for v in vals)))
    return {"dynamic_programming_quality":round(q,3),"dynamic_programming_risk":round(r,3),"interpretation":"strong dynamic-programming discipline" if q>=84 and r<=20 else "review needed"}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    for f in FIELDS: p.add_argument("--"+f.replace("_","-"),type=float,default=0.75)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute([getattr(a,f) for f in FIELDS])
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"dynamic_programming_quality_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
