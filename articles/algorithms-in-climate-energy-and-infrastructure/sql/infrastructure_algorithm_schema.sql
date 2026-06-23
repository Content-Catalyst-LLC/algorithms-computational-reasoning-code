CREATE TABLE IF NOT EXISTS infrastructure_systems (
  system_id TEXT PRIMARY KEY,
  public_impact REAL NOT NULL,
  climate_exposure REAL NOT NULL,
  reliability_impact REAL NOT NULL,
  equity_readiness REAL NOT NULL,
  validation_readiness REAL NOT NULL,
  monitoring_readiness REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  maintenance_readiness REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS infrastructure_algorithm_risk_audit (
  system_id TEXT PRIMARY KEY,
  impact_score REAL NOT NULL,
  governance_score REAL NOT NULL,
  resilience_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS infrastructure_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
