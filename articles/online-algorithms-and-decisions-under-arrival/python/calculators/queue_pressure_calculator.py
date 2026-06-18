#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(arrival_rate: float, service_rate: float) -> dict[str, object]:
    utilization=arrival_rate/service_rate
    return {
        "arrival_rate": arrival_rate,
        "service_rate": service_rate,
        "utilization": round(utilization, 3),
        "stable_under_simple_model": arrival_rate < service_rate,
        "interpretation": "stable" if arrival_rate < service_rate else "backlog risk"
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--arrival-rate",type=float,default=95.0)
    p.add_argument("--service-rate",type=float,default=100.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.arrival_rate,a.service_rate)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"queue_pressure_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
