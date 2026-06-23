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
class ReceptionConfig:
    article: str = "from_baghdad_to_latin_europe_algorism_algebra_and_reception"
    core_threshold: float = 0.80
    high_portability_threshold: float = 0.86


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


def reception_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "algorism_written_arithmetic", "procedural_portability": 0.98, "notation_change": 0.98, "translation_pathway": 0.92, "teaching_value": 0.96, "practical_utility": 0.96, "institutional_adoption": 0.92, "trust_verification": 0.90, "historical_significance": 0.98, "ethical_caution": 0.84, "modern_resonance": 0.98},
        {"theme_id": "algebra_rule_governed_problem_solving", "procedural_portability": 0.96, "notation_change": 0.88, "translation_pathway": 0.94, "teaching_value": 0.94, "practical_utility": 0.92, "institutional_adoption": 0.90, "trust_verification": 0.92, "historical_significance": 0.98, "ethical_caution": 0.84, "modern_resonance": 0.96},
        {"theme_id": "hindu_arabic_numerals_place_value_zero", "procedural_portability": 0.98, "notation_change": 0.98, "translation_pathway": 0.94, "teaching_value": 0.94, "practical_utility": 0.98, "institutional_adoption": 0.92, "trust_verification": 0.90, "historical_significance": 0.98, "ethical_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "toledo_and_arabic_latin_transfer", "procedural_portability": 0.92, "notation_change": 0.88, "translation_pathway": 0.98, "teaching_value": 0.88, "practical_utility": 0.88, "institutional_adoption": 0.94, "trust_verification": 0.88, "historical_significance": 0.96, "ethical_caution": 0.88, "modern_resonance": 0.94},
        {"theme_id": "fibonacci_liber_abaci_commerce", "procedural_portability": 0.96, "notation_change": 0.96, "translation_pathway": 0.90, "teaching_value": 0.98, "practical_utility": 0.98, "institutional_adoption": 0.94, "trust_verification": 0.92, "historical_significance": 0.96, "ethical_caution": 0.86, "modern_resonance": 0.96},
        {"theme_id": "abacus_culture_reception_resistance", "procedural_portability": 0.88, "notation_change": 0.92, "translation_pathway": 0.84, "teaching_value": 0.90, "practical_utility": 0.94, "institutional_adoption": 0.90, "trust_verification": 0.96, "historical_significance": 0.92, "ethical_caution": 0.88, "modern_resonance": 0.94},
        {"theme_id": "origin_story_caution", "procedural_portability": 0.86, "notation_change": 0.86, "translation_pathway": 0.92, "teaching_value": 0.86, "practical_utility": 0.84, "institutional_adoption": 0.86, "trust_verification": 0.90, "historical_significance": 0.94, "ethical_caution": 0.98, "modern_resonance": 0.94},
    ]


def score_theme(row: dict[str, object], config: ReceptionConfig) -> dict[str, object]:
    reception_score = mean([
        float(row["procedural_portability"]),
        float(row["notation_change"]),
        float(row["translation_pathway"]),
        float(row["teaching_value"]),
        float(row["practical_utility"]),
        float(row["institutional_adoption"]),
        float(row["trust_verification"]),
        float(row["historical_significance"]),
        float(row["ethical_caution"]),
        float(row["modern_resonance"]),
    ])

    if reception_score >= config.core_threshold and float(row["procedural_portability"]) >= config.high_portability_threshold:
        interpretive_status = "core_algorism_algebra_reception_thread"
    elif reception_score >= config.core_threshold:
        interpretive_status = "major_algorism_algebra_reception_thread"
    else:
        interpretive_status = "supporting_algorism_algebra_reception_thread"

    return {
        "theme_id": row["theme_id"],
        "procedural_portability": round(float(row["procedural_portability"]), 6),
        "notation_change": round(float(row["notation_change"]), 6),
        "translation_pathway": round(float(row["translation_pathway"]), 6),
        "teaching_value": round(float(row["teaching_value"]), 6),
        "practical_utility": round(float(row["practical_utility"]), 6),
        "institutional_adoption": round(float(row["institutional_adoption"]), 6),
        "trust_verification": round(float(row["trust_verification"]), 6),
        "historical_significance": round(float(row["historical_significance"]), 6),
        "ethical_caution": round(float(row["ethical_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "reception_score": round(reception_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_make_borrowing_passive", "meaning": "Latin Europe received, adapted, taught, resisted, and institutionalized methods."},
        {"caution": "do_not_erase_arabic_and_indian_transmission", "meaning": "Hindu-Arabic numerals and Arabic mathematical traditions are central to the pathway."},
        {"caution": "do_not_claim_fibonacci_singlehandedly_introduced_numerals", "meaning": "Fibonacci was a major popularizer, but transmission involved broader networks."},
        {"caution": "do_not_reduce_algorithm_to_etymology", "meaning": "The word history matters, but algorithmic reasoning also depends on procedures and institutions."},
        {"caution": "do_not_treat_algebra_as_symbolic_from_the_start", "meaning": "Early algebraic reception was often verbal, case-based, geometric, and procedural."},
    ]


def main() -> None:
    config = ReceptionConfig()
    themes = reception_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_algorism_algebra_reception_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_algorism_algebra_reception_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_algorism_algebra_reception_thread"),
        "mean_reception_score": round(mean(float(row["reception_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Algorism and algebra should be studied as received computational methods: translated, taught, practiced, trusted, resisted, adapted, and institutionalized across Latin Europe.",
    }

    write_csv(TABLES / "reception_themes.csv", themes)
    write_csv(TABLES / "reception_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "reception_summary.csv", [summary])

    write_json(JSON_DIR / "reception_config.json", asdict(config))
    write_json(JSON_DIR / "reception_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "reception_summary.json", summary)

    print("From Baghdad to Latin Europe algorism, algebra, and reception map complete.")
    print(TABLES / "reception_summary.csv")


if __name__ == "__main__":
    main()
