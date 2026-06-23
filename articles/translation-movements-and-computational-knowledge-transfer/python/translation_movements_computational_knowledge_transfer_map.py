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
class TranslationTransferConfig:
    article: str = "translation_movements_and_computational_knowledge_transfer"
    core_threshold: float = 0.80
    high_fidelity_threshold: float = 0.86


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


def transfer_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "procedural_fidelity", "procedural_fidelity": 0.98, "vocabulary_mapping": 0.90, "diagram_table_preservation": 0.94, "institutional_support": 0.88, "error_control": 0.94, "adaptation": 0.90, "historical_significance": 0.96, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "technical_vocabulary_mapping", "procedural_fidelity": 0.92, "vocabulary_mapping": 0.98, "diagram_table_preservation": 0.86, "institutional_support": 0.86, "error_control": 0.90, "adaptation": 0.92, "historical_significance": 0.94, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "diagrams_tables_nonverbal_knowledge", "procedural_fidelity": 0.94, "vocabulary_mapping": 0.84, "diagram_table_preservation": 0.98, "institutional_support": 0.86, "error_control": 0.96, "adaptation": 0.88, "historical_significance": 0.94, "ethical_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "patronage_libraries_institutions", "procedural_fidelity": 0.88, "vocabulary_mapping": 0.86, "diagram_table_preservation": 0.88, "institutional_support": 0.98, "error_control": 0.88, "adaptation": 0.90, "historical_significance": 0.96, "ethical_caution": 0.86, "modern_resonance": 0.94},
        {"theme_id": "commentary_correction_adaptation", "procedural_fidelity": 0.94, "vocabulary_mapping": 0.92, "diagram_table_preservation": 0.90, "institutional_support": 0.88, "error_control": 0.98, "adaptation": 0.96, "historical_significance": 0.96, "ethical_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "multilingual_relay_networks", "procedural_fidelity": 0.90, "vocabulary_mapping": 0.92, "diagram_table_preservation": 0.88, "institutional_support": 0.94, "error_control": 0.90, "adaptation": 0.94, "historical_significance": 0.98, "ethical_caution": 0.86, "modern_resonance": 0.96},
        {"theme_id": "origin_story_caution", "procedural_fidelity": 0.86, "vocabulary_mapping": 0.86, "diagram_table_preservation": 0.84, "institutional_support": 0.88, "error_control": 0.90, "adaptation": 0.92, "historical_significance": 0.94, "ethical_caution": 0.98, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: TranslationTransferConfig) -> dict[str, object]:
    transfer_score = mean([
        float(row["procedural_fidelity"]),
        float(row["vocabulary_mapping"]),
        float(row["diagram_table_preservation"]),
        float(row["institutional_support"]),
        float(row["error_control"]),
        float(row["adaptation"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if transfer_score >= config.core_threshold and float(row["procedural_fidelity"]) >= config.high_fidelity_threshold:
        interpretive_status = "core_computational_knowledge_transfer_thread"
    elif transfer_score >= config.core_threshold:
        interpretive_status = "major_computational_knowledge_transfer_thread"
    else:
        interpretive_status = "supporting_computational_knowledge_transfer_thread"

    return {
        "theme_id": row["theme_id"],
        "procedural_fidelity": round(float(row["procedural_fidelity"]), 6),
        "vocabulary_mapping": round(float(row["vocabulary_mapping"]), 6),
        "diagram_table_preservation": round(float(row["diagram_table_preservation"]), 6),
        "institutional_support": round(float(row["institutional_support"]), 6),
        "error_control": round(float(row["error_control"]), 6),
        "adaptation": round(float(row["adaptation"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "transfer_score": round(transfer_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_reduce_translation_to_preservation", "meaning": "Translation preserved texts but also transformed, corrected, adapted, and extended them."},
        {"caution": "do_not_center_everything_on_one_institution", "meaning": "Bayt al-Ḥikma matters, but the movement was broader than a single building or legend."},
        {"caution": "do_not_ignore_non_greek_streams", "meaning": "Syriac, Persian, Sanskrit, Hebrew, Arabic, and Latin channels all matter."},
        {"caution": "do_not_treat_translation_as_word_substitution", "meaning": "Technical translation must preserve diagrams, tables, examples, instruments, and procedures."},
        {"caution": "do_not_create_single_origin_myths", "meaning": "Computational knowledge emerged through layered multilingual transmission and recomposition."},
    ]


def main() -> None:
    config = TranslationTransferConfig()
    themes = transfer_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_computational_knowledge_transfer_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_computational_knowledge_transfer_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_computational_knowledge_transfer_thread"),
        "mean_transfer_score": round(mean(float(row["transfer_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Translation movements should be studied as computational knowledge infrastructure: procedural fidelity, vocabulary mapping, diagram and table preservation, institutional support, error control, adaptation, and multilingual relay.",
    }

    write_csv(TABLES / "transfer_themes.csv", themes)
    write_csv(TABLES / "transfer_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "transfer_summary.csv", [summary])

    write_json(JSON_DIR / "transfer_config.json", asdict(config))
    write_json(JSON_DIR / "transfer_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "transfer_summary.json", summary)

    print("Translation movements and computational knowledge transfer map complete.")
    print(TABLES / "transfer_summary.csv")


if __name__ == "__main__":
    main()
