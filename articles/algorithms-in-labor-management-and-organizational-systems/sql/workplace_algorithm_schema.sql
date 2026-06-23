CREATE TABLE IF NOT EXISTS workplace_systems (
  system_id TEXT PRIMARY KEY,
  worker_impact REAL NOT NULL,
  managerial_impact REAL NOT NULL,
  fairness_readiness REAL NOT NULL,
  privacy_readiness REAL NOT NULL,
  contestability REAL NOT NULL,
  safety_readiness REAL NOT NULL,
  human_review REAL NOT NULL,
  monitoring REAL NOT NULL,
  governance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS workplace_algorithm_governance_audit (
  system_id TEXT PRIMARY KEY,
  impact_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  workplace_algorithm_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS workplace_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
