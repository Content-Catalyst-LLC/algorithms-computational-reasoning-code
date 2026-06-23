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
class ChurchConfig:
    article: str = "alonzo_church_lambda_calculus_and_formal_computation"
    core_threshold: float = 0.80
    high_formalization_threshold: float = 0.86


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


def church_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "lambda_calculus_core", "formalization": 0.98, "functional_abstraction": 0.98, "symbolic_transformation": 0.98, "substitution": 0.96, "reduction": 0.96, "computability": 0.96, "undecidability": 0.86, "type_influence": 0.88, "programming_relevance": 0.98, "ai_caution": 0.86},
        {"theme_id": "effective_calculability", "formalization": 0.98, "functional_abstraction": 0.94, "symbolic_transformation": 0.94, "substitution": 0.90, "reduction": 0.92, "computability": 0.98, "undecidability": 0.92, "type_influence": 0.82, "programming_relevance": 0.92, "ai_caution": 0.90},
        {"theme_id": "entscheidungsproblem_undecidability", "formalization": 0.98, "functional_abstraction": 0.88, "symbolic_transformation": 0.92, "substitution": 0.86, "reduction": 0.88, "computability": 0.98, "undecidability": 0.98, "type_influence": 0.78, "programming_relevance": 0.88, "ai_caution": 0.96},
        {"theme_id": "church_turing_convergence", "formalization": 0.98, "functional_abstraction": 0.94, "symbolic_transformation": 0.94, "substitution": 0.86, "reduction": 0.90, "computability": 0.98, "undecidability": 0.94, "type_influence": 0.82, "programming_relevance": 0.94, "ai_caution": 0.92},
        {"theme_id": "church_numerals_encoding", "formalization": 0.92, "functional_abstraction": 0.98, "symbolic_transformation": 0.96, "substitution": 0.94, "reduction": 0.94, "computability": 0.94, "undecidability": 0.76, "type_influence": 0.84, "programming_relevance": 0.96, "ai_caution": 0.82},
        {"theme_id": "recursion_fixed_points", "formalization": 0.94, "functional_abstraction": 0.98, "symbolic_transformation": 0.98, "substitution": 0.96, "reduction": 0.98, "computability": 0.96, "undecidability": 0.88, "type_influence": 0.86, "programming_relevance": 0.98, "ai_caution": 0.86},
        {"theme_id": "type_theory_and_proofs", "formalization": 0.96, "functional_abstraction": 0.92, "symbolic_transformation": 0.90, "substitution": 0.88, "reduction": 0.88, "computability": 0.88, "undecidability": 0.78, "type_influence": 0.98, "programming_relevance": 0.94, "ai_caution": 0.92},
        {"theme_id": "functional_programming_legacy", "formalization": 0.88, "functional_abstraction": 0.98, "symbolic_transformation": 0.92, "substitution": 0.86, "reduction": 0.92, "computability": 0.90, "undecidability": 0.74, "type_influence": 0.92, "programming_relevance": 0.98, "ai_caution": 0.84},
    ]


def score_theme(row: dict[str, object], config: ChurchConfig) -> dict[str, object]:
    formal_score = mean([
        float(row["formalization"]),
        float(row["functional_abstraction"]),
        float(row["symbolic_transformation"]),
        float(row["substitution"]),
        float(row["reduction"]),
        float(row["computability"]),
        float(row["undecidability"]),
        float(row["type_influence"]),
        float(row["programming_relevance"]),
        float(row["ai_caution"]),
    ])

    if formal_score >= config.core_threshold and float(row["formalization"]) >= config.high_formalization_threshold:
        interpretive_status = "core_church_formal_computation_thread"
    elif formal_score >= config.core_threshold:
        interpretive_status = "major_church_formal_computation_thread"
    else:
        interpretive_status = "supporting_church_formal_computation_thread"

    return {
        "theme_id": row["theme_id"],
        "formalization": round(float(row["formalization"]), 6),
        "functional_abstraction": round(float(row["functional_abstraction"]), 6),
        "symbolic_transformation": round(float(row["symbolic_transformation"]), 6),
        "substitution": round(float(row["substitution"]), 6),
        "reduction": round(float(row["reduction"]), 6),
        "computability": round(float(row["computability"]), 6),
        "undecidability": round(float(row["undecidability"]), 6),
        "type_influence": round(float(row["type_influence"]), 6),
        "programming_relevance": round(float(row["programming_relevance"]), 6),
        "ai_caution": round(float(row["ai_caution"]), 6),
        "formal_score": round(formal_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_lambda_calculus_as_ordinary_algebra", "meaning": "Lambda calculus is a formal system of functions, application, abstraction, and reduction."},
        {"caution": "do_not_confuse_lambda_calculus_with_machine_hardware", "meaning": "Church models computation through expressions, not physical machines."},
        {"caution": "do_not_ignore_binding_and_scope", "meaning": "Substitution requires careful handling of free and bound variables."},
        {"caution": "do_not_treat_church_turing_thesis_as_simple_theorem", "meaning": "The thesis connects informal effective calculability with formal models."},
        {"caution": "do_not_forget_undecidability", "meaning": "Church's legacy includes formal limits on general decision procedure."},
    ]


def main() -> None:
    config = ChurchConfig()
    themes = church_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_church_formal_computation_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_church_formal_computation_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_church_formal_computation_thread"),
        "mean_formal_score": round(mean(float(row["formal_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Church should be studied as a bridge between functions, formal calculation, lambda reduction, undecidability, type theory, and programming-language foundations.",
    }

    write_csv(TABLES / "church_themes.csv", themes)
    write_csv(TABLES / "church_formal_computation_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "church_formal_computation_summary.csv", [summary])

    write_json(JSON_DIR / "church_config.json", asdict(config))
    write_json(JSON_DIR / "church_formal_computation_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "church_formal_computation_summary.json", summary)

    print("Church formal computation map complete.")
    print(TABLES / "church_formal_computation_summary.csv")


if __name__ == "__main__":
    main()
