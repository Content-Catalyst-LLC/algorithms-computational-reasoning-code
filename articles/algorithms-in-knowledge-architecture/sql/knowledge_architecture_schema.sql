CREATE TABLE IF NOT EXISTS knowledge_objects (
  object_id TEXT PRIMARY KEY,
  metadata_completeness REAL NOT NULL,
  taxonomy_fit REAL NOT NULL,
  search_readiness REAL NOT NULL,
  link_quality REAL NOT NULL,
  recommendation_quality REAL NOT NULL,
  provenance REAL NOT NULL,
  freshness REAL NOT NULL,
  editorial_review REAL NOT NULL,
  representation_risk REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS knowledge_architecture_audit (
  object_id TEXT PRIMARY KEY,
  architecture_readiness_score REAL NOT NULL,
  maintenance_risk_score REAL NOT NULL,
  governance_readiness_score REAL NOT NULL,
  recommendation TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS knowledge_architecture_register (
  control TEXT PRIMARY KEY,
  review_question TEXT,
  status TEXT
);
