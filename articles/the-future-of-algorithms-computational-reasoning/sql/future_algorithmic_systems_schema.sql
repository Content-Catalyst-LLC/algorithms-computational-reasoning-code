CREATE TABLE IF NOT EXISTS future_algorithmic_domains (
  domain_id TEXT PRIMARY KEY,
  technical_capability REAL NOT NULL,
  institutional_consequence REAL NOT NULL,
  uncertainty REAL NOT NULL,
  automation_level REAL NOT NULL,
  opacity REAL NOT NULL,
  contestability_need REAL NOT NULL,
  governance_maturity REAL NOT NULL,
  human_judgment_requirement REAL NOT NULL,
  failure_severity REAL NOT NULL,
  deployment_readiness REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS future_algorithmic_systems_map (
  domain_id TEXT PRIMARY KEY,
  technical_capability REAL NOT NULL,
  institutional_consequence REAL NOT NULL,
  uncertainty REAL NOT NULL,
  automation_level REAL NOT NULL,
  opacity REAL NOT NULL,
  contestability_need REAL NOT NULL,
  governance_maturity REAL NOT NULL,
  human_judgment_requirement REAL NOT NULL,
  failure_severity REAL NOT NULL,
  deployment_readiness REAL NOT NULL,
  risk_score REAL NOT NULL,
  readiness_score REAL NOT NULL,
  future_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS future_algorithmic_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS no_go_examples (
  case_id TEXT PRIMARY KEY,
  poor_fit BOOLEAN NOT NULL,
  invalid_data BOOLEAN NOT NULL,
  high_opacity BOOLEAN NOT NULL,
  no_appeal BOOLEAN NOT NULL,
  no_governance BOOLEAN NOT NULL,
  no_go BOOLEAN NOT NULL
);
