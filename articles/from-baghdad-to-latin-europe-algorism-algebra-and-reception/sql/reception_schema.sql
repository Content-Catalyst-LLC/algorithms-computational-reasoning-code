CREATE TABLE IF NOT EXISTS reception_themes (
  theme_id TEXT PRIMARY KEY,
  procedural_portability REAL NOT NULL,
  notation_change REAL NOT NULL,
  translation_pathway REAL NOT NULL,
  teaching_value REAL NOT NULL,
  practical_utility REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  trust_verification REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS reception_map (
  theme_id TEXT PRIMARY KEY,
  procedural_portability REAL NOT NULL,
  notation_change REAL NOT NULL,
  translation_pathway REAL NOT NULL,
  teaching_value REAL NOT NULL,
  practical_utility REAL NOT NULL,
  institutional_adoption REAL NOT NULL,
  trust_verification REAL NOT NULL,
  historical_significance REAL NOT NULL,
  ethical_caution REAL NOT NULL,
  modern_resonance REAL NOT NULL,
  reception_score REAL NOT NULL,
  interpretive_status TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interpretation_cautions (
  caution TEXT PRIMARY KEY,
  meaning TEXT NOT NULL
);
