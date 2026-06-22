CREATE TABLE IF NOT EXISTS algorithmic_harm_contexts (
  case_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  error_likelihood REAL NOT NULL,
  severity REAL NOT NULL,
  exposure REAL NOT NULL,
  contestability REAL NOT NULL,
  ownership REAL NOT NULL,
  monitoring REAL NOT NULL,
  appeals REAL NOT NULL,
  repair REAL NOT NULL,
  governance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS harm_responsibility_audit (
  case_id TEXT PRIMARY KEY,
  domain TEXT,
  harm_risk_score REAL,
  responsibility_capacity REAL,
  remediation_gap REAL,
  high_harm INTEGER,
  low_responsibility INTEGER,
  high_remediation_gap INTEGER,
  status TEXT
);

CREATE TABLE IF NOT EXISTS algorithmic_incident_register (
  field TEXT PRIMARY KEY,
  purpose TEXT,
  required TEXT
);
