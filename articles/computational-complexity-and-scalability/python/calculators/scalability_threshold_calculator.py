#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def growth_cost(n, growth):
    if growth == "linear": return n
    if growth == "n_log_n": return n*math.log2(max(n,2))
    if growth == "quadratic": return n*n
    if growth == "cubic": return n*n*n
    if growth == "exponential": return 2**n if n < 64 else float("inf")
    raise ValueError(growth)
def estimate(budget, growth):
    n=1
    while n < 1000000:
        if growth_cost(n,growth) > budget: return n-1
        n += 1
    return n
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--budget",type=float,default=1000000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"budget":a.budget,"thresholds":{g:estimate(a.budget,g) for g in ["linear","n_log_n","quadratic","cubic","exponential"]}}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"scalability_threshold_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
