from pathlib import Path
import json
from online_algorithms.workflow import run_workflow, ski_rental_table, queue_pressure_table, lru_cache_simulation

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    demos={
        "ski_rental_sample": ski_rental_table(10.0, 50.0, 8),
        "queue_pressure_sample": queue_pressure_table([80, 100, 120], 100.0),
        "lru_cache_sample": lru_cache_simulation(["A","B","A","C","D","A"], 2)
    }
    (root/"outputs"/"json"/"online_algorithm_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Online algorithms and arrival-decision workflow complete.")
