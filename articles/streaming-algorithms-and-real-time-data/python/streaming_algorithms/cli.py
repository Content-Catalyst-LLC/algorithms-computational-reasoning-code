from pathlib import Path
import json
from streaming_algorithms.workflow import run_workflow, sliding_window_counts, reservoir_sample, queue_pressure_table

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    items=["A","B","A","C","A","D","B","E"]
    demos={
        "sliding_window_sample": sliding_window_counts(items, 3),
        "reservoir_sample": reservoir_sample(items, 3),
        "queue_pressure_sample": queue_pressure_table([80, 100, 120], 100.0)
    }
    (root/"outputs"/"json"/"streaming_algorithm_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Streaming algorithms and real-time data workflow complete.")
