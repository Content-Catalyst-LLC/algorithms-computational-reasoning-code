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
class KhwarizmiMethodConfig:
    article: str = "al_khwarizmi_and_the_historical_roots_of_algorithmic_method"
    core_threshold: float = 0.80
    high_method_threshold: float = 0.86


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


def khwarizmi_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "algorism_written_calculation", "arithmetic_method": 0.98, "algebraic_procedure": 0.76, "representation": 0.98, "transformation": 0.88, "proof_relation": 0.78, "transmission": 0.98, "etymology": 0.98, "institutional_adoption": 0.94, "historiographic_caution": 0.92, "modern_resonance": 0.98},
        {"theme_id": "algebra_case_based_method", "arithmetic_method": 0.86, "algebraic_procedure": 0.98, "representation": 0.92, "transformation": 0.98, "proof_relation": 0.92, "transmission": 0.94, "etymology": 0.88, "institutional_adoption": 0.92, "historiographic_caution": 0.92, "modern_resonance": 0.98},
        {"theme_id": "al_jabr_al_muqabalah_transformation", "arithmetic_method": 0.82, "algebraic_procedure": 0.98, "representation": 0.90, "transformation": 0.98, "proof_relation": 0.90, "transmission": 0.94, "etymology": 0.92, "institutional_adoption": 0.92, "historiographic_caution": 0.92, "modern_resonance": 0.96},
        {"theme_id": "unknown_root_square_number", "arithmetic_method": 0.82, "algebraic_procedure": 0.96, "representation": 0.94, "transformation": 0.94, "proof_relation": 0.90, "transmission": 0.92, "etymology": 0.84, "institutional_adoption": 0.90, "historiographic_caution": 0.94, "modern_resonance": 0.96},
        {"theme_id": "geometric_demonstration_correctness", "arithmetic_method": 0.72, "algebraic_procedure": 0.92, "representation": 0.90, "transformation": 0.92, "proof_relation": 0.98, "transmission": 0.86, "etymology": 0.72, "institutional_adoption": 0.86, "historiographic_caution": 0.92, "modern_resonance": 0.94},
        {"theme_id": "astronomy_geography_tables", "arithmetic_method": 0.90, "algebraic_procedure": 0.68, "representation": 0.96, "transformation": 0.82, "proof_relation": 0.80, "transmission": 0.92, "etymology": 0.70, "institutional_adoption": 0.90, "historiographic_caution": 0.90, "modern_resonance": 0.92},
        {"theme_id": "latin_reception_word_algorithm", "arithmetic_method": 0.92, "algebraic_procedure": 0.86, "representation": 0.92, "transformation": 0.86, "proof_relation": 0.76, "transmission": 0.98, "etymology": 0.98, "institutional_adoption": 0.96, "historiographic_caution": 0.98, "modern_resonance": 0.98},
        {"theme_id": "myth_correction_precise_legacy", "arithmetic_method": 0.82, "algebraic_procedure": 0.82, "representation": 0.82, "transformation": 0.82, "proof_relation": 0.82, "transmission": 0.90, "etymology": 0.92, "institutional_adoption": 0.88, "historiographic_caution": 0.98, "modern_resonance": 0.96},
    ]


def score_theme(row: dict[str, object], config: KhwarizmiMethodConfig) -> dict[str, object]:
    method_score = mean([
        float(row["arithmetic_method"]),
        float(row["algebraic_procedure"]),
        float(row["representation"]),
        float(row["transformation"]),
        float(row["proof_relation"]),
        float(row["transmission"]),
        float(row["etymology"]),
        float(row["institutional_adoption"]),
        float(row["historiographic_caution"]),
        float(row["modern_resonance"]),
    ])

    if method_score >= config.core_threshold and max(float(row["arithmetic_method"]), float(row["algebraic_procedure"])) >= config.high_method_threshold:
        interpretive_status = "core_khwarizmi_algorithmic_method_thread"
    elif method_score >= config.core_threshold:
        interpretive_status = "major_khwarizmi_algorithmic_method_thread"
    else:
        interpretive_status = "supporting_khwarizmi_algorithmic_method_thread"

    return {
        "theme_id": row["theme_id"],
        "arithmetic_method": round(float(row["arithmetic_method"]), 6),
        "algebraic_procedure": round(float(row["algebraic_procedure"]), 6),
        "representation": round(float(row["representation"]), 6),
        "transformation": round(float(row["transformation"]), 6),
        "proof_relation": round(float(row["proof_relation"]), 6),
        "transmission": round(float(row["transmission"]), 6),
        "etymology": round(float(row["etymology"]), 6),
        "institutional_adoption": round(float(row["institutional_adoption"]), 6),
        "historiographic_caution": round(float(row["historiographic_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "method_score": round(method_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_claim_al_khwarizmi_invented_all_algorithms", "meaning": "His name is central to algorithm word history, but procedural reasoning is broader and older."},
        {"caution": "do_not_reduce_his_legacy_to_etymology", "meaning": "His arithmetic and algebraic methods matter beyond the word algorithm."},
        {"caution": "do_not_ignore_indian_numeration", "meaning": "Hindu-Arabic numerals and place value have their own history."},
        {"caution": "do_not_project_modern_code_backward", "meaning": "Al-Khwārizmī used verbal and geometric procedures, not programming languages."},
        {"caution": "do_not_describe_him_as_only_preserving_knowledge", "meaning": "Transmission, organization, exposition, and systematization are creative intellectual acts."},
    ]


def main() -> None:
    config = KhwarizmiMethodConfig()
    themes = khwarizmi_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_khwarizmi_algorithmic_method_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_khwarizmi_algorithmic_method_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_khwarizmi_algorithmic_method_thread"),
        "mean_method_score": round(mean(float(row["method_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Al-Khwārizmī should be studied as a decisive bridge in algorithmic method: algorism, algebra, transformation, representation, transmission, and careful historical memory.",
    }

    write_csv(TABLES / "khwarizmi_themes.csv", themes)
    write_csv(TABLES / "khwarizmi_algorithmic_method_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "khwarizmi_method_summary.csv", [summary])

    write_json(JSON_DIR / "khwarizmi_method_config.json", asdict(config))
    write_json(JSON_DIR / "khwarizmi_algorithmic_method_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "khwarizmi_method_summary.json", summary)

    print("Al-Khwārizmī algorithmic method map complete.")
    print(TABLES / "khwarizmi_method_summary.csv")


if __name__ == "__main__":
    main()
