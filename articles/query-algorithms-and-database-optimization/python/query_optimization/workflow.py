from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json
from statistics import mean

@dataclass(frozen=True)
class QueryOptimizationCase:
    case_name: str; system_context: str; optimization_claim: str
    logical_clarity: float; index_suitability: float; cardinality_awareness: float; join_strategy_quality: float
    predicate_pushdown: float; projection_pruning: float; statistics_freshness: float; memory_risk_management: float
    materialization_freshness: float; workload_impact_review: float; auditability: float; communication_clarity: float

WEIGHTS=[.10,.10,.10,.10,.08,.08,.09,.09,.08,.08,.06,.04]

def clamp(x: float) -> float: return max(0.0, min(100.0, x))
def optimization_quality_score(c: QueryOptimizationCase) -> float:
    vals=[c.logical_clarity,c.index_suitability,c.cardinality_awareness,c.join_strategy_quality,c.predicate_pushdown,c.projection_pruning,c.statistics_freshness,c.memory_risk_management,c.materialization_freshness,c.workload_impact_review,c.auditability,c.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))
def optimization_risk(c: QueryOptimizationCase) -> float:
    vals=[c.logical_clarity,c.cardinality_awareness,c.join_strategy_quality,c.statistics_freshness,c.memory_risk_management,c.materialization_freshness,c.workload_impact_review,c.auditability,c.communication_clarity]
    return clamp(100*mean(1-v for v in vals))
def diagnose(score: float, risk: float) -> str:
    if score>=84 and risk<=20: return 'strong query optimization discipline'
    if score>=70 and risk<=35: return 'usable optimization with review needs'
    if risk>=55: return 'high risk; optimization may hide weak estimates, stale materialization, memory spills, or workload impact'
    return 'partial discipline; strengthen plans, indexes, statistics, memory review, auditability, and communication'
def load_cases(path: Path):
    with path.open(newline='', encoding='utf-8') as f:
        return [QueryOptimizationCase(r['case_name'],r['system_context'],r['optimization_claim'],*(float(r[k]) for k in ['logical_clarity','index_suitability','cardinality_awareness','join_strategy_quality','predicate_pushdown','projection_pruning','statistics_freshness','memory_risk_management','materialization_freshness','workload_impact_review','auditability','communication_clarity'])) for r in csv.DictReader(f)]
def estimate_selection_rows(table_rows:int, selectivity:float): return {'table_rows':table_rows,'selectivity':selectivity,'estimated_rows':round(table_rows*selectivity,3)}
def estimate_join_rows(left_rows:int,right_rows:int,left_distinct:int,right_distinct:int):
    d=max(left_distinct,right_distinct,1); return {'left_rows':left_rows,'right_rows':right_rows,'left_distinct':left_distinct,'right_distinct':right_distinct,'estimated_join_rows':round((left_rows*right_rows)/d,3)}
def index_tradeoff(read_benefit:float, write_cost:float, storage_cost:float, maintenance_cost:float):
    net=read_benefit-write_cost-storage_cost-maintenance_cost; return {'read_benefit':read_benefit,'write_cost':write_cost,'storage_cost':storage_cost,'maintenance_cost':maintenance_cost,'net_index_value':round(net,3)}
def plan_governance_score(performance:float, correctness:float, freshness:float, auditability:float, documentation:float):
    score=100*(.25*performance+.25*correctness+.18*freshness+.17*auditability+.15*documentation); return {'plan_governance_score':round(score,3),'diagnostic':'strong performance-governance balance' if score>=84 else 'review correctness, freshness, auditability, and documentation'}
def evaluate(cases):
    out=[]
    for c in cases:
        score=optimization_quality_score(c); risk=optimization_risk(c)
        out.append({**asdict(c),'optimization_quality_score':round(score,3),'optimization_risk':round(risk,3),'diagnostic':diagnose(score,risk)})
    return out
def examples():
    return [{'example':'selection_estimate',**estimate_selection_rows(1000000,.012)},{'example':'join_estimate',**estimate_join_rows(500000,200000,50000,40000)},{'example':'index_tradeoff',**index_tradeoff(82,14,9,6)},{'example':'plan_governance',**plan_governance_score(.86,.84,.80,.82,.84)}]
def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(payload,indent=2,sort_keys=True), encoding='utf-8')
def run_workflow(root:Path):
    rows=evaluate(load_cases(root/'data'/'synthetic_query_optimization_cases.csv'))
    summary={'case_count':len(rows),'average_optimization_quality_score':round(mean(float(r['optimization_quality_score']) for r in rows),3),'average_optimization_risk':round(mean(float(r['optimization_risk']) for r in rows),3),'highest_score_case':max(rows,key=lambda r:float(r['optimization_quality_score']))['case_name'],'highest_risk_case':max(rows,key=lambda r:float(r['optimization_risk']))['case_name']}
    write_csv(root/'outputs'/'tables'/'query_optimization_audit.csv', rows); write_csv(root/'outputs'/'tables'/'query_optimization_audit_summary.csv', [summary]); write_csv(root/'outputs'/'tables'/'query_optimization_examples.csv', examples())
    write_json(root/'outputs'/'json'/'query_optimization_audit.json', rows); write_json(root/'outputs'/'json'/'query_optimization_audit_summary.json', summary); write_json(root/'outputs'/'json'/'query_optimization_examples.json', examples())
if __name__=='__main__': run_workflow(Path(__file__).resolve().parents[2])
