#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def speedup(t1, tp): return t1/tp if tp else 0.0
def amdahl(p, s): return 1/(s + ((1-s)/p)) if p else 0.0

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--sequential-time",type=float,default=120.0)
    p.add_argument("--parallel-time",type=float,default=28.0)
    p.add_argument("--processors",type=int,default=8)
    p.add_argument("--sequential-fraction",type=float,default=0.12)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    obs=speedup(a.sequential_time,a.parallel_time); amd=amdahl(a.processors,a.sequential_fraction)
    result={"sequential_time":a.sequential_time,"parallel_time":a.parallel_time,"processors":a.processors,"sequential_fraction":a.sequential_fraction,"observed_speedup":round(obs,4),"observed_efficiency":round(obs/a.processors,4),"amdahl_speedup":round(amd,4),"amdahl_efficiency":round(amd/a.processors,4)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"parallel_speedup_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
