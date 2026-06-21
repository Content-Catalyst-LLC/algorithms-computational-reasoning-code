from __future__ import annotations

from pathlib import Path
import csv
import json
from datetime import datetime, timezone

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
JSON_DIR = ARTICLE_ROOT / "outputs" / "json"


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = [
        {
            "target_effect": "support_intensity -> outcome",
            "candidate_adjustment": "baseline_need, access_barrier, service_quality",
            "blocks_confounding": "partial",
            "collider_warning": "Do not adjust for downstream decision score.",
            "mediator_warning": "Service quality may be mediator for some support interventions.",
            "review_status": "needs_domain_review",
        },
        {
            "target_effect": "access_barrier_reduction -> outcome",
            "candidate_adjustment": "baseline_need, prior institutional context",
            "blocks_confounding": "partial",
            "collider_warning": "Do not condition on receiving service after the intervention.",
            "mediator_warning": "Support intensity may mediate barrier reduction effects.",
            "review_status": "needs_measurement_review",
        },
        {
            "target_effect": "service_quality -> outcome",
            "candidate_adjustment": "baseline_need, access_barrier, staffing context",
            "blocks_confounding": "partial",
            "collider_warning": "Outcome-based quality flags may be colliders.",
            "mediator_warning": "Quality may mediate institutional redesign effects.",
            "review_status": "needs_temporal_review",
        },
        {
            "target_effect": "threshold_rule_change -> action_rate",
            "candidate_adjustment": "case mix and historical score distribution",
            "blocks_confounding": "not_applicable_rule_change",
            "collider_warning": "Changing the rule does not change underlying need.",
            "mediator_warning": "Downstream resource allocation may mediate outcomes.",
            "review_status": "governance_review_required",
        },
    ]
    write_csv(TABLES / "adjustment_set_review.csv", rows)
    JSON_DIR.mkdir(parents=True, exist_ok=True)
    (JSON_DIR / "adjustment_set_review.json").write_text(json.dumps({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "items": rows,
        "interpretation": "Adjustment review records graph assumptions and warnings; it does not prove identification.",
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(TABLES / "adjustment_set_review.csv")


if __name__ == "__main__":
    main()
