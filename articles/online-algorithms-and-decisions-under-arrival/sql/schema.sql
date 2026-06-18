DROP TABLE IF EXISTS online_decision_cases;
CREATE TABLE online_decision_cases (
  case_name TEXT PRIMARY KEY, system_context TEXT, online_decision TEXT,
  information_at_decision_clarity REAL, arrival_model_clarity REAL, commitment_awareness REAL,
  threshold_transparency REAL, prediction_error_handling REAL, competitive_or_regret_evidence REAL,
  queue_and_capacity_awareness REAL, fairness_under_arrival_review REAL, fallback_readiness REAL,
  governance_readiness REAL, communication_clarity REAL
);
.import --csv data/synthetic_online_decision_cases.csv online_decision_cases
