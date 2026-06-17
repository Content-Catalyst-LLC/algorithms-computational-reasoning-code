from pathlib import Path
import json
from runtime_context.workflow import run_workflow
from runtime_context.examples import minimal_environment_manifest, validate_required_config

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    (root/"outputs"/"json"/"minimal_environment_manifest.json").write_text(json.dumps(minimal_environment_manifest(), indent=2), encoding="utf-8")
    (root/"outputs"/"json"/"config_validation_demo.json").write_text(json.dumps(validate_required_config(["PATH"]), indent=2), encoding="utf-8")
    print("Runtime context workflow complete.")
