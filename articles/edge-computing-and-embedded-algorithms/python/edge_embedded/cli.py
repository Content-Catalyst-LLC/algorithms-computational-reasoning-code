from pathlib import Path
import json
from edge_embedded.workflow import run_workflow, edge_response_time, cloud_dependent_response_time, meets_deadline, battery_life_hours, local_threshold_action

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    edge=edge_response_time(8,6,14,5)
    cloud=cloud_dependent_response_time(8,90,60,90,5)
    demos={
        "edge_response_time_ms":edge,
        "edge_meets_deadline":meets_deadline(edge,50),
        "cloud_response_time_ms":cloud,
        "cloud_meets_deadline":meets_deadline(cloud,50),
        "battery_life_hours":battery_life_hours(12,0.08),
        "local_threshold_action":local_threshold_action(0.82,0.75)
    }
    (root/"outputs"/"json"/"edge_embedded_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Edge computing and embedded algorithms workflow complete.")
