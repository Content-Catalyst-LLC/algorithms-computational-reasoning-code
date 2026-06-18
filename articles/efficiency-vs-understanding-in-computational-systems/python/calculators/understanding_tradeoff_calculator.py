#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def compute(efficiency_gain: float, understanding_before: float, understanding_after: float) -> dict[str, float | str]:
    understanding_loss=max(understanding_before-understanding_after,0.0)
    risk=(0.65*max(efficiency_gain*100 - understanding_after*100,0.0)) + (0.35*understanding_loss*100)
    if understanding_after < 0.50 and efficiency_gain > 0.50:
        diagnostic="high risk; efficiency gain may outpace understanding"
    elif risk > 35:
        diagnostic="review needed; strengthen interpretability and governance"
    else:
        diagnostic="balanced or manageable trade-off"
    return {
        "efficiency_gain": round(efficiency_gain,6),
        "understanding_before": round(understanding_before,6),
        "understanding_after": round(understanding_after,6),
        "understanding_loss": round(understanding_loss,6),
        "tradeoff_risk": round(risk,3),
        "diagnostic": diagnostic
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--efficiency-gain",type=float,default=0.36)
    p.add_argument("--understanding-before",type=float,default=0.82)
    p.add_argument("--understanding-after",type=float,default=0.68)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args()
    result=compute(a.efficiency_gain,a.understanding_before,a.understanding_after)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"understanding_tradeoff_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
