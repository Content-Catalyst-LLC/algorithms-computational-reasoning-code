CREATE TABLE IF NOT EXISTS financial_systems (
  system_id TEXT PRIMARY KEY,
  market_impact REAL NOT NULL,
  consumer_impact REAL NOT NULL,
  model_risk REAL NOT NULL,
  transparency REAL NOT NULL,
  human_review REAL NOT NULL,
  validation REAL NOT NULL,
  monitoring REAL NOT NULL,
  governance REAL NOT NULL,
  liquidity_risk REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS financial_algorithm_risk_audit (
  system_id TEXT PRIMARY KEY,
  impact_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  financial_algorithm_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS financial_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
