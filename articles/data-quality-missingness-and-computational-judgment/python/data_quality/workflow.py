from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
import csv, json, math

@dataclass(frozen=True)
class DataQualityCase:
    case_name: str
    system_context: str
    computational_use: str
    completeness: float
    validity: float
    freshness: float
    provenance: float
    schema_stability: float
    representativeness: float
    missingness_documentation: float
    imputation_discipline: float
    validation_coverage: float
    governance_review: float
    uncertainty_communication: float
    fitness_for_purpose: float

WEIGHTS=[0.10,0.09,0.08,0.10,0.08,0.10,0.09,0.08,0.10,0.07,0.06,0.05]

def clamp(x: float) -> float:
    return max(0.0, min(100.0, x))

def data_quality_score(case: DataQualityCase) -> float:
    vals=[case.completeness,case.validity,case.freshness,case.provenance,case.schema_stability,case.representativeness,case.missingness_documentation,case.imputation_discipline,case.validation_coverage,case.governance_review,case.uncertainty_communication,case.fitness_for_purpose]
    return clamp(100*sum(v*w for v,w in zip(vals, WEIGHTS)))

def computational_judgment_risk(case: DataQualityCase) -> float:
    vals=[case.completeness,case.provenance,case.representativeness,case.missingness_documentation,case.imputation_discipline,case.validation_coverage,case.governance_review,case.uncertainty_communication,case.fitness_for_purpose]
    return clamp(100*mean(1-v for v in vals))

def diagnose(score: float, risk: float) -> str:
    if score >= 84 and risk <= 20:
        return "strong data-quality evidence and computational judgment discipline"
    if score >= 70 and risk <= 35:
        return "usable data with documented review needs"
    if risk >= 55:
        return "high risk; missingness, weak provenance, poor validation, or undercoverage may distort computation"
    return "partial discipline; strengthen missingness documentation, provenance, validation, representativeness, and uncertainty communication"

def load_cases(path: Path) -> list[DataQualityCase]:
    with path.open(newline="", encoding="utf-8") as f:
        rows=csv.DictReader(f)
        return [
            DataQualityCase(
                r["case_name"], r["system_context"], r["computational_use"],
                float(r["completeness"]), float(r["validity"]), float(r["freshness"]),
                float(r["provenance"]), float(r["schema_stability"]), float(r["representativeness"]),
                float(r["missingness_documentation"]), float(r["imputation_discipline"]),
                float(r["validation_coverage"]), float(r["governance_review"]),
                float(r["uncertainty_communication"]), float(r["fitness_for_purpose"])
            ) for r in rows
        ]

def missingness_rate(missing_count: int, total_count: int) -> float:
    return round(missing_count / total_count, 4) if total_count else 0.0

def completeness_score(missing_count: int, total_count: int) -> float:
    return round(1.0 - missingness_rate(missing_count, total_count), 4)

def freshness_score(days_since_update: int, decay: float = 0.025) -> float:
    return round(math.exp(-decay * days_since_update), 4)

def data_quality_calculator(completeness: float, validity: float, timeliness: float, provenance: float, validation: float) -> dict[str, float | str]:
    score=100*(0.25*completeness+0.20*validity+0.15*timeliness+0.22*provenance+0.18*validation)
    return {"completeness":completeness,"validity":validity,"timeliness":timeliness,"provenance":provenance,"validation":validation,"data_quality_score":round(score,3),"diagnostic":"strong data-quality evidence" if score >= 84 else "review completeness, validity, timeliness, provenance, and validation"}

def load_missingness_profiles(path: Path) -> list[dict[str, object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            missing=int(row["missing_count"])
            total=int(row["total_count"])
            rows.append({**row, "missingness_rate": missingness_rate(missing,total), "completeness_score": completeness_score(missing,total)})
    return rows

def load_quality_checks(path: Path) -> list[dict[str, object]]:
    rows=[]
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            passed=int(row["passed"])
            total=int(row["total"])
            threshold=float(row["threshold"])
            rate=round(passed/total,4) if total else 0.0
            rows.append({**row, "pass_rate": rate, "meets_threshold": rate >= threshold})
    return rows

def evaluate(cases: list[DataQualityCase]) -> list[dict[str, object]]:
    out=[]
    for c in cases:
        score=data_quality_score(c)
        risk=computational_judgment_risk(c)
        out.append({**asdict(c), "data_quality_score": round(score,3), "computational_judgment_risk": round(risk,3), "diagnostic": diagnose(score,risk)})
    return out

def quality_examples() -> list[dict[str, object]]:
    return [
        data_quality_calculator(.92,.88,.86,.90,.89),
        data_quality_calculator(.62,.70,.48,.42,.55),
        {"example":"freshness_7_days","freshness_score":freshness_score(7)},
        {"example":"freshness_90_days","freshness_score":freshness_score(90)},
        {"example":"missingness_rate_45_of_1000","missingness_rate":missingness_rate(45,1000)},
        {"example":"completeness_score_45_of_1000","completeness_score":completeness_score(45,1000)}
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
    audit=evaluate(load_cases(root/"data"/"synthetic_data_quality_cases.csv"))
    missing=load_missingness_profiles(root/"data"/"synthetic_missingness_profiles.csv")
    checks=load_quality_checks(root/"data"/"synthetic_quality_checks.csv")
    summary={
        "case_count": len(audit),
        "average_data_quality_score": round(mean(float(r["data_quality_score"]) for r in audit),3),
        "average_computational_judgment_risk": round(mean(float(r["computational_judgment_risk"]) for r in audit),3),
        "highest_score_case": max(audit, key=lambda r: float(r["data_quality_score"]))["case_name"],
        "highest_risk_case": max(audit, key=lambda r: float(r["computational_judgment_risk"]))["case_name"],
    }
    write_csv(root/"outputs"/"tables"/"data_quality_missingness_audit.csv", audit)
    write_csv(root/"outputs"/"tables"/"data_quality_missingness_audit_summary.csv", [summary])
    write_csv(root/"outputs"/"tables"/"missingness_profile_examples.csv", missing)
    write_csv(root/"outputs"/"tables"/"quality_check_examples.csv", checks)
    write_csv(root/"outputs"/"tables"/"data_quality_examples.csv", quality_examples())
    write_json(root/"outputs"/"json"/"data_quality_missingness_audit.json", audit)
    write_json(root/"outputs"/"json"/"data_quality_missingness_audit_summary.json", summary)
    write_json(root/"outputs"/"json"/"missingness_profile_examples.json", missing)
    write_json(root/"outputs"/"json"/"quality_check_examples.json", checks)
    write_json(root/"outputs"/"json"/"data_quality_examples.json", quality_examples())

if __name__ == "__main__":
    run_workflow(Path(__file__).resolve().parents[2])
