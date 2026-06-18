DROP TABLE IF EXISTS concurrency_cases;
CREATE TABLE concurrency_cases (case_name TEXT PRIMARY KEY, computational_goal TEXT NOT NULL, dependency_discipline REAL NOT NULL, shared_state_control REAL NOT NULL, synchronization_design REAL NOT NULL, idempotence REAL NOT NULL, observability REAL NOT NULL, failure_isolation REAL NOT NULL);
DROP TABLE IF EXISTS task_graph;
CREATE TABLE task_graph (task_id TEXT PRIMARY KEY, task_name TEXT NOT NULL, depends_on TEXT, parallel_group TEXT NOT NULL, shared_state INTEGER NOT NULL CHECK(shared_state IN (0,1)), governance_gate INTEGER NOT NULL CHECK(governance_gate IN (0,1)));
DROP TABLE IF EXISTS performance_examples;
CREATE TABLE performance_examples (processors INTEGER PRIMARY KEY, sequential_fraction REAL NOT NULL, sequential_time REAL NOT NULL, parallel_time REAL NOT NULL);
INSERT INTO concurrency_cases VALUES
('Parallel document indexing','increase indexing throughput while preserving source and index consistency',0.84,0.82,0.80,0.84,0.82,0.84),
('Asynchronous AI retrieval service','reduce latency while preserving source-backed responses and traceability',0.78,0.76,0.74,0.72,0.78,0.72),
('Parallel scientific simulation','increase scenario coverage while preserving reproducible outputs',0.86,0.88,0.82,0.86,0.78,0.82),
('Unsafe shared-state worker pool','speed up batch processing',0.42,0.24,0.22,0.26,0.28,0.30);
INSERT INTO task_graph VALUES
('ingest_documents','Ingest documents',NULL,'source',0,0),
('parse_documents','Parse documents','ingest_documents','document_workers',0,0),
('extract_metadata','Extract metadata','ingest_documents','document_workers',0,0),
('generate_embeddings','Generate embeddings','parse_documents','embedding_workers',0,0),
('validate_partitions','Validate partitions','parse_documents|extract_metadata','validation_workers',0,1),
('merge_index','Merge index','generate_embeddings|validate_partitions','index_merge',1,1),
('publish_snapshot','Publish snapshot','merge_index','publish',1,1),
('monitor_run','Monitor run','publish_snapshot','observability',0,0);
INSERT INTO performance_examples VALUES (1,0.12,120.0,120.0),(2,0.12,120.0,66.0),(4,0.12,120.0,38.0),(8,0.12,120.0,28.0),(16,0.12,120.0,24.0),(32,0.12,120.0,22.0);
