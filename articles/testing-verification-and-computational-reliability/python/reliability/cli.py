from pathlib import Path
import json
from reliability.workflow import run_workflow
from reliability.examples import load_test_results, test_result_summary, score_in_range, nondecreasing, round_trip

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    rows=load_test_results(root)
    demos={
        "synthetic_test_result_summary": test_result_summary(rows),
        "score_in_range_72": score_in_range(72),
        "nondecreasing_demo": nondecreasing([1,2,2,5]),
        "round_trip_demo": round_trip("computational reliability")
    }
    (root/"outputs"/"json"/"reliability_example_demos.json").write_text(json.dumps(demos, indent=2), encoding="utf-8")
    print("Testing, verification, and reliability workflow complete.")
