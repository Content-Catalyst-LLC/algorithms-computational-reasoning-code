#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(max_depth, runtime_stack_limit, has_base_case, progress_verified, memoization_used, repeated_subproblem_count):
    depth_ratio=max_depth/max(1,runtime_stack_limit)
    risk=100*(0.40*min(1,depth_ratio)+0.25*(1-has_base_case)+0.20*(1-progress_verified)+0.10*min(1,repeated_subproblem_count/1000)+0.05*(1-memoization_used))
    return {"max_depth":max_depth,"runtime_stack_limit":runtime_stack_limit,"depth_ratio":round(depth_ratio,4),"recursion_depth_risk_score":round(min(100,risk),2),"interpretation":"Risk rises with deep recursion, missing base cases, unclear progress, and repeated subproblems."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--max-depth",type=int,default=250)
    p.add_argument("--runtime-stack-limit",type=int,default=1000)
    p.add_argument("--has-base-case",type=int,default=1)
    p.add_argument("--progress-verified",type=int,default=1)
    p.add_argument("--memoization-used",type=int,default=0)
    p.add_argument("--repeated-subproblem-count",type=int,default=100)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.max_depth,a.runtime_stack_limit,a.has_base_case,a.progress_verified,a.memoization_used,a.repeated_subproblem_count)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"recursion_depth_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
