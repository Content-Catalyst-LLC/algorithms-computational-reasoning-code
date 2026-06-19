#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def switching_cost(migration, rebuild, training, downtime, lost_network):
    return migration + rebuild + training + downtime + lost_network

def ratio(numerator, denominator):
    return numerator / denominator if denominator else 0.0

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--migration",type=float,default=45000)
    p.add_argument("--rebuild",type=float,default=120000)
    p.add_argument("--training",type=float,default=18000)
    p.add_argument("--downtime",type=float,default=24000)
    p.add_argument("--lost-network",type=float,default=75000)
    p.add_argument("--platform-requests",type=float,default=850000)
    p.add_argument("--total-requests",type=float,default=1000000)
    p.add_argument("--actor-exposure",type=float,default=250000)
    p.add_argument("--total-exposure",type=float,default=5000000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={
      "switching_cost":round(switching_cost(a.migration,a.rebuild,a.training,a.downtime,a.lost_network),3),
      "api_dependency_ratio":round(ratio(a.platform_requests,a.total_requests),6),
      "visibility_share":round(ratio(a.actor_exposure,a.total_exposure),6)
    }
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"platform_switching_api_visibility_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
