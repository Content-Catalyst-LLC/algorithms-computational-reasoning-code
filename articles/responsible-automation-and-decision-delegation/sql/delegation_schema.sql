CREATE TABLE IF NOT EXISTS delegation_contexts (
  context_id TEXT PRIMARY KEY,
  evidence_quality REAL NOT NULL,
  validation REAL NOT NULL,
  reversibility REAL NOT NULL,
  contestability REAL NOT NULL,
  governance REAL NOT NULL,
  human_review REAL NOT NULL,
  automated_final_actions INTEGER NOT NULL,
  total_decisions INTEGER NOT NULL,
  stakes REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS delegation_readiness_audit (
  context_id TEXT PRIMARY KEY,
  delegation_readiness_score REAL NOT NULL,
  automation_reliance_score REAL NOT NULL,
  delegation_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL,
  status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS delegation_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
