from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class DatabaseKnowledgeCase:
    case_name: str
    system_context: str
    database_role: str
    schema_clarity: float
    relationship_modeling: float
    constraint_discipline: float
    query_expressiveness: float
    indexing_strategy: float
    transaction_reliability: float
    metadata_quality: float
    provenance_lineage: float
    access_control: float
    correction_workflow: float
    retention_policy: float
    interoperability: float
    governance_readiness: float
    communication_clarity: float

WEIGHTS=[0.09,0.08,0.08,0.08,0.07,0.08,0.08,0.08,0.07,0.07,0.06,0.06,0.06,0.04]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def knowledge_system_score(case: DatabaseKnowledgeCase) -> float:
    vals=[case.schema_clarity,case.relationship_modeling,case.constraint_discipline,case.query_expressiveness,case.indexing_strategy,case.transaction_reliability,case.metadata_quality,case.provenance_lineage,case.access_control,case.correction_workflow,case.retention_policy,case.interoperability,case.governance_readiness,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def representation_risk(case: DatabaseKnowledgeCase) -> float:
    vals=[case.schema_clarity,case.relationship_modeling,case.constraint_discipline,case.metadata_quality,case.provenance_lineage,case.correction_workflow,case.governance_readiness,case.communication_clarity]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong database knowledge system discipline"
    if score >= 70 and risk <= 35:
        return "usable database knowledge system with review needs"
    if risk >= 55:
        return "high risk; database may encode weak representation, provenance, correction, or governance"
    return "partial discipline; strengthen schema, constraints, metadata, provenance, access, correction, and governance"

def load_cases(path: Path) -> list[DatabaseKnowledgeCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            DatabaseKnowledgeCase(
                r["case_name"], r["system_context"], r["database_role"],
                float(r["schema_clarity"]), float(r["relationship_modeling"]),
                float(r["constraint_discipline"]), float(r["query_expressiveness"]),
                float(r["indexing_strategy"]), float(r["transaction_reliability"]),
                float(r["metadata_quality"]), float(r["provenance_lineage"]),
                float(r["access_control"]), float(r["correction_workflow"]),
                float(r["retention_policy"]), float(r["interoperability"]),
                float(r["governance_readiness"]), float(r["communication_clarity"])
            ) for r in rows
        ]

def schema_quality(fields_defined: float, keys_defined: float, constraints_defined: float, metadata_complete: float, lineage_documented: float) -> dict[str, float | str]:
    score=100*(0.22*fields_defined+0.20*keys_defined+0.20*constraints_defined+0.20*metadata_complete+0.18*lineage_documented)
    diagnostic="strong schema quality" if score >= 84 else "review schema documentation, keys, constraints, metadata, and lineage"
    return {"schema_quality_score": round(score,3), "diagnostic": diagnostic}

def governance_risk(metadata_quality: float, provenance_lineage: float, access_control: float, correction_workflow: float, retention_policy: float) -> dict[str, float | str]:
    risk=100*mean([1-metadata_quality,1-provenance_lineage,1-access_control,1-correction_workflow,1-retention_policy])
    diagnostic="manageable governance risk" if risk < 30 else "elevated governance risk; strengthen metadata, provenance, access, correction, and retention"
    return {"database_governance_risk": round(risk,3), "diagnostic": diagnostic}

def evaluate(cases: list[DatabaseKnowledgeCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=knowledge_system_score(c)
        risk=representation_risk(c)
        out.append({**asdict(c), "knowledge_system_score": round(score,3), "representation_risk": round(risk,3), "diagnostic": diagnose(score,risk)})
    return out

def schema_inventory() -> list[dict[str, object]]:
    return [
        {"table_name":"articles","primary_key":"article_id","knowledge_role":"publication object","critical_constraints":"unique slug; required title; publication status"},
        {"table_name":"authors","primary_key":"author_id","knowledge_role":"creator identity","critical_constraints":"unique author identifier; verified display name"},
        {"table_name":"references","primary_key":"reference_id","knowledge_role":"source evidence","critical_constraints":"required citation text; source type; article linkage"},
        {"table_name":"repositories","primary_key":"repo_id","knowledge_role":"executable companion knowledge","critical_constraints":"unique URL; article linkage; license status"},
        {"table_name":"audit_events","primary_key":"event_id","knowledge_role":"change history","critical_constraints":"timestamp; actor; action; affected record"},
    ]

def query_examples() -> list[dict[str, object]]:
    return [
        {"question":"Which articles lack repository links?","query_type":"anti-join","governance_value":"Find missing computational companions."},
        {"question":"Which references support each article?","query_type":"join","governance_value":"Trace source support."},
        {"question":"Which records changed last week?","query_type":"audit query","governance_value":"Support change review."},
        {"question":"Which fields have missing metadata?","query_type":"data quality query","governance_value":"Improve interpretability."},
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
    rows=evaluate(load_cases(root/"data"/"synthetic_database_knowledge_cases.csv"))
    summary={
        "case_count": len(rows),
        "average_knowledge_system_score": round(mean(float(r["knowledge_system_score"]) for r in rows),3),
        "average_representation_risk": round(mean(float(r["representation_risk"]) for r in rows),3),
        "highest_score_case": max(rows, key=lambda r: float(r["knowledge_system_score"]))["case_name"],
        "highest_risk_case": max(rows, key=lambda r: float(r["representation_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"database_knowledge_system_audit.csv", rows)
    write_csv(root/"outputs"/"tables"/"database_knowledge_system_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"schema_inventory.csv", schema_inventory())
    write_csv(root/"outputs"/"tables"/"query_examples.csv", query_examples())
    write_json(root/"outputs"/"json"/"database_knowledge_system_audit.json", rows)
    write_json(root/"outputs"/"json"/"database_knowledge_system_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"schema_inventory.json", schema_inventory())
    write_json(root/"outputs"/"json"/"query_examples.json", query_examples())
    write_json(root/"outputs"/"json"/"database_calculator_examples.json", [schema_quality(0.9,0.85,0.8,0.88,0.82), governance_risk(0.8,0.84,0.78,0.76,0.82)])

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
