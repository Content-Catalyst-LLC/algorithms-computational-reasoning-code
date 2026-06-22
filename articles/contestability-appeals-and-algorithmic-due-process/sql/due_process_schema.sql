CREATE TABLE IF NOT EXISTS algorithmic_due_process_contexts (
  case_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  stakes REAL NOT NULL,
  notice REAL NOT NULL,
  reasons REAL NOT NULL,
  evidence_access REAL NOT NULL,
  human_review REAL NOT NULL,
  correction_capacity REAL NOT NULL,
  remedy_capacity REAL NOT NULL,
  appeal_burden REAL NOT NULL,
  resolution_days INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS contestability_appeals_audit (
  case_id TEXT PRIMARY KEY,
  domain TEXT,
  stakes REAL,
  contestability_score REAL,
  appeal_effectiveness_score REAL,
  procedural_risk_score REAL,
  appeal_burden REAL,
  resolution_days INTEGER,
  status TEXT
);

CREATE TABLE IF NOT EXISTS due_process_governance_register (
  item TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
