from pathlib import Path
import csv

REQUIRED_FIELDS={"case_id","status","score"}

def validate_record(record: dict[str, object]) -> dict[str, object]:
    missing=sorted(REQUIRED_FIELDS-set(record.keys()))
    errors=[]
    if missing: errors.append({"code":"missing_required_fields","fields":missing})
    if "score" in record and not isinstance(record["score"], (int,float)):
        errors.append({"code":"invalid_score_type"})
    return {"valid":len(errors)==0,"errors":errors}

def compatibility_check(old_fields: set[str], new_fields: set[str]) -> dict[str, object]:
    removed=sorted(old_fields-new_fields)
    added=sorted(new_fields-old_fields)
    return {"compatible":len(removed)==0,"removed_fields":removed,"added_fields":added}

def load_interface_taxonomy(root: Path) -> list[dict[str, str]]:
    with (root/"data"/"synthetic_interface_taxonomy.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
