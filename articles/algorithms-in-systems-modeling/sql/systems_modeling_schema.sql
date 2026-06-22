CREATE TABLE IF NOT EXISTS system_scenarios (
  scenario_id TEXT PRIMARY KEY,
  feedback_strength REAL NOT NULL,
  network_dependency REAL NOT NULL,
  scenario_uncertainty REAL NOT NULL,
  resilience REAL NOT NULL,
  calibration REAL NOT NULL,
  documentation REAL NOT NULL,
  governance REAL NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS systems_modeling_audit (
  scenario_id TEXT PRIMARY KEY,
  system_vulnerability_score REAL NOT NULL,
  model_readiness_score REAL NOT NULL,
  system_modeling_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS systems_modeling_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
