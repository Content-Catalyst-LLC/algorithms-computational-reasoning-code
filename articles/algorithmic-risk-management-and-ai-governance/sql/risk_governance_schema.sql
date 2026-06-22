CREATE TABLE IF NOT EXISTS risk_items (
  risk_id TEXT PRIMARY KEY,
  system TEXT NOT NULL,
  severity REAL NOT NULL,
  likelihood REAL NOT NULL,
  detectability REAL NOT NULL,
  ownership REAL NOT NULL,
  documentation REAL NOT NULL,
  monitoring REAL NOT NULL,
  contestability REAL NOT NULL,
  remediation REAL NOT NULL,
  stop_authority REAL NOT NULL,
  control_effectiveness REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS risk_governance_audit (
  risk_id TEXT PRIMARY KEY,
  system TEXT NOT NULL,
  inherent_risk_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  control_effectiveness REAL NOT NULL,
  residual_risk_score REAL NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS risk_governance_controls (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
