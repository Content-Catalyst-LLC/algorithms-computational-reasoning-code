CREATE TABLE IF NOT EXISTS bias_history_group_records (
  group_id TEXT PRIMARY KEY,
  data_share REAL NOT NULL,
  deployment_share REAL NOT NULL,
  selection_rate REAL NOT NULL,
  label_positive_rate REAL NOT NULL,
  verified_positive_rate REAL NOT NULL,
  provenance_risk REAL NOT NULL,
  measurement_weakness REAL NOT NULL,
  proxy_risk REAL NOT NULL,
  remediation REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS bias_history_group_metrics (
  group_id TEXT PRIMARY KEY,
  representation_gap REAL NOT NULL,
  selection_rate REAL NOT NULL,
  label_gap REAL NOT NULL,
  provenance_risk REAL NOT NULL,
  measurement_weakness REAL NOT NULL,
  proxy_risk REAL NOT NULL,
  remediation REAL NOT NULL,
  historical_risk_score REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS bias_history_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
