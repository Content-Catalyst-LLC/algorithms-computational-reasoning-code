from pathlib import Path
import json
from data_quality.workflow import run_workflow, data_quality_calculator, missingness_rate, completeness_score, freshness_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "data_quality_score": data_quality_calculator(.92,.88,.86,.90,.89),
        "missingness_45_of_1000": {"missingness_rate": missingness_rate(45,1000), "completeness_score": completeness_score(45,1000)},
        "freshness_30_days": {"freshness_score": freshness_score(30)}
    }
    (root/"outputs"/"json"/"data_quality_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Data quality, missingness, and computational judgment workflow complete.")
