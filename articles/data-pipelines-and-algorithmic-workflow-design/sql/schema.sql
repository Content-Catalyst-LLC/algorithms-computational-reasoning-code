DROP TABLE IF EXISTS pipeline_tasks;
CREATE TABLE pipeline_tasks (
  task_id TEXT PRIMARY KEY,
  task_name TEXT NOT NULL,
  depends_on TEXT,
  task_type TEXT NOT NULL,
  expected_output TEXT NOT NULL,
  validation_required INTEGER NOT NULL CHECK(validation_required IN (0,1)),
  governance_gate INTEGER NOT NULL CHECK(governance_gate IN (0,1))
);

DROP TABLE IF EXISTS pipeline_quality_checks;
CREATE TABLE pipeline_quality_checks (
  check_id TEXT PRIMARY KEY,
  check_name TEXT NOT NULL,
  dimension TEXT NOT NULL,
  passed INTEGER NOT NULL,
  total INTEGER NOT NULL,
  threshold REAL NOT NULL
);

DROP TABLE IF EXISTS pipeline_runs;
CREATE TABLE pipeline_runs (
  run_id INTEGER PRIMARY KEY,
  run_label TEXT NOT NULL,
  source_snapshot TEXT NOT NULL,
  pipeline_version TEXT NOT NULL,
  validation_pass_rate REAL NOT NULL,
  freshness_score REAL NOT NULL,
  lineage_coverage REAL NOT NULL,
  monitoring_status TEXT NOT NULL
);

INSERT INTO pipeline_tasks VALUES
('ingest_sources','Ingest source records',NULL,'ingestion','raw source table',1,0),
('validate_schema','Validate input schema','ingest_sources','validation','schema validation report',1,1),
('normalize_records','Normalize records','validate_schema','transformation','normalized records',1,0),
('join_metadata','Join metadata','normalize_records','transformation','enriched records',1,0),
('calculate_features','Calculate features','join_metadata','feature_engineering','feature table',1,0),
('build_index','Build search index','calculate_features','indexing','index artifact',1,1),
('publish_outputs','Publish outputs','build_index','delivery','published report and index',1,1),
('monitor_run','Monitor run','publish_outputs','observability','monitoring summary',1,0);

INSERT INTO pipeline_quality_checks VALUES
('schema_required_fields','Required fields present','validity',10,10,1.00),
('unique_record_id','Record IDs unique','uniqueness',995,1000,0.99),
('fresh_source_data','Source updated recently','freshness',1,1,1.00),
('lineage_present','Output rows have lineage','provenance',980,1000,0.95),
('null_rate_allowed','Null rates within bounds','completeness',96,100,0.95),
('join_coverage','Join coverage meets expectation','integrity',940,1000,0.90),
('monitoring_events','Monitoring events emitted','observability',8,8,1.00),
('governance_approval','Governance gate approved','governance',1,1,1.00);

INSERT INTO pipeline_runs VALUES
(1,'baseline run','source_snapshot_2026_06_18','commit_abc123',0.97,0.93,0.96,'healthy'),
(2,'stale source run','source_snapshot_2026_04_01','commit_abc123',0.91,0.28,0.94,'freshness warning'),
(3,'schema drift run','source_snapshot_2026_06_18','commit_def456',0.72,0.92,0.81,'schema warning');
