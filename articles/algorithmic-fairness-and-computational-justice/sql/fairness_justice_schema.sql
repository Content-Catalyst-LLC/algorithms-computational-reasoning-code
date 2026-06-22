CREATE TABLE IF NOT EXISTS fairness_group_records (
  group_id TEXT PRIMARY KEY,
  n INTEGER NOT NULL,
  selected INTEGER NOT NULL,
  true_positive INTEGER NOT NULL,
  false_positive INTEGER NOT NULL,
  false_negative INTEGER NOT NULL,
  true_negative INTEGER NOT NULL,
  mean_score REAL NOT NULL,
  observed_rate REAL NOT NULL,
  measurement_validity REAL NOT NULL,
  contestability REAL NOT NULL,
  remediation REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS fairness_group_metrics (
  group_id TEXT PRIMARY KEY,
  selection_rate REAL NOT NULL,
  false_positive_rate REAL NOT NULL,
  false_negative_rate REAL NOT NULL,
  true_positive_rate REAL NOT NULL,
  calibration_gap REAL NOT NULL,
  fairness_evidence_score REAL NOT NULL,
  justice_capacity_score REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS fairness_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
