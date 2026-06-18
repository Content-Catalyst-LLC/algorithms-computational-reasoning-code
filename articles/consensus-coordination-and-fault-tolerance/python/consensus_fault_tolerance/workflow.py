from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from math import comb
import csv, json

@dataclass(frozen=True)
class ConsensusCase:
    case_name: str
    system_context: str
    coordination_goal: str
    agreement_clarity: float
    quorum_design: float
    failure_model: float
    leader_election: float
    log_replication: float
    partition_behavior: float
    retry_idempotence: float
    observability: float
    recovery_design: float
    security_trust: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.10,0.10,0.11,0.09,0.09,0.10,0.09,0.10,0.08,0.06,0.05,0.03]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def consensus_reliability_score(case: ConsensusCase) -> float:
    vals=[case.agreement_clarity,case.quorum_design,case.failure_model,case.leader_election,case.log_replication,case.partition_behavior,case.retry_idempotence,case.observability,case.recovery_design,case.security_trust,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def consensus_risk(case: ConsensusCase) -> float:
    vals=[case.agreement_clarity,case.quorum_design,case.failure_model,case.leader_election,case.partition_behavior,case.retry_idempotence,case.observability,case.recovery_design,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong consensus, coordination, and fault-tolerance discipline"
    if score >= 70 and risk <= 35:
        return "usable coordination design with review needs"
    if risk >= 55:
        return "high risk; weak agreement, partition behavior, retries, recovery, or observability may create unreliable distributed decisions"
    return "partial discipline; strengthen quorum design, failure modeling, partition behavior, idempotence, observability, recovery, and governance"

def majority_quorum(node_count: int) -> int:
    return (node_count // 2) + 1

def crash_fault_tolerance(node_count: int) -> int:
    return (node_count - 1) // 2

def byzantine_replica_requirement(faults: int) -> int:
    return (3 * faults) + 1

def quorum_intersection_holds(node_count: int, quorum_size: int) -> bool:
    return (2 * quorum_size) > node_count

def majority_availability(node_count: int, node_availability: float) -> float:
    q=majority_quorum(node_count)
    return round(sum(comb(node_count,a)*(node_availability**a)*((1-node_availability)**(node_count-a)) for a in range(q,node_count+1)), 8)

def consensus_risk_score(agreement: float, quorum: float, failure_model: float, partition: float, retry: float, observability: float, recovery: float) -> dict[str, float | str]:
    risk=100*(0.16*(1-agreement)+0.16*(1-quorum)+0.17*(1-failure_model)+0.15*(1-partition)+0.12*(1-retry)+0.12*(1-observability)+0.12*(1-recovery))
    return {"agreement_clarity":agreement,"quorum_design":quorum,"failure_model":failure_model,"partition_behavior":partition,"retry_idempotence":retry,"observability":observability,"recovery_design":recovery,"consensus_risk_score":round(risk,3)}

def load_cases(path: Path) -> list[ConsensusCase]:
    fields=["agreement_clarity","quorum_design","failure_model","leader_election","log_replication","partition_behavior","retry_idempotence","observability","recovery_design","security_trust","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [ConsensusCase(r["case_name"], r["system_context"], r["coordination_goal"], *[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def evaluate(cases: list[ConsensusCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=consensus_reliability_score(c)
        risk=consensus_risk(c)
        out.append({**asdict(c), "consensus_reliability_score":round(score,3), "consensus_risk":round(risk,3), "diagnostic":diagnose(score,risk)})
    return out

def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def calculator_examples() -> list[dict[str, object]]:
    rows=[]
    for n in [3,5,7,9]:
        q=majority_quorum(n)
        rows.append({"node_count":n,"majority_quorum":q,"crash_fault_tolerance":crash_fault_tolerance(n),"quorum_intersection_holds":quorum_intersection_holds(n,q),"majority_availability_at_99_percent_node_availability":majority_availability(n,.99)})
    for f in [1,2,3]:
        rows.append({"byzantine_faults":f,"minimum_replicas_3f_plus_1":byzantine_replica_requirement(f)})
    rows.append(consensus_risk_score(.88,.90,.86,.84,.82,.82,.84))
    rows.append(consensus_risk_score(.28,.18,.30,.12,.30,.26,.22))
    return rows

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_consensus_cases.csv"))
    summary={"case_count":len(audit),"average_consensus_reliability_score":round(mean(float(r["consensus_reliability_score"]) for r in audit),3),"average_consensus_risk":round(mean(float(r["consensus_risk"]) for r in audit),3),"highest_score_case":max(audit,key=lambda r:float(r["consensus_reliability_score"]))["case_name"],"highest_risk_case":max(audit,key=lambda r:float(r["consensus_risk"]))["case_name"]}
    for name, rows in [("consensus_fault_tolerance_audit",audit),("consensus_fault_tolerance_audit_summary",[summary]),("consensus_fault_tolerance_calculator_examples",calculator_examples())]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)
    for src, name in [("synthetic_quorum_records.csv","quorum_records"),("synthetic_leader_terms.csv","leader_terms")]:
        with (root/"data"/src).open(newline="", encoding="utf-8") as f:
            rows=list(csv.DictReader(f))
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
