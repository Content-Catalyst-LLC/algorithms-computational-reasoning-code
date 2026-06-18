#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def estimate(n, branches, shrink, combine_power):
    depth=0; size=max(1,n)
    while size > 1:
        size=max(1,size//shrink); depth += 1
    if combine_power == 0:
        combine_work=depth+1
    else:
        combine_work=sum((n/(shrink**level))**combine_power*(branches**level) for level in range(depth+1))
    return {"n":n,"branches":branches,"shrink":shrink,"combine_power":combine_power,"estimated_depth":depth,"estimated_leaf_count":branches**depth,"estimated_nonrecursive_work":round(combine_work,3),"interpretation":"Pedagogical recurrence estimate for T(n)=aT(n/b)+O(n^d)."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=1024)
    p.add_argument("--branches",type=int,default=2)
    p.add_argument("--shrink",type=int,default=2)
    p.add_argument("--combine-power",type=float,default=1.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=estimate(a.n,a.branches,a.shrink,a.combine_power)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"recurrence_complexity_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
