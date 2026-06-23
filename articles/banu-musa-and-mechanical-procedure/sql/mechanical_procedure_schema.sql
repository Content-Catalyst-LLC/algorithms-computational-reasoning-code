CREATE TABLE IF NOT EXISTS mechanical_procedure_themes (
  theme_id TEXT PRIMARY KEY,
  mechanical_structure REAL NOT NULL,
  procedural_sequence REAL NOT NULL,
  conditional_control REAL NOT NULL,
  hidden_state REAL NOT NULL,
  feedback_potential REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS mechanical_procedure_map (
  theme_id TEXT PRIMARY KEY,
  mechanical_structure REAL NOT NULL,
  procedural_sequence REAL NOT NULL,
  conditional_control REAL NOT NULL,
  hidden_state REAL NOT NULL,
  feedback_potential REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  mechanical_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
