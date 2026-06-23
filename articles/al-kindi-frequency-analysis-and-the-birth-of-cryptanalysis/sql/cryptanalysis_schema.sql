CREATE TABLE IF NOT EXISTS sample_frequency_table (
  symbol TEXT PRIMARY KEY,
  count INTEGER NOT NULL,
  relative_frequency REAL NOT NULL,
  rank INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cryptanalysis_themes (
  theme_id TEXT PRIMARY KEY,
  linguistic_evidence REAL NOT NULL,
  counting_procedure REAL NOT NULL,
  inferential_structure REAL NOT NULL,
  cryptanalytic_relevance REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS cryptanalysis_map (
  theme_id TEXT PRIMARY KEY,
  linguistic_evidence REAL NOT NULL,
  counting_procedure REAL NOT NULL,
  inferential_structure REAL NOT NULL,
  cryptanalytic_relevance REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  cryptanalysis_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
