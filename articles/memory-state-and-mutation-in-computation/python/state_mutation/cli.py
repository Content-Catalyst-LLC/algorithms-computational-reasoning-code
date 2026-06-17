from pathlib import Path
import json
from state_mutation.workflow import run_workflow
from state_mutation.examples import aliasing_demo, demo_state_machine
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    run_workflow(root)
    (root/"outputs"/"json"/"state_machine_demo.json").write_text(json.dumps(demo_state_machine(), indent=2), encoding="utf-8")
    (root/"outputs"/"json"/"aliasing_demo.json").write_text(json.dumps(aliasing_demo(), indent=2), encoding="utf-8")
    print("State and mutation workflow complete.")
