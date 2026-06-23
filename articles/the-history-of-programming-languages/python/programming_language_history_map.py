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
class LanguageHistoryConfig:
    article: str = "the_history_of_programming_languages"
    core_threshold: float = 0.80
    high_influence_threshold: float = 0.86


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


def language_traditions() -> list[dict[str, object]]:
    return [
        {"tradition_id": "machine_code_assembly", "abstraction": 0.30, "performance_orientation": 0.98, "readability": 0.35, "formal_specification": 0.70, "ecosystem_depth": 0.80, "domain_fit": 0.70, "safety_orientation": 0.30, "institutional_adoption": 0.90, "historical_influence": 0.98, "governance_caution": 0.96},
        {"tradition_id": "fortran_scientific_programming", "abstraction": 0.82, "performance_orientation": 0.96, "readability": 0.76, "formal_specification": 0.78, "ecosystem_depth": 0.92, "domain_fit": 0.98, "safety_orientation": 0.48, "institutional_adoption": 0.96, "historical_influence": 0.98, "governance_caution": 0.90},
        {"tradition_id": "lisp_symbolic_computation", "abstraction": 0.96, "performance_orientation": 0.62, "readability": 0.72, "formal_specification": 0.88, "ecosystem_depth": 0.84, "domain_fit": 0.92, "safety_orientation": 0.62, "institutional_adoption": 0.78, "historical_influence": 0.96, "governance_caution": 0.86},
        {"tradition_id": "algol_structured_design", "abstraction": 0.92, "performance_orientation": 0.72, "readability": 0.86, "formal_specification": 0.98, "ecosystem_depth": 0.72, "domain_fit": 0.80, "safety_orientation": 0.70, "institutional_adoption": 0.70, "historical_influence": 0.98, "governance_caution": 0.84},
        {"tradition_id": "cobol_institutional_data_processing", "abstraction": 0.78, "performance_orientation": 0.70, "readability": 0.84, "formal_specification": 0.82, "ecosystem_depth": 0.88, "domain_fit": 0.98, "safety_orientation": 0.62, "institutional_adoption": 0.98, "historical_influence": 0.90, "governance_caution": 0.94},
        {"tradition_id": "c_systems_programming", "abstraction": 0.72, "performance_orientation": 0.98, "readability": 0.70, "formal_specification": 0.84, "ecosystem_depth": 0.98, "domain_fit": 0.94, "safety_orientation": 0.36, "institutional_adoption": 0.98, "historical_influence": 0.98, "governance_caution": 0.98},
        {"tradition_id": "object_oriented_programming", "abstraction": 0.90, "performance_orientation": 0.74, "readability": 0.82, "formal_specification": 0.78, "ecosystem_depth": 0.94, "domain_fit": 0.88, "safety_orientation": 0.70, "institutional_adoption": 0.96, "historical_influence": 0.94, "governance_caution": 0.90},
        {"tradition_id": "declarative_logic_functional", "abstraction": 0.98, "performance_orientation": 0.66, "readability": 0.78, "formal_specification": 0.98, "ecosystem_depth": 0.82, "domain_fit": 0.86, "safety_orientation": 0.90, "institutional_adoption": 0.74, "historical_influence": 0.92, "governance_caution": 0.86},
        {"tradition_id": "sql_database_languages", "abstraction": 0.92, "performance_orientation": 0.84, "readability": 0.82, "formal_specification": 0.90, "ecosystem_depth": 0.98, "domain_fit": 0.98, "safety_orientation": 0.78, "institutional_adoption": 0.98, "historical_influence": 0.94, "governance_caution": 0.96},
        {"tradition_id": "scripting_web_languages", "abstraction": 0.88, "performance_orientation": 0.58, "readability": 0.86, "formal_specification": 0.72, "ecosystem_depth": 0.96, "domain_fit": 0.94, "safety_orientation": 0.56, "institutional_adoption": 0.96, "historical_influence": 0.92, "governance_caution": 0.94},
        {"tradition_id": "python_r_julia_workflows", "abstraction": 0.94, "performance_orientation": 0.78, "readability": 0.92, "formal_specification": 0.76, "ecosystem_depth": 0.98, "domain_fit": 0.98, "safety_orientation": 0.58, "institutional_adoption": 0.96, "historical_influence": 0.92, "governance_caution": 0.94},
        {"tradition_id": "haskell_rust_type_safety", "abstraction": 0.92, "performance_orientation": 0.84, "readability": 0.76, "formal_specification": 0.96, "ecosystem_depth": 0.84, "domain_fit": 0.86, "safety_orientation": 0.98, "institutional_adoption": 0.78, "historical_influence": 0.88, "governance_caution": 0.90},
        {"tradition_id": "ai_generated_code_layer", "abstraction": 0.96, "performance_orientation": 0.70, "readability": 0.72, "formal_specification": 0.68, "ecosystem_depth": 0.88, "domain_fit": 0.88, "safety_orientation": 0.58, "institutional_adoption": 0.92, "historical_influence": 0.88, "governance_caution": 0.98},
    ]


def score_tradition(row: dict[str, object], config: LanguageHistoryConfig) -> dict[str, object]:
    history_score = mean([
        float(row["abstraction"]),
        float(row["performance_orientation"]),
        float(row["readability"]),
        float(row["formal_specification"]),
        float(row["ecosystem_depth"]),
        float(row["domain_fit"]),
        float(row["safety_orientation"]),
        float(row["institutional_adoption"]),
        float(row["historical_influence"]),
        float(row["governance_caution"]),
    ])

    if history_score >= config.core_threshold and float(row["historical_influence"]) >= config.high_influence_threshold:
        interpretive_status = "core_programming_language_history_thread"
    elif history_score >= config.core_threshold:
        interpretive_status = "major_programming_language_history_thread"
    else:
        interpretive_status = "supporting_programming_language_history_thread"

    scored = {key: round(float(row[key]), 6) for key in [
        "abstraction", "performance_orientation", "readability", "formal_specification",
        "ecosystem_depth", "domain_fit", "safety_orientation", "institutional_adoption",
        "historical_influence", "governance_caution"
    ]}
    scored.update({
        "tradition_id": row["tradition_id"],
        "history_score": round(history_score, 6),
        "interpretive_status": interpretive_status,
    })
    return scored


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_language_history_as_progress_only", "meaning": "Newer languages do not simply replace older ones; they solve different problems under different constraints."},
        {"caution": "do_not_reduce_languages_to_syntax", "meaning": "A language includes semantics, runtime, libraries, tools, standards, and communities."},
        {"caution": "do_not_ignore_institutions", "meaning": "Business, science, government, education, and web platforms shape language adoption."},
        {"caution": "do_not_confuse_expressiveness_with_safety", "meaning": "Expressive languages still require tests, review, and operational constraints."},
        {"caution": "do_not_treat_ai_code_generation_as_the_end_of_languages", "meaning": "AI-generated code still depends on languages, ecosystems, runtimes, and governance."},
    ]


def language_family_edges() -> list[dict[str, str]]:
    return [
        {"source": "machine_code_assembly", "target": "fortran_scientific_programming", "relation": "abstraction_from_machine"},
        {"source": "fortran_scientific_programming", "target": "python_r_julia_workflows", "relation": "scientific_workflow_lineage"},
        {"source": "lisp_symbolic_computation", "target": "declarative_logic_functional", "relation": "symbolic_functional_lineage"},
        {"source": "algol_structured_design", "target": "c_systems_programming", "relation": "syntax_and_block_structure_lineage"},
        {"source": "c_systems_programming", "target": "haskell_rust_type_safety", "relation": "safety_response_to_low_level_power"},
        {"source": "cobol_institutional_data_processing", "target": "sql_database_languages", "relation": "institutional_data_lineage"},
        {"source": "object_oriented_programming", "target": "c_systems_programming", "relation": "systems_and_object_hybridization"},
        {"source": "scripting_web_languages", "target": "ai_generated_code_layer", "relation": "rapid_generation_and_glue_code_context"},
    ]


def main() -> None:
    config = LanguageHistoryConfig()
    traditions = language_traditions()
    scored = [score_tradition(row, config) for row in traditions]
    cautions = interpretation_cautions()
    edges = language_family_edges()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "traditions_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_programming_language_history_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_programming_language_history_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_programming_language_history_thread"),
        "mean_history_score": round(mean(float(row["history_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "edges": len(edges),
        "interpretation": "Programming-language history should be studied as a layered history of expression, execution, abstraction, ecosystems, institutions, safety, and governance.",
    }

    write_csv(TABLES / "programming_language_traditions.csv", traditions)
    write_csv(TABLES / "programming_language_history_map.csv", scored)
    write_csv(TABLES / "language_family_edges.csv", edges)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "programming_language_history_summary.csv", [summary])

    write_json(JSON_DIR / "language_history_config.json", asdict(config))
    write_json(JSON_DIR / "programming_language_history_map.json", scored)
    write_json(JSON_DIR / "language_family_edges.json", edges)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "programming_language_history_summary.json", summary)

    print("Programming language history map complete.")
    print(TABLES / "programming_language_history_summary.csv")


if __name__ == "__main__":
    main()
