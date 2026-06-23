from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


@dataclass(frozen=True)
class ComputationalMappingConfig:
    article: str = "geography_coordinates_and_computational_mapping_in_the_islamic_world"
    core_threshold: float = 0.80
    high_spatial_threshold: float = 0.86


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def computational_mapping_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "coordinates_as_spatial_data", "spatial_representation": 0.98, "coordinate_structure": 0.98, "procedural_clarity": 0.88, "institutional_use": 0.86, "correction_awareness": 0.90, "transmission_importance": 0.90, "modern_resonance": 0.96},
        {"theme_id": "al_khwarizmi_geographical_tables", "spatial_representation": 0.94, "coordinate_structure": 0.96, "procedural_clarity": 0.88, "institutional_use": 0.84, "correction_awareness": 0.92, "transmission_importance": 0.94, "modern_resonance": 0.94},
        {"theme_id": "routes_as_network_reasoning", "spatial_representation": 0.90, "coordinate_structure": 0.78, "procedural_clarity": 0.92, "institutional_use": 0.94, "correction_awareness": 0.82, "transmission_importance": 0.88, "modern_resonance": 0.94},
        {"theme_id": "climates_and_regional_classification", "spatial_representation": 0.88, "coordinate_structure": 0.84, "procedural_clarity": 0.86, "institutional_use": 0.88, "correction_awareness": 0.82, "transmission_importance": 0.88, "modern_resonance": 0.90},
        {"theme_id": "al_idrisi_cartographic_synthesis", "spatial_representation": 0.96, "coordinate_structure": 0.84, "procedural_clarity": 0.88, "institutional_use": 0.90, "correction_awareness": 0.88, "transmission_importance": 0.94, "modern_resonance": 0.92},
        {"theme_id": "qibla_and_directional_calculation", "spatial_representation": 0.90, "coordinate_structure": 0.88, "procedural_clarity": 0.94, "institutional_use": 0.96, "correction_awareness": 0.86, "transmission_importance": 0.88, "modern_resonance": 0.94},
        {"theme_id": "projection_scale_and_map_choice", "spatial_representation": 0.94, "coordinate_structure": 0.90, "procedural_clarity": 0.86, "institutional_use": 0.86, "correction_awareness": 0.90, "transmission_importance": 0.84, "modern_resonance": 0.96},
    ]


def score_theme(row: dict[str, object], config: ComputationalMappingConfig) -> dict[str, object]:
    mapping_score = mean([
        float(row["spatial_representation"]),
        float(row["coordinate_structure"]),
        float(row["procedural_clarity"]),
        float(row["institutional_use"]),
        float(row["correction_awareness"]),
        float(row["transmission_importance"]),
        float(row["modern_resonance"]),
    ])

    if mapping_score >= config.core_threshold and float(row["spatial_representation"]) >= config.high_spatial_threshold:
        interpretive_status = "core_computational_mapping_thread"
    elif mapping_score >= config.core_threshold:
        interpretive_status = "major_computational_mapping_thread"
    else:
        interpretive_status = "supporting_computational_mapping_thread"

    return {
        "theme_id": row["theme_id"],
        "spatial_representation": round(float(row["spatial_representation"]), 6),
        "coordinate_structure": round(float(row["coordinate_structure"]), 6),
        "procedural_clarity": round(float(row["procedural_clarity"]), 6),
        "institutional_use": round(float(row["institutional_use"]), 6),
        "correction_awareness": round(float(row["correction_awareness"]), 6),
        "transmission_importance": round(float(row["transmission_importance"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "mapping_score": round(mapping_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_maps_as_mirrors", "meaning": "Maps are constructed representations shaped by projection, scale, selection, and purpose."},
        {"caution": "do_not_treat_coordinates_as_context_free", "meaning": "Coordinates depend on reference systems, measurement practices, copying, and correction."},
        {"caution": "do_not_reduce_islamic_geography_to_preservation", "meaning": "Islamic-world geography inherited, corrected, extended, and synthesized earlier materials."},
        {"caution": "do_not_ignore_routes_and_networks", "meaning": "Geographic computation includes movement, sequence, distance, and connection."},
        {"caution": "do_not_project_modern_gis_backward", "meaning": "Medieval coordinate lists and maps are spatial-computational artifacts, but not modern GIS."},
    ]


def main() -> None:
    config = ComputationalMappingConfig()
    themes = computational_mapping_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_computational_mapping_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_computational_mapping_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_computational_mapping_thread"),
        "mean_mapping_score": round(mean(float(row["mapping_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Computational mapping should be studied as spatial algorithmic reasoning: coordinates, routes, regions, projections, correction, transmission, and institutional use.",
    }

    write_csv(TABLES / "computational_mapping_themes.csv", themes)
    write_csv(TABLES / "computational_mapping_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "computational_mapping_summary.csv", [summary])

    write_json(JSON_DIR / "computational_mapping_config.json", asdict(config))
    write_json(JSON_DIR / "computational_mapping_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "computational_mapping_summary.json", summary)

    print("Geography, coordinates, and computational mapping map complete.")
    print(TABLES / "computational_mapping_summary.csv")


if __name__ == "__main__":
    main()
