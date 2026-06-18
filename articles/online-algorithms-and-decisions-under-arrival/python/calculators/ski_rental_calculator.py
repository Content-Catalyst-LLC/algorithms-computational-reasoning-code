#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(rent_cost: float, buy_cost: float, days: int) -> dict[str, object]:
    break_even = int(buy_cost // rent_cost)
    rent_only = days * rent_cost
    buy_now = buy_cost
    threshold = min(days, break_even) * rent_cost
    if days > break_even:
        threshold += buy_cost
    offline = min(rent_only, buy_now)
    return {
        "rent_cost": rent_cost,
        "buy_cost": buy_cost,
        "days": days,
        "break_even_day": break_even,
        "rent_only_cost": round(rent_only, 3),
        "buy_now_cost": round(buy_now, 3),
        "threshold_strategy_cost": round(threshold, 3),
        "offline_optimum_cost": round(offline, 3),
        "threshold_to_offline_ratio": round(threshold / max(offline, 1e-9), 3)
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--rent-cost",type=float,default=10.0)
    p.add_argument("--buy-cost",type=float,default=50.0)
    p.add_argument("--days",type=int,default=8)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.rent_cost,a.buy_cost,a.days)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"ski_rental_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
