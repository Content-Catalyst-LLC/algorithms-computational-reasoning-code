from pathlib import Path
import json
from efficiency_understanding.workflow import run_workflow, efficiency_gain, understanding_composite

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "efficiency_gain_sample": efficiency_gain(100.0, 64.0),
        "understanding_composite_sample": understanding_composite(0.80,0.75,0.70,0.78,0.82)
    }
    (root/"outputs"/"json"/"efficiency_understanding_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Efficiency vs. understanding workflow complete.")
