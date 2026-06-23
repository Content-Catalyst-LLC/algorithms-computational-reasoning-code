CREATE TABLE IF NOT EXISTS procedural_legacy_themes (
  theme_id TEXT PRIMARY KEY,
  procedure REAL NOT NULL,
  representation REAL NOT NULL,
  transmission REAL NOT NULL,
  application REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS al_khwarizmi_procedural_legacy_map (
  theme_id TEXT PRIMARY KEY,
  procedure REAL NOT NULL,
  representation REAL NOT NULL,
  transmission REAL NOT NULL,
  application REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  legacy_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
