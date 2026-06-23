CREATE TABLE IF NOT EXISTS learning_systems (
  system_id TEXT PRIMARY KEY,
  learner_impact REAL NOT NULL,
  instructional_impact REAL NOT NULL,
  equity_readiness REAL NOT NULL,
  privacy_readiness REAL NOT NULL,
  pedagogical_validity REAL NOT NULL,
  human_review REAL NOT NULL,
  accessibility_readiness REAL NOT NULL,
  monitoring REAL NOT NULL,
  governance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS learning_system_governance_audit (
  system_id TEXT PRIMARY KEY,
  impact_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  learning_system_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS learning_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
