CREATE TABLE IF NOT EXISTS verbal_procedure_themes (
  theme_id TEXT PRIMARY KEY,
  procedural_clarity REAL NOT NULL,
  representation_dependence REAL NOT NULL,
  pedagogical_value REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  practical_use REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS verbal_procedure_map (
  theme_id TEXT PRIMARY KEY,
  procedural_clarity REAL NOT NULL,
  representation_dependence REAL NOT NULL,
  pedagogical_value REAL NOT NULL,
  transmission_importance REAL NOT NULL,
  practical_use REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  verbal_procedure_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
