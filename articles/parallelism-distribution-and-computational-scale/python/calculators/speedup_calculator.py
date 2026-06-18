#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def speedup(serial_fraction: float, processors: int) -> float:
    return 1.0 / (serial_fraction + ((1.0 - serial_fraction) / processors))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--serial-fraction",type=float,default=0.10)
    p.add_argument("--processors",type=int,default=16)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    s=speedup(a.serial_fraction,a.processors)
    result={
        "serial_fraction":a.serial_fraction,
        "processors":a.processors,
        "amdahl_speedup_bound":round(s,4),
        "parallel_efficiency":round(s/a.processors,4)
    }
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"speedup_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
