#!/usr/bin/env python3
import argparse, json
from pathlib import Path
def compute(score_proxy_validity, counterexample_coverage, tie_breaking_clarity, override_available, traceability, long_term_monitoring):
    risk=100*(0.25*(1-score_proxy_validity)+0.20*(1-counterexample_coverage)+0.15*(1-tie_breaking_clarity)+0.15*(1-override_available)+0.15*(1-traceability)+0.10*(1-long_term_monitoring))
    return {"local_choice_risk":round(max(0,min(100,risk)),3),"interpretation":"Risk rises when proxy validity, counterexample coverage, tie-breaking, override, traceability, or monitoring are weak."}
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--score-proxy-validity",type=float,default=0.70)
    p.add_argument("--counterexample-coverage",type=float,default=0.60)
    p.add_argument("--tie-breaking-clarity",type=float,default=0.70)
    p.add_argument("--override-available",type=float,default=0.80)
    p.add_argument("--traceability",type=float,default=0.80)
    p.add_argument("--long-term-monitoring",type=float,default=0.60)
    p.add_argument("--output-dir",type=Path,default=Path("outputs/json"))
    a=p.parse_args(); result=compute(a.score_proxy_validity,a.counterexample_coverage,a.tie_breaking_clarity,a.override_available,a.traceability,a.long_term_monitoring)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    (a.output_dir/"local_choice_risk_calculator.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
