#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def unit_cost(compute_cost, storage_cost, network_cost, managed_service_cost, observability_cost, completed_work):
    total = compute_cost + storage_cost + network_cost + managed_service_cost + observability_cost
    return total / completed_work if completed_work else 0.0

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--compute-cost",type=float,default=120.0)
    p.add_argument("--storage-cost",type=float,default=35.0)
    p.add_argument("--network-cost",type=float,default=25.0)
    p.add_argument("--managed-service-cost",type=float,default=90.0)
    p.add_argument("--observability-cost",type=float,default=18.0)
    p.add_argument("--completed-work",type=float,default=144000)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"compute_cost":a.compute_cost,"storage_cost":a.storage_cost,"network_cost":a.network_cost,"managed_service_cost":a.managed_service_cost,"observability_cost":a.observability_cost,"completed_work":a.completed_work,"unit_cost":round(unit_cost(a.compute_cost,a.storage_cost,a.network_cost,a.managed_service_cost,a.observability_cost,a.completed_work),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"cloud_unit_cost_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
