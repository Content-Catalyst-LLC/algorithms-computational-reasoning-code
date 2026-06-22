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
class KnowledgeArchitectureConfig:
    article: str = "algorithms_in_knowledge_architecture"
    low_readiness_threshold: float = 0.65
    high_maintenance_risk_threshold: float = 0.70
    high_representation_risk_threshold: float = 0.70


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


def knowledge_objects() -> list[dict[str, object]]:
    return [
        {"object_id": "article_map_algorithms", "metadata_completeness": 0.92, "taxonomy_fit": 0.88, "search_readiness": 0.86, "link_quality": 0.90, "recommendation_quality": 0.82, "provenance": 0.86, "freshness": 0.84, "editorial_review": 0.90, "representation_risk": 0.28},
        {"object_id": "legacy_policy_archive", "metadata_completeness": 0.46, "taxonomy_fit": 0.52, "search_readiness": 0.48, "link_quality": 0.38, "recommendation_quality": 0.40, "provenance": 0.44, "freshness": 0.32, "editorial_review": 0.42, "representation_risk": 0.74},
        {"object_id": "cross_domain_methods_cluster", "metadata_completeness": 0.72, "taxonomy_fit": 0.66, "search_readiness": 0.74, "link_quality": 0.80, "recommendation_quality": 0.78, "provenance": 0.70, "freshness": 0.68, "editorial_review": 0.74, "representation_risk": 0.52},
        {"object_id": "automated_recommendation_pathway", "metadata_completeness": 0.78, "taxonomy_fit": 0.70, "search_readiness": 0.82, "link_quality": 0.64, "recommendation_quality": 0.62, "provenance": 0.76, "freshness": 0.80, "editorial_review": 0.58, "representation_risk": 0.72},
    ]


def score_object(row: dict[str, object], config: KnowledgeArchitectureConfig) -> dict[str, object]:
    architecture_readiness = mean([
        float(row["metadata_completeness"]),
        float(row["taxonomy_fit"]),
        float(row["search_readiness"]),
        float(row["link_quality"]),
        float(row["recommendation_quality"]),
        float(row["provenance"]),
        float(row["editorial_review"]),
    ])
    maintenance_risk = mean([
        1.0 - float(row["metadata_completeness"]),
        1.0 - float(row["link_quality"]),
        1.0 - float(row["freshness"]),
        1.0 - float(row["provenance"]),
    ])
    governance_readiness = mean([
        float(row["provenance"]),
        float(row["editorial_review"]),
        float(row["metadata_completeness"]),
        float(row["freshness"]),
    ])

    recommendation = "knowledge_architecture_ready"
    if architecture_readiness < config.low_readiness_threshold and maintenance_risk >= config.high_maintenance_risk_threshold:
        recommendation = "rebuild_before_algorithmic_discovery"
    elif float(row["representation_risk"]) >= config.high_representation_risk_threshold:
        recommendation = "editorial_governance_review_required"
    elif architecture_readiness < config.low_readiness_threshold:
        recommendation = "metadata_and_linking_review_required"
    elif maintenance_risk >= config.high_maintenance_risk_threshold:
        recommendation = "maintenance_backlog_review_required"

    return {
        "object_id": row["object_id"],
        "metadata_completeness": round(float(row["metadata_completeness"]), 6),
        "taxonomy_fit": round(float(row["taxonomy_fit"]), 6),
        "search_readiness": round(float(row["search_readiness"]), 6),
        "link_quality": round(float(row["link_quality"]), 6),
        "recommendation_quality": round(float(row["recommendation_quality"]), 6),
        "provenance": round(float(row["provenance"]), 6),
        "freshness": round(float(row["freshness"]), 6),
        "editorial_review": round(float(row["editorial_review"]), 6),
        "representation_risk": round(float(row["representation_risk"]), 6),
        "architecture_readiness_score": round(architecture_readiness, 6),
        "maintenance_risk_score": round(maintenance_risk, 6),
        "governance_readiness_score": round(governance_readiness, 6),
        "recommendation": recommendation,
    }


def knowledge_architecture_register() -> list[dict[str, str]]:
    return [
        {"control": "taxonomy_register", "review_question": "Are categories, hierarchy, alternatives, and revisions documented?", "status": "required"},
        {"control": "metadata_schema", "review_question": "Are required fields, validation rules, and provenance fields defined?", "status": "required"},
        {"control": "search_evaluation", "review_question": "Are retrieval quality, ranking signals, and failure cases reviewed?", "status": "required"},
        {"control": "link_graph_audit", "review_question": "Do internal links support learning, navigation, and conceptual clarity?", "status": "required"},
        {"control": "recommendation_review", "review_question": "Do recommendations widen understanding rather than merely optimize engagement?", "status": "required"},
        {"control": "maintenance_workflow", "review_question": "Are stale content, broken links, duplicates, and metadata gaps reviewed?", "status": "required"},
        {"control": "editorial_governance", "review_question": "Can human editors approve, revise, reject, and document algorithmic suggestions?", "status": "required"},
    ]


def main() -> None:
    config = KnowledgeArchitectureConfig()
    objects = knowledge_objects()
    audit = [score_object(row, config) for row in objects]
    controls = knowledge_architecture_register()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "objects_reviewed": len(audit),
        "objects_ready": sum(1 for row in audit if row["recommendation"] == "knowledge_architecture_ready"),
        "objects_requiring_editorial_review": sum(1 for row in audit if row["recommendation"] == "editorial_governance_review_required"),
        "objects_requiring_metadata_or_link_review": sum(1 for row in audit if row["recommendation"] == "metadata_and_linking_review_required"),
        "objects_requiring_rebuild": sum(1 for row in audit if row["recommendation"] == "rebuild_before_algorithmic_discovery"),
        "mean_architecture_readiness_score": round(mean(float(row["architecture_readiness_score"]) for row in audit), 6),
        "mean_maintenance_risk_score": round(mean(float(row["maintenance_risk_score"]) for row in audit), 6),
        "mean_governance_readiness_score": round(mean(float(row["governance_readiness_score"]) for row in audit), 6),
        "governance_controls": len(controls),
        "interpretation": "Knowledge architecture review should connect classification, metadata, search, linking, recommendation, provenance, maintenance, representation risk, and editorial governance.",
    }

    write_csv(TABLES / "knowledge_objects.csv", objects)
    write_csv(TABLES / "knowledge_architecture_audit.csv", audit)
    write_csv(TABLES / "knowledge_architecture_register.csv", controls)
    write_csv(TABLES / "knowledge_architecture_summary.csv", [summary])

    write_json(JSON_DIR / "knowledge_architecture_config.json", asdict(config))
    write_json(JSON_DIR / "knowledge_architecture_audit.json", audit)
    write_json(JSON_DIR / "knowledge_architecture_register.json", controls)
    write_json(JSON_DIR / "knowledge_architecture_summary.json", summary)

    print("Algorithms in knowledge architecture audit complete.")
    print(TABLES / "knowledge_architecture_summary.csv")


if __name__ == "__main__":
    main()
