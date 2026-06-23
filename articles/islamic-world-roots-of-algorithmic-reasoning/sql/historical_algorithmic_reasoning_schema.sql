CREATE TABLE IF NOT EXISTS historical_themes (
  theme_id TEXT PRIMARY KEY,
  procedural_explicitness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  practical_application REAL NOT NULL,
  representation_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS historical_algorithmic_reasoning_map (
  theme_id TEXT PRIMARY KEY,
  procedural_explicitness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  practical_application REAL NOT NULL,
  representation_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  significance_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS historical_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
