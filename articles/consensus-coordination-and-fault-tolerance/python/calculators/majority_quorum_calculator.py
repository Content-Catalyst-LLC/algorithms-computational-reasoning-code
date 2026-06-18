#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from math import comb
def majority_quorum(n): return n//2 + 1
def crash_fault_tolerance(n): return (n-1)//2
def majority_availability(n,a):
    q=majority_quorum(n)
    return sum(comb(n,x)*(a**x)*((1-a)**(n-x)) for x in range(q,n+1))
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--node-count",type=int,default=5)
    p.add_argument("--node-availability",type=float,default=.99)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    q=majority_quorum(a.node_count)
    result={"node_count":a.node_count,"majority_quorum":q,"crash_fault_tolerance":crash_fault_tolerance(a.node_count),"quorum_intersection_holds":2*q>a.node_count,"majority_availability":round(majority_availability(a.node_count,a.node_availability),8)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"majority_quorum_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
