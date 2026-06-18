from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class DistributedSystemCase:
    case_name: str
    system_context: str
    computational_goal: str
    node_design: float
    message_discipline: float
    failure_handling: float
    replication_strategy: float
    consistency_clarity: float
    consensus_readiness: float
    latency_awareness: float
    observability: float
    security_trust: float
    provenance_support: float
    reproducibility: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.08,0.09,0.11,0.09,0.10,0.08,0.07,0.10,0.08,0.08,0.05,0.04,0.03]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def distributed_reliability_score(case: DistributedSystemCase) -> float:
    vals=[case.node_design,case.message_discipline,case.failure_handling,case.replication_strategy,case.consistency_clarity,case.consensus_readiness,case.latency_awareness,case.observability,case.security_trust,case.provenance_support,case.reproducibility,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def distributed_risk(case: DistributedSystemCase) -> float:
    vals=[case.message_discipline,case.failure_handling,case.replication_strategy,case.consistency_clarity,case.consensus_readiness,case.observability,case.security_trust,case.provenance_support,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong distributed-system discipline"
    if score >= 70 and risk <= 35:
        return "usable distributed design with review needs"
    if risk >= 55:
        return "high risk; network delay, partial failure, weak consistency, poor observability, or trust gaps may distort computation"
    return "partial discipline; strengthen messages, failure handling, consistency, observability, provenance, and governance"

def load_cases(path: Path) -> list[DistributedSystemCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            DistributedSystemCase(
                r["case_name"], r["system_context"], r["computational_goal"],
                float(r["node_design"]), float(r["message_discipline"]),
                float(r["failure_handling"]), float(r["replication_strategy"]),
                float(r["consistency_clarity"]), float(r["consensus_readiness"]),
                float(r["latency_awareness"]), float(r["observability"]),
                float(r["security_trust"]), float(r["provenance_support"]),
                float(r["reproducibility"]), float(r["governance_review"]),
                float(r["communication_clarity"])
            ) for r in rows
        ]

def quorum_size(node_count: int) -> int:
    return (node_count // 2) + 1

def crash_fault_tolerance(node_count: int) -> int:
    return (node_count - 1) // 2

def availability_with_replication(replica_count: int, node_availability: float) -> float:
    return round(1.0 - ((1.0 - node_availability) ** replica_count), 6)

def distributed_latency(compute_ms: float, network_ms: float, queue_ms: float) -> float:
    return round(compute_ms + network_ms + queue_ms, 3)

def replication_lag(replica_visible_time: float, write_committed_time: float) -> float:
    return round(replica_visible_time - write_committed_time, 3)

def distributed_risk_score(message: float, failure: float, replication: float, consistency: float, observability: float, security: float, provenance: float) -> dict[str, float | str]:
    risk=100*(0.16*(1-message)+0.18*(1-failure)+0.15*(1-replication)+0.17*(1-consistency)+0.14*(1-observability)+0.10*(1-security)+0.10*(1-provenance))
    return {"message_discipline":message,"failure_handling":failure,"replication_strategy":replication,"consistency_clarity":consistency,"observability":observability,"security_trust":security,"provenance_support":provenance,"distributed_risk_score":round(risk,3),"diagnostic":"low distributed risk" if risk <= 25 else "review messages, failure handling, consistency, observability, security, and provenance"}

def load_quorum_examples(path: Path) -> list[dict[str, object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            n=int(row["node_count"])
            availability=float(row["node_availability"])
            rows.append({**row,"majority_quorum":quorum_size(n),"crash_fault_tolerance":crash_fault_tolerance(n),"all_replicas_availability":availability_with_replication(n, availability)})
    return rows

def load_nodes(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    return rows

def load_messages(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    return rows

def calculator_examples() -> list[dict[str, object]]:
    rows=[]
    for n in [3,5,7,9]:
        rows.append({"node_count":n,"majority_quorum":quorum_size(n),"crash_fault_tolerance":crash_fault_tolerance(n)})
    rows.extend([
        {"example":"availability_three_replicas_99_percent_nodes","replica_count":3,"node_availability":0.99,"availability":availability_with_replication(3,0.99)},
        {"example":"distributed_response_latency","compute_ms":35.0,"network_ms":80.0,"queue_ms":20.0,"response_ms":distributed_latency(35.0,80.0,20.0)},
        {"example":"replication_lag","write_committed_time":1000.0,"replica_visible_time":1042.5,"replication_lag_ms":replication_lag(1042.5,1000.0)},
        distributed_risk_score(.84,.80,.82,.78,.84,.78,.80),
        distributed_risk_score(.38,.30,.34,.24,.22,.42,.18),
    ])
    return rows

def evaluate(cases: list[DistributedSystemCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=distributed_reliability_score(c)
        risk=distributed_risk(c)
        out.append({**asdict(c), "distributed_reliability_score":round(score,3), "distributed_risk":round(risk,3), "diagnostic":diagnose(score,risk)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_distributed_cases.csv"))
    quorums=load_quorum_examples(root/"data"/"synthetic_quorum_examples.csv")
    nodes=load_nodes(root/"data"/"synthetic_network_nodes.csv")
    messages=load_messages(root/"data"/"synthetic_messages.csv")
    summary={
        "case_count": len(audit),
        "average_distributed_reliability_score": round(mean(float(r["distributed_reliability_score"]) for r in audit),3),
        "average_distributed_risk": round(mean(float(r["distributed_risk"]) for r in audit),3),
        "highest_score_case": max(audit, key=lambda r: float(r["distributed_reliability_score"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["distributed_risk"]))["case_name"],
    }
    write_csv(root/"outputs"/"tables"/"distributed_algorithms_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"distributed_algorithms_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"distributed_quorum_examples.csv", quorums)
    write_csv(root/"outputs"/"tables"/"distributed_nodes.csv", nodes)
    write_csv(root/"outputs"/"tables"/"distributed_messages.csv", messages)
    write_csv(root/"outputs"/"tables"/"distributed_algorithm_calculator_examples.csv", calculator_examples())
    write_json(root/"outputs"/"json"/"distributed_algorithms_audit.json", audit)
    write_json(root/"outputs"/"json"/"distributed_algorithms_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"distributed_quorum_examples.json", quorums)
    write_json(root/"outputs"/"json"/"distributed_nodes.json", nodes)
    write_json(root/"outputs"/"json"/"distributed_messages.json", messages)
    write_json(root/"outputs"/"json"/"distributed_algorithm_calculator_examples.json", calculator_examples())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
