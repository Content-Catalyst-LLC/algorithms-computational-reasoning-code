CREATE TABLE IF NOT EXISTS deployment_snapshots (
  period TEXT PRIMARY KEY,
  input_drift REAL NOT NULL,
  label_drift REAL NOT NULL,
  accuracy REAL NOT NULL,
  calibration_gap REAL NOT NULL,
  subgroup_gap REAL NOT NULL,
  override_rate REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS drift_decay_audit (
  period TEXT PRIMARY KEY,
  input_drift REAL,
  label_drift REAL,
  accuracy REAL,
  performance_decay REAL,
  calibration_gap REAL,
  subgroup_gap REAL,
  override_rate REAL,
  decay_risk_score REAL,
  status TEXT
);

CREATE TABLE IF NOT EXISTS drift_decay_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
