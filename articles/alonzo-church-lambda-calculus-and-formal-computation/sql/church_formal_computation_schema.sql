CREATE TABLE IF NOT EXISTS church_themes (
  theme_id TEXT PRIMARY KEY,
  formalization REAL NOT NULL,
  functional_abstraction REAL NOT NULL,
  symbolic_transformation REAL NOT NULL,
  substitution REAL NOT NULL,
  reduction REAL NOT NULL,
  computability REAL NOT NULL,
  undecidability REAL NOT NULL,
  type_influence REAL NOT NULL,
  programming_relevance REAL NOT NULL,
  ai_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS church_formal_computation_map (
  theme_id TEXT PRIMARY KEY,
  formalization REAL NOT NULL,
  functional_abstraction REAL NOT NULL,
  symbolic_transformation REAL NOT NULL,
  substitution REAL NOT NULL,
  reduction REAL NOT NULL,
  computability REAL NOT NULL,
  undecidability REAL NOT NULL,
  type_influence REAL NOT NULL,
  programming_relevance REAL NOT NULL,
  ai_caution REAL NOT NULL,
  formal_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
