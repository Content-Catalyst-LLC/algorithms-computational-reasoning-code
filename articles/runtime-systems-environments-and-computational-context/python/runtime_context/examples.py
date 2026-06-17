from __future__ import annotations
from pathlib import Path
import csv, os, platform, sys

def minimal_environment_manifest() -> dict[str, object]:
    return {
        "python_version": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
        "cwd": os.getcwd(),
        "path_available": "PATH" in os.environ,
    }

def validate_required_config(required: list[str]) -> dict[str, object]:
    missing=[k for k in required if not os.environ.get(k)]
    return {"required": required, "missing": missing, "valid": len(missing)==0}

def load_environment_taxonomy(root: Path) -> list[dict[str, str]]:
    with (root/"data"/"synthetic_environment_taxonomy.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
