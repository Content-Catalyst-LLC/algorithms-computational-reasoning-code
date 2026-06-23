CREATE TABLE IF NOT EXISTS khwarizmi_themes (
  theme_id TEXT PRIMARY KEY,
  arithmetic_method REAL NOT NULL,
  algebraic_procedure REAL NOT NULL,
  representation REAL NOT NULL,
  transformation REAL NOT NULL,
  proof_relation REAL NOT NULL,
  transmission REAL NOT NULL,
  etymology REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  historiographic_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS khwarizmi_algorithmic_method_map (
  theme_id TEXT PRIMARY KEY,
  arithmetic_method REAL NOT NULL,
  algebraic_procedure REAL NOT NULL,
  representation REAL NOT NULL,
  transformation REAL NOT NULL,
  proof_relation REAL NOT NULL,
  transmission REAL NOT NULL,
  etymology REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  historiographic_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  method_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
