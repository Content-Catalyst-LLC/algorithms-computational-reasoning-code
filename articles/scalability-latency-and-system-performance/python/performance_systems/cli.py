from pathlib import Path
import json
from performance_systems.workflow import run_workflow, response_time, throughput, utilization, little_law, amdahl_speedup, unit_cost

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "response_time_ms":response_time(45,20,85,35,15),
        "throughput":throughput(12000,60),
        "utilization":utilization(180,200),
        "little_law_items":little_law(180,0.45),
        "amdahl_speedup":amdahl_speedup(8,0.12),
        "unit_cost":unit_cost(240,120000)
    }
    (root/"outputs"/"json"/"performance_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Scalability, latency, and system performance workflow complete.")
