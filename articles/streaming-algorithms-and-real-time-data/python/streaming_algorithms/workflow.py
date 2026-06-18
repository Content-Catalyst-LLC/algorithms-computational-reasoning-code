from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import csv, json, random
from statistics import mean

@dataclass(frozen=True)
class StreamingCase:
    case_name: str
    system_context: str
    streaming_claim: str
    bounded_memory_clarity: float
    approximation_transparency: float
    event_time_handling: float
    late_data_policy: float
    window_design: float
    sampling_quality: float
    sketch_suitability: float
    throughput_awareness: float
    alert_governance: float
    retention_policy: float
    privacy_review: float
    fallback_readiness: float
    communication_clarity: float

WEIGHTS=[0.09,0.09,0.08,0.08,0.08,0.07,0.08,0.09,0.08,0.07,0.07,0.06,0.06]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def streaming_claim_quality(case: StreamingCase) -> float:
    vals=[
        case.bounded_memory_clarity, case.approximation_transparency,
        case.event_time_handling, case.late_data_policy, case.window_design,
        case.sampling_quality, case.sketch_suitability, case.throughput_awareness,
        case.alert_governance, case.retention_policy, case.privacy_review,
        case.fallback_readiness, case.communication_clarity
    ]
    return clamp(100*sum(v*w for v,w in zip(vals,WEIGHTS)))

def streaming_claim_risk(case: StreamingCase) -> float:
    vals=[
        case.bounded_memory_clarity, case.approximation_transparency,
        case.event_time_handling, case.late_data_policy, case.window_design,
        case.sampling_quality, case.sketch_suitability, case.throughput_awareness,
        case.alert_governance, case.retention_policy, case.privacy_review,
        case.fallback_readiness, case.communication_clarity
    ]
    return clamp(100*mean(1-v for v in vals))

def diagnose(q: float, r: float) -> str:
    if q >= 84 and r <= 20:
        return "strong streaming algorithm discipline"
    if q >= 70 and r <= 35:
        return "usable streaming claim with monitoring or governance review needs"
    if r >= 55:
        return "high risk; streaming claim may hide approximation, delay, missing data, or retention effects"
    return "partial streaming discipline"

def load_cases(path: Path) -> list[StreamingCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            StreamingCase(
                r["case_name"], r["system_context"], r["streaming_claim"],
                float(r["bounded_memory_clarity"]), float(r["approximation_transparency"]),
                float(r["event_time_handling"]), float(r["late_data_policy"]),
                float(r["window_design"]), float(r["sampling_quality"]),
                float(r["sketch_suitability"]), float(r["throughput_awareness"]),
                float(r["alert_governance"]), float(r["retention_policy"]),
                float(r["privacy_review"]), float(r["fallback_readiness"]),
                float(r["communication_clarity"])
            ) for r in rows
        ]

def reservoir_sample(items: list[str], k: int, seed: int = 17) -> list[str]:
    rng = random.Random(seed)
    sample: list[str] = []
    for index, item in enumerate(items, start=1):
        if len(sample) < k:
            sample.append(item)
        else:
            replacement_index = rng.randint(1, index)
            if replacement_index <= k:
                sample[replacement_index - 1] = item
    return sample

def sliding_window_counts(items: list[str], window_size: int) -> list[dict[str, object]]:
    rows=[]
    for t in range(1, len(items)+1):
        window=items[max(0,t-window_size):t]
        counts={item: window.count(item) for item in sorted(set(window))}
        rows.append({"time":t,"event":items[t-1],"window_size":window_size,"window_items":"|".join(window),"counts":json.dumps(counts, sort_keys=True)})
    return rows

def queue_pressure_table(arrival_rates: list[float], processing_rate: float) -> list[dict[str, object]]:
    rows=[]
    for arrival_rate in arrival_rates:
        utilization=arrival_rate/processing_rate
        rows.append({
            "arrival_rate": arrival_rate,
            "processing_rate": processing_rate,
            "utilization": round(utilization,3),
            "stable_under_simple_model": arrival_rate < processing_rate,
            "interpretation": "stable" if arrival_rate < processing_rate else "backpressure risk"
        })
    return rows

def simple_bloom_demo(items: list[str], queries: list[str], bit_count: int = 32) -> list[dict[str, object]]:
    bits=[0]*bit_count
    def hashes(x: str) -> tuple[int, int]:
        return (sum(ord(c) for c in x) % bit_count, sum((i+1)*ord(c) for i,c in enumerate(x)) % bit_count)
    for item in items:
        for h in hashes(item):
            bits[h]=1
    return [{"query":q,"possibly_present": all(bits[h] == 1 for h in hashes(q))} for q in queries]

def evaluate(cases: list[StreamingCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        q,r=streaming_claim_quality(c),streaming_claim_risk(c)
        out.append({**asdict(c),"streaming_claim_quality":round(q,3),"streaming_claim_risk":round(r,3),"diagnostic":diagnose(q,r)})
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
    audit=evaluate(load_cases(root/"data"/"synthetic_streaming_cases.csv"))
    stream=["A","B","A","C","A","D","B","E","A","C","F","A"]
    sample=[{"sample_size":4,"sample":"|".join(reservoir_sample(stream,4))}]
    windows=sliding_window_counts(stream, 5)
    pressure=queue_pressure_table([50,75,90,100,120], 100.0)
    bloom=simple_bloom_demo(["A","B","C"], ["A","D","B","E"])
    summary={
        "case_count": len(audit),
        "average_streaming_claim_quality": round(mean(float(r["streaming_claim_quality"]) for r in audit), 3),
        "average_streaming_claim_risk": round(mean(float(r["streaming_claim_risk"]) for r in audit), 3),
        "highest_quality_case": max(audit, key=lambda r: float(r["streaming_claim_quality"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["streaming_claim_risk"]))["case_name"]
    }
    write_csv(root/"outputs"/"tables"/"streaming_algorithm_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"streaming_algorithm_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"reservoir_sample_demo.csv", sample)
    write_csv(root/"outputs"/"tables"/"sliding_window_counts.csv", windows)
    write_csv(root/"outputs"/"tables"/"streaming_queue_pressure.csv", pressure)
    write_csv(root/"outputs"/"tables"/"bloom_filter_demo.csv", bloom)
    write_json(root/"outputs"/"json"/"streaming_algorithm_audit.json", audit)
    write_json(root/"outputs"/"json"/"streaming_algorithm_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"reservoir_sample_demo.json", sample)
    write_json(root/"outputs"/"json"/"sliding_window_counts.json", windows)
    write_json(root/"outputs"/"json"/"streaming_queue_pressure.json", pressure)
    write_json(root/"outputs"/"json"/"bloom_filter_demo.json", bloom)

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
