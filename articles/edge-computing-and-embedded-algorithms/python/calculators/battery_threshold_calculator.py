#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def battery_life_hours(battery_wh, average_power_w):
    return battery_wh / average_power_w if average_power_w else 0.0

def local_threshold_action(signal_value, threshold):
    return "alert" if signal_value >= threshold else "monitor"

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--battery-wh",type=float,default=12.0)
    p.add_argument("--average-power-w",type=float,default=0.08)
    p.add_argument("--signal-value",type=float,default=0.82)
    p.add_argument("--threshold",type=float,default=0.75)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result={"battery_wh":a.battery_wh,"average_power_w":a.average_power_w,"battery_life_hours":round(battery_life_hours(a.battery_wh,a.average_power_w),3),"signal_value":a.signal_value,"threshold":a.threshold,"action":local_threshold_action(a.signal_value,a.threshold)}
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"battery_threshold_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
