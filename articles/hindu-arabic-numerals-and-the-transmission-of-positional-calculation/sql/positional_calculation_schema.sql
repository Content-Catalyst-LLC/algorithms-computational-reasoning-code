CREATE TABLE IF NOT EXISTS positional_calculation_themes (
  theme_id TEXT PRIMARY KEY,
  representation REAL NOT NULL,
  procedure REAL NOT NULL,
  transmission REAL NOT NULL,
  practical_use REAL NOT NULL,
  pedagogy REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS positional_calculation_transmission_map (
  theme_id TEXT PRIMARY KEY,
  representation REAL NOT NULL,
  procedure REAL NOT NULL,
  transmission REAL NOT NULL,
  practical_use REAL NOT NULL,
  pedagogy REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  positional_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
