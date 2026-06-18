#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def compute(n):
    return {"n":n,"subsets_2_to_n":2**n if n <= 60 else "too_large","permutations_n_factorial":math.factorial(n) if n <= 20 else "too_large","quadratic_pairs":n*(n-1)//2}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=20)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.n)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"search_space_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
