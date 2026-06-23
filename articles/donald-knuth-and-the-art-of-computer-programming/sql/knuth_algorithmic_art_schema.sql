CREATE TABLE IF NOT EXISTS knuth_themes (
  theme_id TEXT PRIMARY KEY,
  algorithm_analysis REAL NOT NULL,
  exposition REAL NOT NULL,
  mathematical_rigor REAL NOT NULL,
  historical_depth REAL NOT NULL,
  implementation_relevance REAL NOT NULL,
  typography_relevance REAL NOT NULL,
  literate_programming REAL NOT NULL,
  pedagogy REAL NOT NULL,
  maintainability REAL NOT NULL,
  governance_caution REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS knuth_algorithmic_art_map (
  theme_id TEXT PRIMARY KEY,
  algorithm_analysis REAL NOT NULL,
  exposition REAL NOT NULL,
  mathematical_rigor REAL NOT NULL,
  historical_depth REAL NOT NULL,
  implementation_relevance REAL NOT NULL,
  typography_relevance REAL NOT NULL,
  literate_programming REAL NOT NULL,
  pedagogy REAL NOT NULL,
  maintainability REAL NOT NULL,
  governance_caution REAL NOT NULL,
  art_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS comparison_sort_lower_bounds (
  n INTEGER PRIMARY KEY,
  comparison_sort_lower_bound_log2_factorial REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
