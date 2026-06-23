CREATE TABLE IF NOT EXISTS transfer_themes (
  theme_id TEXT PRIMARY KEY,
  procedural_fidelity REAL NOT NULL,
  vocabulary_mapping REAL NOT NULL,
  diagram_table_preservation REAL NOT NULL,
  institutional_support REAL NOT NULL,
  error_control REAL NOT NULL,
  adaptation REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS transfer_map (
  theme_id TEXT PRIMARY KEY,
  procedural_fidelity REAL NOT NULL,
  vocabulary_mapping REAL NOT NULL,
  diagram_table_preservation REAL NOT NULL,
  institutional_support REAL NOT NULL,
  error_control REAL NOT NULL,
  adaptation REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  transfer_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
