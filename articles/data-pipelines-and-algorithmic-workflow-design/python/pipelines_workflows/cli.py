from pathlib import Path
import json
from pipelines_workflows.workflow import run_workflow, pipeline_quality_calculator, freshness_score, validation_pass_rate

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "pipeline_quality_score": pipeline_quality_calculator(.92,.86,.90,.88,.82),
        "freshness_14_days": {"freshness_score": freshness_score(14)},
        "validation_18_of_20": {"validation_pass_rate": validation_pass_rate(18,20)}
    }
    (root/"outputs"/"json"/"pipeline_workflow_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Data pipelines and algorithmic workflow design workflow complete.")
