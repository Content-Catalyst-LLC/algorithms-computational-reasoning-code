from pathlib import Path
import json
from api_interfaces.workflow import run_workflow
from api_interfaces.examples import compatibility_check, validate_record

if __name__ == "__main__":
    root=Path(__file__).resolve().parents[2]
    run_workflow(root)
    (root/"outputs"/"json"/"compatibility_check_demo.json").write_text(json.dumps(compatibility_check({"case_id","status","score"},{"case_id","status","score","version"}), indent=2), encoding="utf-8")
    (root/"outputs"/"json"/"minimal_validator_demo.json").write_text(json.dumps(validate_record({"case_id":"x","status":"review","score":1.0}), indent=2), encoding="utf-8")
    print("API and interface workflow complete.")
