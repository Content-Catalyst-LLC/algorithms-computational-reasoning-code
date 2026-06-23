CREATE TABLE IF NOT EXISTS computational_mapping_themes (
  theme_id TEXT PRIMARY KEY,
  spatial_representation REAL NOT NULL,
  coordinate_structure REAL NOT NULL,
  procedural_clarity REAL NOT NULL,
  institutional_use REAL NOT NULL,
  correction_awareness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS computational_mapping_map (
  theme_id TEXT PRIMARY KEY,
  spatial_representation REAL NOT NULL,
  coordinate_structure REAL NOT NULL,
  procedural_clarity REAL NOT NULL,
  institutional_use REAL NOT NULL,
  correction_awareness REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  mapping_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
