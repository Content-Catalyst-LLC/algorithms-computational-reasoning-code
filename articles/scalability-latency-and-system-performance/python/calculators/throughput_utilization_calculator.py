#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def throughput(completed_work, time_seconds):
    return completed_work / time_seconds if time_seconds else 0.0

def utilization(arrival_rate, service_rate):
    return arrival_rate / service_rate if service_rate else 0.0

def little_law(arrival_rate, average_time_in_system):
    return arrival_rate * average_time_in_system

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--completed-work",type=float,default=12000)
    p.add_argument("--time-seconds",type=float,default=60)
    p.add_argument("--arrival-rate",type=float,default=180)
    p.add_argument("--service-rate",type=float,default=200)
    p.add_argument("--average-time-in-system",type=float,default=0.45)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"completed_work":a.completed_work,"time_seconds":a.time_seconds,"throughput":round(throughput(a.completed_work,a.time_seconds),6),"arrival_rate":a.arrival_rate,"service_rate":a.service_rate,"utilization":round(utilization(a.arrival_rate,a.service_rate),6),"average_time_in_system":a.average_time_in_system,"average_items_in_system":round(little_law(a.arrival_rate,a.average_time_in_system),6)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"throughput_utilization_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
