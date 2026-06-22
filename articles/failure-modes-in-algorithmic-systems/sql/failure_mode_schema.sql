CREATE TABLE IF NOT EXISTS failure_modes (
  failure_id TEXT PRIMARY KEY,
  category TEXT NOT NULL,
  likelihood REAL NOT NULL,
  severity REAL NOT NULL,
  detectability REAL NOT NULL,
  controllability REAL NOT NULL,
  monitoring REAL NOT NULL,
  fallback REAL NOT NULL,
  rollback REAL NOT NULL,
  escalation REAL NOT NULL,
  repair REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS failure_mode_audit (
  failure_id TEXT PRIMARY KEY,
  category TEXT,
  failure_risk_score REAL,
  priority_score REAL,
  resilience_capacity REAL,
  severe_failure INTEGER,
  high_failure_risk INTEGER,
  high_priority INTEGER,
  low_resilience INTEGER,
  status TEXT
);

CREATE TABLE IF NOT EXISTS failure_mode_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
