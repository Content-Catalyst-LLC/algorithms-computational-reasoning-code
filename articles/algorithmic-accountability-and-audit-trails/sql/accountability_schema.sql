CREATE TABLE IF NOT EXISTS accountability_system_records (
  system_id TEXT PRIMARY KEY,
  required_records INTEGER NOT NULL,
  available_records INTEGER NOT NULL,
  documentation REAL NOT NULL,
  provenance REAL NOT NULL,
  reviewability REAL NOT NULL,
  contestability REAL NOT NULL,
  remediation REAL NOT NULL,
  governance REAL NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS accountability_audit (
  system_id TEXT PRIMARY KEY,
  audit_completeness_score REAL NOT NULL,
  accountability_capacity_score REAL NOT NULL,
  reconstruction_risk_score REAL NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS accountability_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
