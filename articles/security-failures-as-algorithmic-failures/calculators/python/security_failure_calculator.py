# security_failure_calculator.py
# Calculator for failure-resistance, residual risk, and control-gap priority.

from __future__ import annotations

from pathlib import Path
import csv
import json

ARTICLE_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ARTICLE_ROOT / "calculators" / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

weights = {
    "assumption_quality": 0.08,
    "threat_model_coverage": 0.10,
    "input_boundary_control": 0.10,
    "authorization_control": 0.10,
    "cryptographic_procedure": 0.08,
    "dependency_governance": 0.08,
    "configuration_safety": 0.08,
    "state_timing_control": 0.08,
    "logging_traceability": 0.08,
    "monitoring_detection": 0.08,
    "incident_response": 0.06,
    "lifecycle_review": 0.05,
    "governance_ownership": 0.03,
}

scenario = {
    "assumption_quality": 0.62,
    "threat_model_coverage": 0.58,
    "input_boundary_control": 0.70,
    "authorization_control": 0.55,
    "cryptographic_procedure": 0.66,
    "dependency_governance": 0.50,
    "configuration_safety": 0.54,
    "state_timing_control": 0.48,
    "logging_traceability": 0.60,
    "monitoring_detection": 0.52,
    "incident_response": 0.50,
    "lifecycle_review": 0.44,
    "governance_ownership": 0.46,
}

score = 100.0 * sum(weights[key] * scenario[key] for key in weights)
risk = 100.0 * sum(1.0 - scenario[key] for key in weights) / len(weights)
control_gap = (1.0 - scenario["authorization_control"]) * 0.90 * 100.0

result = {
    **scenario,
    "failure_resistance_score": round(score, 3),
    "algorithmic_failure_risk": round(risk, 3),
    "authorization_control_gap_score": round(control_gap, 3),
    "interpretation": "Higher failure resistance and lower residual risk indicate stronger algorithmic security reasoning."
}

with (OUTPUT_DIR / "security_failure_calculator_result.json").open("w", encoding="utf-8") as handle:
    json.dump(result, handle, indent=2, sort_keys=True)

with (OUTPUT_DIR / "security_failure_calculator_result.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(result.keys()))
    writer.writeheader()
    writer.writerow(result)

print(json.dumps(result, indent=2, sort_keys=True))
