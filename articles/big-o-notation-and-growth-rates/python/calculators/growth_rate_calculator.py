#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
def cost(n, growth):
    if growth == "constant": return 1.0
    if growth == "log": return math.log2(max(n,2))
    if growth == "linear": return float(n)
    if growth == "n_log_n": return n*math.log2(max(n,2))
    if growth == "quadratic": return float(n*n)
    if growth == "cubic": return float(n*n*n)
    if growth == "exponential": return "too_large" if n > 30 else float(2**n)
    if growth == "factorial": return "too_large" if n > 12 else float(math.factorial(n))
    raise ValueError(growth)
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=1000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"n":a.n,**{g:cost(a.n,g) for g in ["constant","log","linear","n_log_n","quadratic","cubic","exponential","factorial"]}}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"growth_rate_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
