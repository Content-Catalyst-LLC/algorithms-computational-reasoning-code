from pathlib import Path
import json
from cloud_infrastructure.workflow import run_workflow, total_latency, nominal_capacity, unit_cost, redundant_availability, infrastructure_risk_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "cloud_response_latency_ms":total_latency(80,45,60,25,15),
        "nominal_capacity":nominal_capacity(12,250),
        "unit_cost":unit_cost(120,35,25,90,18,144000),
        "redundant_availability":redundant_availability([.99,.985]),
        "infrastructure_risk_score":infrastructure_risk_score(.18,.24,.16,.22,.20)
    }
    (root/"outputs"/"json"/"cloud_infrastructure_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Cloud computing and algorithmic infrastructure workflow complete.")
