from pathlib import Path
import json
from parallelism_scale.workflow import run_workflow, speedup, capacity_table

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "speedup_serial_fraction_0_10_processors_16": round(speedup(0.10, 16), 4),
        "capacity_table": capacity_table(100.0, [1,2,4,8,16])
    }
    (root/"outputs"/"json"/"parallelism_scale_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Parallelism and scale workflow complete.")
