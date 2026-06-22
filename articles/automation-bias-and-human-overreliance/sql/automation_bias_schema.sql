CREATE TABLE IF NOT EXISTS automation_oversight_cases (
  case_id TEXT PRIMARY KEY,
  context TEXT NOT NULL,
  acceptance_rate REAL NOT NULL,
  model_quality REAL NOT NULL,
  uncertainty REAL NOT NULL,
  review_time_minutes REAL NOT NULL,
  override_friction REAL NOT NULL,
  appeal_pathway INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS automation_bias_overreliance_audit (
  case_id TEXT PRIMARY KEY,
  context TEXT,
  acceptance_rate REAL,
  model_quality REAL,
  calibration_gap REAL,
  overreliance_gap REAL,
  review_time_minutes REAL,
  override_friction REAL,
  appeal_pathway INTEGER,
  automation_bias_risk_score REAL,
  status TEXT
);

CREATE TABLE IF NOT EXISTS automation_oversight_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
