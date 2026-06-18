DROP TABLE IF EXISTS divide_conquer_cases;
DROP TABLE IF EXISTS partition_records;

CREATE TABLE divide_conquer_cases (
  case_name TEXT PRIMARY KEY, problem_context TEXT, design_choice TEXT,
  decomposition_clarity REAL, base_case_clarity REAL, subproblem_validity REAL,
  progress_toward_termination REAL, combination_correctness REAL, recurrence_awareness REAL,
  edge_case_coverage REAL, boundary_handling REAL, traceability REAL, governance_readiness REAL
);

CREATE TABLE partition_records (
  partition_id TEXT PRIMARY KEY,
  source_size INTEGER,
  subproblem_size INTEGER,
  base_case TEXT,
  combine_rule TEXT,
  boundary_check TEXT
);

INSERT INTO divide_conquer_cases VALUES
('Merge sort workflow','A sorting workflow divides records into halves and merges sorted results','Balanced recursive merge sort with stable merge and explicit base case',0.92,0.92,0.90,0.92,0.92,0.90,0.86,0.84,0.84,0.82),
('Document chunking for retrieval','Long documents are divided into chunks for indexing and retrieval','Chunking with overlap metadata preservation boundary checks and citation traceability',0.84,0.78,0.82,0.88,0.76,0.70,0.78,0.86,0.90,0.88),
('Parallel aggregation pipeline','A large dataset is partitioned summarized independently and recombined','Map-reduce style partitioning with deterministic aggregation and partition-level logs',0.88,0.82,0.86,0.88,0.86,0.78,0.82,0.82,0.90,0.88),
('Unreviewed spatial partition','A spatial model divides a region into zones without checking boundary interactions','Recursive partitioning with weak boundary validation and limited recombination evidence',0.64,0.58,0.60,0.72,0.46,0.52,0.44,0.30,0.42,0.38);

INSERT INTO partition_records VALUES
('P-001',1024,512,'false','merge sorted halves','not_applicable'),
('P-002',512,256,'false','merge sorted halves','not_applicable'),
('P-003',128,64,'false','aggregate partial summaries','cross_partition_total_check'),
('P-004',1,1,'true','direct return','not_applicable'),
('P-005',5000,1250,'false','map-reduce aggregation','partition_balance_check');
