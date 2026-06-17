from pathlib import Path
import json
from software_architecture.workflow import run_workflow
from software_architecture.examples import dependency_density, failure_reachability

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    sample_edges=[("api","domain"),("domain","interfaces"),("worker","domain"),("reporting","storage")]
    (root/"outputs"/"json"/"dependency_density_demo.json").write_text(json.dumps({"dependency_density":dependency_density(sample_edges)}, indent=2), encoding="utf-8")
    (root/"outputs"/"json"/"failure_reachability_demo.json").write_text(json.dumps({"api_failure_reachability":sorted(failure_reachability(sample_edges, "api"))}, indent=2), encoding="utf-8")
    print("Software architecture workflow complete.")
