CREATE TABLE IF NOT EXISTS programming_language_traditions (
  tradition_id TEXT PRIMARY KEY,
  abstraction REAL NOT NULL,
  performance_orientation REAL NOT NULL,
  readability REAL NOT NULL,
  formal_specification REAL NOT NULL,
  ecosystem_depth REAL NOT NULL,
  domain_fit REAL NOT NULL,
  safety_orientation REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  historical_influence REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS programming_language_history_map (
  tradition_id TEXT PRIMARY KEY,
  abstraction REAL NOT NULL,
  performance_orientation REAL NOT NULL,
  readability REAL NOT NULL,
  formal_specification REAL NOT NULL,
  ecosystem_depth REAL NOT NULL,
  domain_fit REAL NOT NULL,
  safety_orientation REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  historical_influence REAL NOT NULL,
  governance_caution REAL NOT NULL,
  history_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS language_family_edges (
  source TEXT NOT NULL,
  target TEXT NOT NULL,
  relation TEXT NOT NULL,
  PRIMARY KEY (source, target, relation)
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
