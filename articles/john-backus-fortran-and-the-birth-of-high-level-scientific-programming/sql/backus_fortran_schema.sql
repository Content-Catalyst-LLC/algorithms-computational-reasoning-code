CREATE TABLE IF NOT EXISTS backus_themes (
  theme_id TEXT PRIMARY KEY,
  high_level_language REAL NOT NULL,
  scientific_expression REAL NOT NULL,
  compiler_optimization REAL NOT NULL,
  numerical_relevance REAL NOT NULL,
  portability REAL NOT NULL,
  performance_credibility REAL NOT NULL,
  language_history REAL NOT NULL,
  formal_specification REAL NOT NULL,
  maintainability REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS backus_fortran_scientific_programming_map (
  theme_id TEXT PRIMARY KEY,
  high_level_language REAL NOT NULL,
  scientific_expression REAL NOT NULL,
  compiler_optimization REAL NOT NULL,
  numerical_relevance REAL NOT NULL,
  portability REAL NOT NULL,
  performance_credibility REAL NOT NULL,
  language_history REAL NOT NULL,
  formal_specification REAL NOT NULL,
  maintainability REAL NOT NULL,
  governance_caution REAL NOT NULL,
  birth_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS formula_translation_example (
  x REAL PRIMARY KEY,
  a REAL NOT NULL,
  b REAL NOT NULL,
  c REAL NOT NULL,
  y REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
