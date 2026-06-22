CREATE TABLE IF NOT EXISTS documentation_records (
  system_id TEXT PRIMARY KEY,
  required_fields INTEGER NOT NULL,
  completed_fields INTEGER NOT NULL,
  accuracy REAL NOT NULL,
  specificity REAL NOT NULL,
  timeliness REAL NOT NULL,
  accessibility REAL NOT NULL,
  actionability REAL NOT NULL,
  model_card INTEGER NOT NULL,
  datasheet INTEGER NOT NULL,
  risk_register INTEGER NOT NULL,
  change_log INTEGER NOT NULL,
  appeal_documentation INTEGER NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS documentation_audit (
  system_id TEXT PRIMARY KEY,
  documentation_completeness_score REAL NOT NULL,
  artifact_coverage_score REAL NOT NULL,
  documentation_quality_score REAL NOT NULL,
  documentation_risk_score REAL NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS documentation_register (
  artifact TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
