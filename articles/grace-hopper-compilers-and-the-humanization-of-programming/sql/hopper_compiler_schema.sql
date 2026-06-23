CREATE TABLE IF NOT EXISTS hopper_themes (
  theme_id TEXT PRIMARY KEY,
  compiler_centrality REAL NOT NULL,
  human_readability REAL NOT NULL,
  portability REAL NOT NULL,
  documentation REAL NOT NULL,
  standards REAL NOT NULL,
  debugging REAL NOT NULL,
  business_relevance REAL NOT NULL,
  institutional_scale REAL NOT NULL,
  abstraction REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS hopper_compiler_humanization_map (
  theme_id TEXT PRIMARY KEY,
  compiler_centrality REAL NOT NULL,
  human_readability REAL NOT NULL,
  portability REAL NOT NULL,
  documentation REAL NOT NULL,
  standards REAL NOT NULL,
  debugging REAL NOT NULL,
  business_relevance REAL NOT NULL,
  institutional_scale REAL NOT NULL,
  abstraction REAL NOT NULL,
  governance_caution REAL NOT NULL,
  humanization_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
