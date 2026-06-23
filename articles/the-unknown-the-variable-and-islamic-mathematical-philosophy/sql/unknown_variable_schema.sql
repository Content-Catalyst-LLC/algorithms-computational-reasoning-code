CREATE TABLE IF NOT EXISTS unknown_variable_themes (
  theme_id TEXT PRIMARY KEY,
  unknown_representation REAL NOT NULL,
  procedural_transformation REAL NOT NULL,
  abstraction REAL NOT NULL,
  proof_relation REAL NOT NULL,
  translation_continuity REAL NOT NULL,
  practical_grounding REAL NOT NULL,
  philosophical_depth REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS unknown_variable_map (
  theme_id TEXT PRIMARY KEY,
  unknown_representation REAL NOT NULL,
  procedural_transformation REAL NOT NULL,
  abstraction REAL NOT NULL,
  proof_relation REAL NOT NULL,
  translation_continuity REAL NOT NULL,
  practical_grounding REAL NOT NULL,
  philosophical_depth REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  unknown_variable_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
