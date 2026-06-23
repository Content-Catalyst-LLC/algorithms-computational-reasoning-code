CREATE TABLE IF NOT EXISTS astronomical_prediction_themes (
  theme_id TEXT PRIMARY KEY,
  table_structure REAL NOT NULL,
  procedural_clarity REAL NOT NULL,
  predictive_function REAL NOT NULL,
  institutional_use REAL NOT NULL,
  correction_awareness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS astronomical_prediction_map (
  theme_id TEXT PRIMARY KEY,
  table_structure REAL NOT NULL,
  procedural_clarity REAL NOT NULL,
  predictive_function REAL NOT NULL,
  institutional_use REAL NOT NULL,
  correction_awareness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  prediction_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
