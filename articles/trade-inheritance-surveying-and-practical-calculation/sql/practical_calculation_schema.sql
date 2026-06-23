CREATE TABLE IF NOT EXISTS practical_calculation_themes (
  theme_id TEXT PRIMARY KEY,
  procedure REAL NOT NULL,
  representation REAL NOT NULL,
  institutional_importance REAL NOT NULL,
  verification REAL NOT NULL,
  transmission REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS practical_calculation_procedure_map (
  theme_id TEXT PRIMARY KEY,
  procedure REAL NOT NULL,
  representation REAL NOT NULL,
  institutional_importance REAL NOT NULL,
  verification REAL NOT NULL,
  transmission REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  practical_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
