CREATE TABLE IF NOT EXISTS platform_systems (
  system_id TEXT PRIMARY KEY,
  engagement_pressure REAL NOT NULL,
  transparency REAL NOT NULL,
  contestability REAL NOT NULL,
  moderation_readiness REAL NOT NULL,
  creator_impact REAL NOT NULL,
  public_knowledge_impact REAL NOT NULL,
  user_control REAL NOT NULL,
  governance REAL NOT NULL,
  monitoring REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS attention_system_audit (
  system_id TEXT PRIMARY KEY,
  governance_readiness_score REAL NOT NULL,
  attention_risk_score REAL NOT NULL,
  platform_risk_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS platform_governance_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
