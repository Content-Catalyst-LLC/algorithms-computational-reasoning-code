#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def edge_response_time(sense_ms, filter_ms, compute_ms, actuate_ms):
    return sense_ms + filter_ms + compute_ms + actuate_ms

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--sense-ms",type=float,default=8.0)
    p.add_argument("--filter-ms",type=float,default=6.0)
    p.add_argument("--compute-ms",type=float,default=14.0)
    p.add_argument("--actuate-ms",type=float,default=5.0)
    p.add_argument("--deadline-ms",type=float,default=50.0)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    response=edge_response_time(a.sense_ms,a.filter_ms,a.compute_ms,a.actuate_ms)
    result={"sense_ms":a.sense_ms,"filter_ms":a.filter_ms,"compute_ms":a.compute_ms,"actuate_ms":a.actuate_ms,"edge_response_time_ms":round(response,3),"deadline_ms":a.deadline_ms,"meets_deadline":response<=a.deadline_ms}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"edge_response_deadline_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
