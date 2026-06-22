CREATE TABLE IF NOT EXISTS candidate_decisions (
  decision_id TEXT PRIMARY KEY,
  predicted_probability REAL NOT NULL,
  benefit_if_act REAL NOT NULL,
  cost_if_act REAL NOT NULL,
  loss_if_miss REAL NOT NULL,
  calibration REAL NOT NULL,
  uncertainty_communication REAL NOT NULL,
  human_review REAL NOT NULL,
  contestability REAL NOT NULL,
  governance REAL NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS decision_science_audit (
  decision_id TEXT PRIMARY KEY,
  predicted_probability REAL NOT NULL,
  expected_value_of_action REAL NOT NULL,
  expected_loss_if_no_action REAL NOT NULL,
  threshold_action INTEGER NOT NULL,
  decision_support_readiness_score REAL NOT NULL,
  stakes REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS decision_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
