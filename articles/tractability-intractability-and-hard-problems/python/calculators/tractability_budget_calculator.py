#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def label(cost,budget):
    if cost <= 0.25*budget: return "comfortable"
    if cost <= budget: return "near budget"
    return "exceeds budget"
def compute(n,budget):
    linear=n
    quadratic=n*n
    exponential=2**n if n <= 30 else float("inf")
    return {"n":n,"budget":budget,"linear":{"cost":linear,"feasibility":label(linear,budget)},"quadratic":{"cost":quadratic,"feasibility":label(quadratic,budget)},"exponential":{"cost":"too_large" if exponential == float("inf") else exponential,"feasibility":"exceeds budget" if exponential > budget else label(exponential,budget)}}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=30)
    p.add_argument("--budget",type=float,default=1000000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.n,a.budget)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"tractability_budget_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
