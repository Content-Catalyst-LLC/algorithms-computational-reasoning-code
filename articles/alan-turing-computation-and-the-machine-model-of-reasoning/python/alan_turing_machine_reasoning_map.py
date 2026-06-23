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
class TuringConfig:
    article: str = "alan_turing_computation_and_the_machine_model_of_reasoning"
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


def turing_themes() -> list[dict[str, object]]:
    return [
        {"theme_id": "effective_procedure", "formalization": 0.98, "machine_abstraction": 0.92, "symbolic_representation": 0.92, "universality": 0.76, "decidability": 0.86, "limit_awareness": 0.92, "reasoning_relevance": 0.98, "ai_relevance": 0.78, "governance_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "turing_machine_model", "formalization": 0.98, "machine_abstraction": 0.98, "symbolic_representation": 0.96, "universality": 0.86, "decidability": 0.90, "limit_awareness": 0.92, "reasoning_relevance": 0.96, "ai_relevance": 0.82, "governance_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "human_computer_abstraction", "formalization": 0.92, "machine_abstraction": 0.96, "symbolic_representation": 0.92, "universality": 0.78, "decidability": 0.82, "limit_awareness": 0.88, "reasoning_relevance": 0.96, "ai_relevance": 0.80, "governance_caution": 0.84, "modern_resonance": 0.94},
        {"theme_id": "universal_machine", "formalization": 0.96, "machine_abstraction": 0.98, "symbolic_representation": 0.96, "universality": 0.98, "decidability": 0.88, "limit_awareness": 0.90, "reasoning_relevance": 0.94, "ai_relevance": 0.86, "governance_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "undecidability_and_limits", "formalization": 0.98, "machine_abstraction": 0.92, "symbolic_representation": 0.90, "universality": 0.86, "decidability": 0.98, "limit_awareness": 0.98, "reasoning_relevance": 0.96, "ai_relevance": 0.86, "governance_caution": 0.96, "modern_resonance": 0.98},
        {"theme_id": "halting_problem", "formalization": 0.98, "machine_abstraction": 0.94, "symbolic_representation": 0.92, "universality": 0.90, "decidability": 0.98, "limit_awareness": 0.98, "reasoning_relevance": 0.96, "ai_relevance": 0.84, "governance_caution": 0.96, "modern_resonance": 0.98},
        {"theme_id": "church_turing_thesis", "formalization": 0.96, "machine_abstraction": 0.90, "symbolic_representation": 0.94, "universality": 0.92, "decidability": 0.90, "limit_awareness": 0.92, "reasoning_relevance": 0.96, "ai_relevance": 0.82, "governance_caution": 0.86, "modern_resonance": 0.98},
        {"theme_id": "imitation_game_machine_intelligence", "formalization": 0.82, "machine_abstraction": 0.84, "symbolic_representation": 0.88, "universality": 0.76, "decidability": 0.74, "limit_awareness": 0.88, "reasoning_relevance": 0.90, "ai_relevance": 0.98, "governance_caution": 0.94, "modern_resonance": 0.98},
        {"theme_id": "ai_caution_after_turing", "formalization": 0.86, "machine_abstraction": 0.88, "symbolic_representation": 0.88, "universality": 0.86, "decidability": 0.88, "limit_awareness": 0.98, "reasoning_relevance": 0.94, "ai_relevance": 0.98, "governance_caution": 0.98, "modern_resonance": 0.98},
    ]


def score_theme(row: dict[str, object], config: TuringConfig) -> dict[str, object]:
    reasoning_score = mean([
        float(row["formalization"]),
        float(row["machine_abstraction"]),
        float(row["symbolic_representation"]),
        float(row["universality"]),
        float(row["decidability"]),
        float(row["limit_awareness"]),
        float(row["reasoning_relevance"]),
        float(row["ai_relevance"]),
        float(row["governance_caution"]),
        float(row["modern_resonance"]),
    ])

    if reasoning_score >= config.core_threshold and float(row["formalization"]) >= config.high_formalization_threshold:
        interpretive_status = "core_turing_machine_reasoning_thread"
    elif reasoning_score >= config.core_threshold:
        interpretive_status = "major_turing_machine_reasoning_thread"
    else:
        interpretive_status = "supporting_turing_machine_reasoning_thread"

    return {
        "theme_id": row["theme_id"],
        "formalization": round(float(row["formalization"]), 6),
        "machine_abstraction": round(float(row["machine_abstraction"]), 6),
        "symbolic_representation": round(float(row["symbolic_representation"]), 6),
        "universality": round(float(row["universality"]), 6),
        "decidability": round(float(row["decidability"]), 6),
        "limit_awareness": round(float(row["limit_awareness"]), 6),
        "reasoning_relevance": round(float(row["reasoning_relevance"]), 6),
        "ai_relevance": round(float(row["ai_relevance"]), 6),
        "governance_caution": round(float(row["governance_caution"]), 6),
        "modern_resonance": round(float(row["modern_resonance"]), 6),
        "reasoning_score": round(reasoning_score, 6),
        "interpretive_status": interpretive_status,
    }


def interpretation_cautions() -> list[dict[str, str]]:
    return [
        {"caution": "do_not_treat_turing_machine_as_physical_laptop", "meaning": "A Turing machine is an abstract model, not an engineering design."},
        {"caution": "do_not_claim_all_reasoning_is_computation", "meaning": "Turing formalizes effective procedure, not every form of human judgment."},
        {"caution": "do_not_ignore_undecidability", "meaning": "Turing's legacy includes limits of automation."},
        {"caution": "do_not_reduce_turing_to_ai_slogan", "meaning": "The imitation game is important but not a complete theory of intelligence."},
        {"caution": "do_not_confuse_computability_with_feasibility", "meaning": "A computable task may still be impractical because of time, memory, or context."},
    ]


def main() -> None:
    config = TuringConfig()
    themes = turing_themes()
    scored = [score_theme(row, config) for row in themes]
    cautions = interpretation_cautions()

    summary = {
        "article": config.article,
        "timestamp_utc": timestamp_utc(),
        "themes_reviewed": len(scored),
        "core_threads": sum(1 for row in scored if row["interpretive_status"] == "core_turing_machine_reasoning_thread"),
        "major_threads": sum(1 for row in scored if row["interpretive_status"] == "major_turing_machine_reasoning_thread"),
        "supporting_threads": sum(1 for row in scored if row["interpretive_status"] == "supporting_turing_machine_reasoning_thread"),
        "mean_reasoning_score": round(mean(float(row["reasoning_score"]) for row in scored), 6),
        "cautions": len(cautions),
        "interpretation": "Turing should be studied as a bridge between effective procedure, machine abstraction, universal computation, formal limits, and AI-era caution.",
    }

    write_csv(TABLES / "turing_themes.csv", themes)
    write_csv(TABLES / "turing_machine_reasoning_map.csv", scored)
    write_csv(TABLES / "interpretation_cautions.csv", cautions)
    write_csv(TABLES / "turing_reasoning_summary.csv", [summary])

    write_json(JSON_DIR / "turing_config.json", asdict(config))
    write_json(JSON_DIR / "turing_machine_reasoning_map.json", scored)
    write_json(JSON_DIR / "interpretation_cautions.json", cautions)
    write_json(JSON_DIR / "turing_reasoning_summary.json", summary)

    print("Turing machine reasoning map complete.")
    print(TABLES / "turing_reasoning_summary.csv")


if __name__ == "__main__":
    main()
