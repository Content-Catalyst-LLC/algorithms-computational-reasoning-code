DROP TABLE IF EXISTS missingness_profiles;
CREATE TABLE missingness_profiles (
  field TEXT PRIMARY KEY,
  missing_count INTEGER NOT NULL,
  total_count INTEGER NOT NULL,
  missingness_reason TEXT NOT NULL,
  handling_policy TEXT NOT NULL
);

DROP TABLE IF EXISTS quality_checks;
CREATE TABLE quality_checks (
  check_id TEXT PRIMARY KEY,
  dimension TEXT NOT NULL,
  passed INTEGER NOT NULL,
  total INTEGER NOT NULL,
  threshold REAL NOT NULL,
  gate_action TEXT NOT NULL
);

DROP TABLE IF EXISTS data_quality_cases;
CREATE TABLE data_quality_cases (
  case_name TEXT PRIMARY KEY,
  computational_use TEXT NOT NULL,
  completeness REAL NOT NULL,
  validity REAL NOT NULL,
  freshness REAL NOT NULL,
  provenance REAL NOT NULL,
  representativeness REAL NOT NULL,
  uncertainty_communication REAL NOT NULL
);

INSERT INTO missingness_profiles VALUES
('source_id',0,1000,'required field','block if missing'),
('publication_date',45,1000,'not collected in older source','flag historical coverage gap'),
('review_status',120,1000,'pending review','mark as pending and exclude from approved-only outputs'),
('citation_url',80,1000,'source unavailable or print-only','preserve source note and alternate citation'),
('confidence_score',310,1000,'not applicable to manually curated records','use structured missingness code'),
('entity_identifier',24,1000,'entity resolution pending','route to identity review'),
('freshness_timestamp',60,1000,'source does not expose update timestamp','display freshness limitation'),
('coverage_group',140,1000,'not collected by source','do not generalize by group');

INSERT INTO quality_checks VALUES
('required_source_id','completeness',1000,1000,1.00,'block'),
('valid_date_format','validity',985,1000,0.98,'review'),
('freshness_threshold','freshness',910,1000,0.90,'warn'),
('provenance_present','provenance',930,1000,0.95,'review'),
('schema_version_present','schema_stability',1000,1000,1.00,'block'),
('representativeness_reviewed','representativeness',760,1000,0.80,'review'),
('missingness_reason_present','missingness_documentation',820,1000,0.85,'review'),
('imputed_value_flagged','imputation_discipline',940,1000,0.95,'block'),
('uncertainty_note_present','uncertainty_communication',700,1000,0.80,'review');

INSERT INTO data_quality_cases VALUES
('Search metadata quality','search ranking and retrieval',0.84,0.86,0.78,0.88,0.76,0.74),
('AI retrieval provenance gaps','retrieval augmented generation',0.72,0.78,0.76,0.62,0.70,0.54),
('Scientific dataset with strong lineage','reproducible research',0.88,0.86,0.82,0.92,0.84,0.84),
('Opaque operational dashboard','management dashboard',0.46,0.54,0.42,0.34,0.36,0.16);
