from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json

@dataclass(frozen=True)
class EdgeEmbeddedCase:
    case_name: str
    system_context: str
    local_decision_goal: str
    latency_discipline: float
    power_awareness: float
    memory_awareness: float
    sensor_validation: float
    offline_behavior: float
    update_safety: float
    security_design: float
    observability: float
    fail_safe_design: float
    data_minimization: float
    governance_review: float
    communication_clarity: float

WEIGHTS=[0.11,0.09,0.08,0.10,0.09,0.08,0.10,0.10,0.11,0.06,0.05,0.03]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def edge_embedded_score(case: EdgeEmbeddedCase) -> float:
    vals=[case.latency_discipline,case.power_awareness,case.memory_awareness,case.sensor_validation,case.offline_behavior,case.update_safety,case.security_design,case.observability,case.fail_safe_design,case.data_minimization,case.governance_review,case.communication_clarity]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def edge_embedded_risk(case: EdgeEmbeddedCase) -> float:
    vals=[case.latency_discipline,case.power_awareness,case.sensor_validation,case.offline_behavior,case.update_safety,case.security_design,case.observability,case.fail_safe_design,case.governance_review]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong edge and embedded algorithm discipline"
    if score >= 70 and risk <= 35:
        return "usable edge design with review needs"
    if risk >= 55:
        return "high risk; timing, power, sensor validation, offline behavior, update safety, security, observability, or fail-safe design may undermine device behavior"
    return "partial discipline; strengthen timing, power, sensor validation, offline operation, update safety, security, observability, fail-safe behavior, and governance"

def load_cases(path: Path) -> list[EdgeEmbeddedCase]:
    fields=["latency_discipline","power_awareness","memory_awareness","sensor_validation","offline_behavior","update_safety","security_design","observability","fail_safe_design","data_minimization","governance_review","communication_clarity"]
    with path.open(newline="", encoding="utf-8") as f:
        return [EdgeEmbeddedCase(r["case_name"],r["system_context"],r["local_decision_goal"],*[float(r[k]) for k in fields]) for r in csv.DictReader(f)]

def edge_response_time(sense_ms: float, filter_ms: float, compute_ms: float, actuate_ms: float) -> float:
    return round(sense_ms + filter_ms + compute_ms + actuate_ms, 3)

def cloud_dependent_response_time(sense_ms: float, uplink_ms: float, cloud_compute_ms: float, downlink_ms: float, actuate_ms: float) -> float:
    return round(sense_ms + uplink_ms + cloud_compute_ms + downlink_ms + actuate_ms, 3)

def meets_deadline(response_time_ms: float, deadline_ms: float) -> bool:
    return response_time_ms <= deadline_ms

def battery_life_hours(battery_wh: float, average_power_w: float) -> float:
    return round(battery_wh / average_power_w, 3) if average_power_w else 0.0

def local_threshold_action(signal_value: float, threshold: float) -> str:
    return "alert" if signal_value >= threshold else "monitor"

def evaluate(cases: list[EdgeEmbeddedCase]) -> list[dict[str,object]]:
    rows=[]
    for c in cases:
        score=edge_embedded_score(c)
        risk=edge_embedded_risk(c)
        rows.append({**asdict(c),"edge_embedded_score":round(score,3),"edge_embedded_risk":round(risk,3),"diagnostic":diagnose(score,risk)})
    return rows

def timing_power_summary(path: Path) -> list[dict[str,object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            edge=edge_response_time(float(r["sense_ms"]),float(r["filter_ms"]),float(r["compute_ms"]),float(r["actuate_ms"]))
            cloud=cloud_dependent_response_time(float(r["sense_ms"]),float(r["uplink_ms"]),float(r["cloud_compute_ms"]),float(r["downlink_ms"]),float(r["actuate_ms"]))
            deadline=float(r["deadline_ms"])
            rows.append({
                **r,
                "edge_response_time_ms":edge,
                "cloud_response_time_ms":cloud,
                "edge_meets_deadline":meets_deadline(edge,deadline),
                "cloud_meets_deadline":meets_deadline(cloud,deadline),
                "battery_life_hours":battery_life_hours(float(r["battery_wh"]),float(r["average_power_w"])),
                "local_action":local_threshold_action(float(r["signal_value"]),float(r["threshold"]))
            })
    return rows

def calculator_examples() -> list[dict[str,object]]:
    edge_time=edge_response_time(8,6,14,5)
    cloud_time=cloud_dependent_response_time(8,90,60,90,5)
    return [
        {"example":"edge_response_time","sense_ms":8,"filter_ms":6,"compute_ms":14,"actuate_ms":5,"edge_response_time_ms":edge_time,"deadline_ms":50,"meets_deadline":meets_deadline(edge_time,50)},
        {"example":"cloud_dependent_response_time","sense_ms":8,"uplink_ms":90,"cloud_compute_ms":60,"downlink_ms":90,"actuate_ms":5,"cloud_response_time_ms":cloud_time,"deadline_ms":50,"meets_deadline":meets_deadline(cloud_time,50)},
        {"example":"battery_life","battery_wh":12,"average_power_w":0.08,"battery_life_hours":battery_life_hours(12,0.08)},
        {"example":"local_threshold_action","signal_value":0.82,"threshold":0.75,"action":local_threshold_action(0.82,0.75)}
    ]

def write_csv(path: Path, rows: list[dict[str,object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

def run_workflow(root: Path) -> None:
    audit=evaluate(load_cases(root/"data"/"synthetic_edge_embedded_cases.csv"))
    timing=timing_power_summary(root/"data"/"synthetic_edge_timing_power.csv")
    summary={
        "case_count":len(audit),
        "average_edge_embedded_score":round(mean(float(r["edge_embedded_score"]) for r in audit),3),
        "average_edge_embedded_risk":round(mean(float(r["edge_embedded_risk"]) for r in audit),3),
        "highest_score_case":max(audit,key=lambda r:float(r["edge_embedded_score"]))["case_name"],
        "highest_risk_case":max(audit,key=lambda r:float(r["edge_embedded_risk"]))["case_name"]
    }
    for name, rows in [
        ("edge_embedded_algorithm_audit",audit),
        ("edge_embedded_algorithm_audit_summary",[summary]),
        ("edge_timing_power_summary",timing),
        ("edge_embedded_calculator_examples",calculator_examples())
    ]:
        write_csv(root/"outputs"/"tables"/f"{name}.csv", rows)
        write_json(root/"outputs"/"json"/f"{name}.json", rows)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
