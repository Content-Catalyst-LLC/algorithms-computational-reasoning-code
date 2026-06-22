CREATE TABLE IF NOT EXISTS explanation_cases (
  case_id TEXT PRIMARY KEY,
  audience TEXT NOT NULL,
  faithfulness REAL NOT NULL,
  stability REAL NOT NULL,
  understandability REAL NOT NULL,
  actionability REAL NOT NULL,
  uncertainty_communication REAL NOT NULL,
  documentation_completeness REAL NOT NULL,
  contestability REAL NOT NULL,
  governance_readiness REAL NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS explanation_audit (
  case_id TEXT PRIMARY KEY,
  audience TEXT NOT NULL,
  explanation_quality_score REAL NOT NULL,
  transparency_capacity_score REAL NOT NULL,
  accountability_capacity_score REAL NOT NULL,
  explanation_risk_score REAL NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS explanation_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
