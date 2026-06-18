from pathlib import Path
import json
from evolutionary_algorithms.workflow import run_workflow
from evolutionary_algorithms.examples import binary_fitness, crossover, diversity, multi_seed_summary, mutation, simple_ga

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    pop=[[1,0,1,1],[1,1,0,0],[0,0,1,1]]
    demos={
        "binary_fitness": binary_fitness([1,0,1,1]),
        "mutation": mutation([1,0,1,1], 0.25),
        "crossover": crossover([1,1,1,1],[0,0,0,0]),
        "diversity": diversity(pop),
        "simple_ga": simple_ga(),
        "multi_seed_summary": multi_seed_summary()
    }
    (root/"outputs"/"json"/"evolutionary_algorithm_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Evolutionary algorithm workflow complete.")
