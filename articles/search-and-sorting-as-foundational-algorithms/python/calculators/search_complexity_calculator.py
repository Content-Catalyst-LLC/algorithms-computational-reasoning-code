#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(n, algorithm, key_range):
    if algorithm == "linear_search":
        steps=n
    elif algorithm == "binary_search":
        steps=max(1, math.ceil(math.log2(max(2,n))))
    elif algorithm == "merge_sort":
        steps=n*max(1, math.log2(max(2,n)))
    elif algorithm == "quadratic_sort":
        steps=n*n
    elif algorithm == "counting_sort":
        steps=n+key_range
    else:
        steps=n
    return {"n":n,"algorithm":algorithm,"key_range":key_range,"estimated_steps":round(steps,3),"interpretation":"Estimate is pedagogical and depends on assumptions and implementation details."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=1000)
    p.add_argument("--algorithm",choices=["linear_search","binary_search","merge_sort","quadratic_sort","counting_sort"],default="merge_sort")
    p.add_argument("--key-range",type=int,default=100)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.n,a.algorithm,a.key_range)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"search_complexity_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
