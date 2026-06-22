CREATE TABLE IF NOT EXISTS human_review_contexts (
  context_id TEXT PRIMARY KEY,
  time REAL NOT NULL,
  information REAL NOT NULL,
  authority REAL NOT NULL,
  training REAL NOT NULL,
  protection REAL NOT NULL,
  accepted_recommendations INTEGER NOT NULL,
  total_recommendations INTEGER NOT NULL,
  overrides INTEGER NOT NULL,
  reviewed_cases INTEGER NOT NULL,
  escalation_capacity REAL NOT NULL,
  contestability REAL NOT NULL,
  governance REAL NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS human_review_audit (
  context_id TEXT PRIMARY KEY,
  review_capacity_score REAL NOT NULL,
  reliance_score REAL NOT NULL,
  override_rate REAL NOT NULL,
  judgment_capacity_score REAL NOT NULL,
  review_risk_score REAL NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS human_review_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
