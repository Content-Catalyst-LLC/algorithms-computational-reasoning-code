from pathlib import Path
import json
from approximation_algorithms.workflow import run_workflow
from approximation_algorithms.examples import approximation_ratio_minimization, exact_subset_cover_size, greedy_set_cover, relative_gap_minimization, vertex_cover_approx

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    universe={"a","b","c","d","e","f"}
    sets={"S1":{"a","b","c"},"S2":{"c","d"},"S3":{"d","e","f"},"S4":{"a","f"}}
    demos={
        "approximation_ratio_minimization": approximation_ratio_minimization(12, 8),
        "relative_gap_minimization": relative_gap_minimization(12, 10),
        "vertex_cover_size": len(vertex_cover_approx([("A","B"),("B","C"),("C","D")])),
        "greedy_set_cover": greedy_set_cover(universe,sets),
        "exact_subset_cover_size": exact_subset_cover_size(universe,sets)
    }
    (root/"outputs"/"json"/"approximation_algorithm_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Approximation algorithm workflow complete.")
