#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(branching_factor, depth, candidate_type):
    if candidate_type == "tree":
        count=sum(branching_factor**level for level in range(depth+1))
    elif candidate_type == "subsets":
        count=2**depth
    elif candidate_type == "permutations":
        count=math.factorial(depth)
    else:
        count=branching_factor**depth
    return {"candidate_type":candidate_type,"branching_factor":branching_factor,"depth_or_n":depth,"estimated_candidates":count,"interpretation":"Pedagogical estimate of search-space growth; pruning and constraints may reduce explored nodes."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--branching-factor",type=int,default=3)
    p.add_argument("--depth",type=int,default=8)
    p.add_argument("--candidate-type",choices=["tree","subsets","permutations","assignments"],default="tree")
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.branching_factor,a.depth,a.candidate_type)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"search_space_growth_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
