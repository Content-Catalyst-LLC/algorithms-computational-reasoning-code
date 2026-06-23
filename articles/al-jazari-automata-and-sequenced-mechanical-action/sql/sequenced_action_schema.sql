CREATE TABLE IF NOT EXISTS sequenced_action_themes (
  theme_id TEXT PRIMARY KEY,
  sequence_structure REAL NOT NULL,
  timing_control REAL NOT NULL,
  mechanical_embodiment REAL NOT NULL,
  conditional_action REAL NOT NULL,
  repeatability REAL NOT NULL,
  documentation_quality REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS sequenced_action_map (
  theme_id TEXT PRIMARY KEY,
  sequence_structure REAL NOT NULL,
  timing_control REAL NOT NULL,
  mechanical_embodiment REAL NOT NULL,
  conditional_action REAL NOT NULL,
  repeatability REAL NOT NULL,
  documentation_quality REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  sequenced_action_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
