CREATE TABLE IF NOT EXISTS philosophical_domains (
  domain_id TEXT PRIMARY KEY,
  formalization_intensity REAL NOT NULL,
  abstraction_risk REAL NOT NULL,
  representation_risk REAL NOT NULL,
  delegation_level REAL NOT NULL,
  opacity REAL NOT NULL,
  optimization_pressure REAL NOT NULL,
  contestability_need REAL NOT NULL,
  institutional_consequence REAL NOT NULL,
  human_judgment_requirement REAL NOT NULL,
  governance_urgency REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS algorithmic_philosophy_review_map (
  domain_id TEXT PRIMARY KEY,
  formalization_intensity REAL NOT NULL,
  abstraction_risk REAL NOT NULL,
  representation_risk REAL NOT NULL,
  delegation_level REAL NOT NULL,
  opacity REAL NOT NULL,
  optimization_pressure REAL NOT NULL,
  contestability_need REAL NOT NULL,
  institutional_consequence REAL NOT NULL,
  human_judgment_requirement REAL NOT NULL,
  governance_urgency REAL NOT NULL,
  review_score REAL NOT NULL,
  review_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS delegation_risk_examples (
  case_id TEXT PRIMARY KEY,
  decision_severity REAL NOT NULL,
  automation_level REAL NOT NULL,
  opacity REAL NOT NULL,
  delegation_risk REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS philosophical_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
