#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

def compute(lockfiles: int, pinned_toolchains: int, build_scripts: int, artifact_checksums: int, release_provenance_records: int) -> dict[str, object]:
    indicators = [lockfiles, pinned_toolchains, build_scripts, artifact_checksums, release_provenance_records]
    score = round(100.0 * sum(1 for value in indicators if value > 0) / len(indicators), 2)
    return {
        "lockfiles_present": lockfiles,
        "pinned_toolchains_present": pinned_toolchains,
        "build_scripts_present": build_scripts,
        "artifact_checksums_present": artifact_checksums,
        "release_provenance_records_present": release_provenance_records,
        "build_reproducibility_score": score,
        "interpretation": "Build reproducibility improves when dependencies, toolchains, scripts, artifacts, and release provenance are explicit and reviewable.",
    }

def main() -> None:
    parser = argparse.ArgumentParser(description="Build reproducibility calculator.")
    parser.add_argument("--lockfiles", type=int, default=1)
    parser.add_argument("--pinned-toolchains", type=int, default=1)
    parser.add_argument("--build-scripts", type=int, default=1)
    parser.add_argument("--artifact-checksums", type=int, default=1)
    parser.add_argument("--release-provenance-records", type=int, default=1)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/json"))
    args = parser.parse_args()
    result = compute(args.lockfiles, args.pinned_toolchains, args.build_scripts, args.artifact_checksums, args.release_provenance_records)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "build_reproducibility_calculator.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
