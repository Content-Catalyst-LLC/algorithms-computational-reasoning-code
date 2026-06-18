from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class RelationalQueryCase:
    case_name: str
    system_context: str
    query_question: str
    entity_clarity: float
    relationship_clarity: float
    predicate_precision: float
    join_validity: float
    key_discipline: float
    missingness_handling: float
    aggregation_meaning: float
    query_reproducibility: float
    access_awareness: float
    provenance_connection: float
    recursive_relation_handling: float
    communication_clarity: float

WEIGHTS=[0.10,0.10,0.10,0.10,0.09,0.09,0.08,0.08,0.07,0.07,0.06,0.06]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def query_logic_score(case: RelationalQueryCase) -> float:
    vals=[case.entity_clarity,case.relationship_clarity,case.predicate_precision,case.join_validity,case.key_discipline,case.missingness_handling,case.aggregation_meaning,case.query_reproducibility,case.access_awareness,case.provenance_connection,case.recursive_relation_handling,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def representation_risk(case: RelationalQueryCase) -> float:
    vals=[case.entity_clarity,case.relationship_clarity,case.predicate_precision,case.join_validity,case.key_discipline,case.missingness_handling,case.provenance_connection,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong relational query logic discipline"
    if score >= 70 and risk <= 35:
        return "usable query logic with review needs"
    if risk >= 55:
        return "high risk; query may hide weak relationships, predicates, missingness, or provenance"
    return "partial discipline; strengthen entities, relationships, predicates, joins, keys, and interpretation"

def load_cases(path: Path) -> list[RelationalQueryCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            RelationalQueryCase(
                r["case_name"], r["system_context"], r["query_question"],
                float(r["entity_clarity"]), float(r["relationship_clarity"]),
                float(r["predicate_precision"]), float(r["join_validity"]),
                float(r["key_discipline"]), float(r["missingness_handling"]),
                float(r["aggregation_meaning"]), float(r["query_reproducibility"]),
                float(r["access_awareness"]), float(r["provenance_connection"]),
                float(r["recursive_relation_handling"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def query_logic_calculator(entity: float, relationship: float, predicate: float, join: float, keys: float, missingness: float) -> dict[str, object]:
    score=100*(0.18*entity+0.18*relationship+0.18*predicate+0.18*join+0.14*keys+0.14*missingness)
    return {"query_logic_core_score": round(score,3), "diagnostic": "strong core query logic" if score >= 84 else "review entities, relationships, predicates, joins, keys, and missingness"}

def join_risk_calculator(key_quality: float, cardinality_documented: float, duplicate_checks: float, missingness_policy: float, provenance_linked: float) -> dict[str, object]:
    risk=100*mean([1-key_quality,1-cardinality_documented,1-duplicate_checks,1-missingness_policy,1-provenance_linked])
    return {"join_risk": round(risk,3), "diagnostic": "manageable join risk" if risk < 30 else "elevated join risk; review keys, cardinality, duplicates, missingness, and provenance"}

def evaluate(cases: list[RelationalQueryCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=query_logic_score(c)
        risk=representation_risk(c)
        out.append({**asdict(c), "query_logic_score": round(score,3), "representation_risk": round(risk,3), "diagnostic": diagnose(score,risk)})
    return out

def query_pattern_inventory() -> list[dict[str, object]]:
    return [
        {"pattern":"selection","formal_question":"Which records satisfy a predicate?","example":"published articles","governance_value":"clarifies inclusion criteria"},
        {"pattern":"projection","formal_question":"Which attributes should be returned?","example":"title, slug, publication_status","governance_value":"limits exposure and focuses attention"},
        {"pattern":"inner_join","formal_question":"Which records have matching partners?","example":"articles with references","governance_value":"reconstructs context"},
        {"pattern":"anti_join","formal_question":"Which records lack a required relationship?","example":"articles without repository links","governance_value":"finds missing evidence"},
        {"pattern":"group_by","formal_question":"How do summaries differ by category?","example":"article count by series","governance_value":"turns records into metrics"},
        {"pattern":"recursive_query","formal_question":"How do nested relationships unfold?","example":"subtopics under a category","governance_value":"tracks hierarchy and inheritance"},
    ]

def relational_set_examples() -> list[dict[str, object]]:
    published={"a1","a2","a3","a4"}
    with_references={"a1","a2","a4"}
    with_repo={"a1","a3"}
    return [
        {"operation":"intersection","result":"|".join(sorted(published & with_references))},
        {"operation":"anti_join_missing_references","result":"|".join(sorted(published - with_references))},
        {"operation":"published_with_repo","result":"|".join(sorted(published & with_repo))},
        {"operation":"missing_repo","result":"|".join(sorted(published - with_repo))},
    ]

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    rows=evaluate(load_cases(root/"data"/"synthetic_relational_query_cases.csv"))
    summary={
        "case_count": len(rows),
        "average_query_logic_score": round(mean(float(r["query_logic_score"]) for r in rows),3),
        "average_representation_risk": round(mean(float(r["representation_risk"]) for r in rows),3),
        "highest_score_case": max(rows, key=lambda r: float(r["query_logic_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda r: float(r["representation_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"relational_query_logic_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"relational_query_logic_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"query_pattern_inventory.csv", query_pattern_inventory())
    write_csv(root/"outputs"/"tables"/"relational_set_examples.csv", relational_set_examples())
    write_json(root/"outputs"/"json"/"relational_query_logic_audit.json", rows)
    write_json(root/"outputs"/"json"/"relational_query_logic_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"query_pattern_inventory.json", query_pattern_inventory())
    write_json(root/"outputs"/"json"/"relational_set_examples.json", relational_set_examples())
    write_json(root/"outputs"/"json"/"query_calculator_examples.json", [query_logic_calculator(.88,.86,.84,.82,.84,.80), join_risk_calculator(.84,.80,.78,.82,.84)])

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
