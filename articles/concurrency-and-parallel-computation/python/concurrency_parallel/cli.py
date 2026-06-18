from pathlib import Path
import json
from concurrency_parallel.workflow import run_workflow, speedup, amdahl_speedup, parallel_efficiency, concurrency_risk_score

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "speedup_120_to_28": {"speedup": speedup(120,28), "efficiency_8": parallel_efficiency(8, speedup(120,28))},
        "amdahl_16_workers": {"amdahl_speedup": amdahl_speedup(16,.12), "efficiency_16": parallel_efficiency(16, amdahl_speedup(16,.12))},
        "concurrency_risk": concurrency_risk_score(.84,.82,.80,.84,.82,.84)
    }
    (root/"outputs"/"json"/"concurrency_parallelism_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Concurrency and parallel computation workflow complete.")
