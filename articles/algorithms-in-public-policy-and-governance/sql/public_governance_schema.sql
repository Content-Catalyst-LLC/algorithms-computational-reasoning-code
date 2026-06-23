CREATE TABLE IF NOT EXISTS public_algorithm_use_cases (
  use_case_id TEXT PRIMARY KEY,
  rights_impact REAL NOT NULL,
  due_process REAL NOT NULL,
  transparency REAL NOT NULL,
  human_review REAL NOT NULL,
  data_quality REAL NOT NULL,
  vendor_accountability REAL NOT NULL,
  appeal_readiness REAL NOT NULL,
  monitoring REAL NOT NULL,
  public_value REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS public_governance_audit (
  use_case_id TEXT PRIMARY KEY,
  procedural_readiness_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  public_algorithmic_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS public_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
