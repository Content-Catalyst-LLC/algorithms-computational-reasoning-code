#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(workers: int, service_rate: float, overhead_rate: float) -> dict[str, float]:
    ideal=workers*service_rate
    overhead=ideal*overhead_rate*max(workers-1,0)
    effective=max(ideal-overhead,0.0)
    return {
        "workers":workers,
        "service_rate_per_worker":service_rate,
        "overhead_rate":overhead_rate,
        "ideal_capacity":round(ideal,3),
        "estimated_overhead":round(overhead,3),
        "effective_capacity":round(effective,3)
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--workers",type=int,default=8)
    p.add_argument("--service-rate",type=float,default=100.0)
    p.add_argument("--overhead-rate",type=float,default=0.05)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.workers,a.service_rate,a.overhead_rate)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"distributed_capacity_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
