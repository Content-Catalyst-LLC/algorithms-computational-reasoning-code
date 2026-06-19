from pathlib import Path
import json
from platform_power.workflow import run_workflow, dependency_score, switching_cost, api_dependency_ratio, visibility_share

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "dependency_score":dependency_score(.80,.90,.70,.85,.65),
        "switching_cost":switching_cost(45000,120000,18000,24000,75000),
        "api_dependency_ratio":api_dependency_ratio(850000,1000000),
        "visibility_share":visibility_share(250000,5000000)
    }
    (root/"outputs"/"json"/"platform_power_example_demos.json").write_text(json.dumps(demos,indent=2),encoding="utf-8")
    print("Algorithmic infrastructure and platform power workflow complete.")
