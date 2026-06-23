CREATE TABLE IF NOT EXISTS algebraic_procedure_themes (
  theme_id TEXT PRIMARY KEY,
  classification REAL NOT NULL,
  transformation REAL NOT NULL,
  representation REAL NOT NULL,
  demonstration REAL NOT NULL,
  practical_use REAL NOT NULL,
  transmission REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS rule_governed_algebra_map (
  theme_id TEXT PRIMARY KEY,
  classification REAL NOT NULL,
  transformation REAL NOT NULL,
  representation REAL NOT NULL,
  demonstration REAL NOT NULL,
  practical_use REAL NOT NULL,
  transmission REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  procedure_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
