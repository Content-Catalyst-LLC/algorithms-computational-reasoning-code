from pathlib import Path
import json
from big_o_growth.workflow import run_workflow, cost, estimate_threshold

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "growth_at_1000":{"linear":cost(1000,"linear"),"n_log_n":cost(1000,"n_log_n"),"quadratic":cost(1000,"quadratic")},
        "thresholds_for_1e6":{"linear":estimate_threshold(1_000_000,"linear"),"quadratic":estimate_threshold(1_000_000,"quadratic"),"exponential":estimate_threshold(1_000_000,"exponential")}
    }
    (root/"outputs"/"json"/"big_o_growth_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Big-O growth workflow complete.")
