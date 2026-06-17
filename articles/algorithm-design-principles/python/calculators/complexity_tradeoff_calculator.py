#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(n, strategy, interpretability_weight, performance_weight):
    estimates={"linear":n,"nlogn":n*max(1,math.log2(max(2,n))),"quadratic":n*n,"exponential":2**min(n,30)}
    steps=estimates.get(strategy,n)
    normalized_cost=min(100,100*steps/max(1,estimates["quadratic"]))
    interpretability={"linear":90,"nlogn":75,"quadratic":85,"exponential":50}.get(strategy,70)
    score=round(performance_weight*(100-normalized_cost)+interpretability_weight*interpretability,3)
    return {"n":n,"strategy":strategy,"estimated_steps":round(steps,3),"normalized_cost":round(normalized_cost,3),"tradeoff_score":score}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=1000)
    p.add_argument("--strategy",choices=["linear","nlogn","quadratic","exponential"],default="nlogn")
    p.add_argument("--interpretability-weight",type=float,default=0.4)
    p.add_argument("--performance-weight",type=float,default=0.6)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.n,a.strategy,a.interpretability_weight,a.performance_weight)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"complexity_tradeoff_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
