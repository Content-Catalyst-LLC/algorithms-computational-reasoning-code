DROP TABLE IF EXISTS traceability_cases;
DROP TABLE IF EXISTS provenance_edges;

CREATE TABLE traceability_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  traceability_structure_choice TEXT NOT NULL,
  metadata_completeness REAL NOT NULL,
  source_clarity REAL NOT NULL,
  lineage_coverage REAL NOT NULL,
  version_control REAL NOT NULL,
  timestamp_quality REAL NOT NULL,
  schema_clarity REAL NOT NULL,
  integrity_checks REAL NOT NULL,
  access_governance REAL NOT NULL,
  reproducibility_support REAL NOT NULL,
  stewardship_readiness REAL NOT NULL
);

CREATE TABLE provenance_edges (
  from_id TEXT NOT NULL,
  to_id TEXT NOT NULL,
  relation TEXT NOT NULL,
  actor TEXT NOT NULL,
  timestamp TEXT NOT NULL
);

INSERT INTO traceability_cases VALUES
('Research dataset repository','A research dataset is published with documentation source records schema and reproducible workflow links','Dataset metadata with DOI schema source citations checksums license code version and lineage notes',0.92,0.94,0.86,0.90,0.88,0.90,0.90,0.86,0.90,0.88),
('AI model registry','A deployed model requires traceability for model version training data evaluation deployment and monitoring','Model registry with model cards dataset cards evaluation reports deployment logs and rollback metadata',0.88,0.84,0.86,0.92,0.88,0.84,0.84,0.90,0.84,0.90),
('Institutional case workflow','A public or institutional case record moves through review evidence gathering decision revision and publication','Structured case metadata event logs decision history evidence links access controls and chain-of-custody records',0.90,0.88,0.88,0.86,0.92,0.84,0.86,0.94,0.78,0.90),
('Knowledge library article system','A knowledge library connects article metadata article maps repository folders images citations and publication history','Article metadata records with slug map position source references image metadata GitHub folder version notes and related links',0.90,0.86,0.82,0.86,0.80,0.86,0.78,0.78,0.84,0.88);

INSERT INTO provenance_edges VALUES
('cleaning-script-a','raw-data-v1','used','pipeline','2026-06-17T12:00:00Z'),
('analysis-table-v1','cleaning-script-a','was_generated_by','pipeline','2026-06-17T12:10:00Z'),
('model-run-42','analysis-table-v1','used','model-runner','2026-06-17T12:20:00Z'),
('published-chart-v1','model-run-42','was_generated_by','publisher','2026-06-17T12:30:00Z'),
('published-chart-v1','raw-data-v1','was_derived_from','publisher','2026-06-17T12:30:00Z');
