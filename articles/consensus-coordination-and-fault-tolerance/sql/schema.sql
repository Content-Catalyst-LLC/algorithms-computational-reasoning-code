DROP TABLE IF EXISTS consensus_cases;
CREATE TABLE consensus_cases(case_name TEXT PRIMARY KEY, agreement_clarity REAL, quorum_design REAL, failure_model REAL, leader_election REAL, partition_behavior REAL, retry_idempotence REAL, observability REAL, recovery_design REAL, governance_review REAL);
INSERT INTO consensus_cases VALUES
('Replicated database commit',0.88,0.90,0.86,0.84,0.84,0.82,0.82,0.84,0.76),
('Search index snapshot publication',0.82,0.74,0.78,0.68,0.78,0.84,0.80,0.78,0.78),
('AI retrieval fail-closed policy',0.78,0.62,0.76,0.58,0.80,0.74,0.82,0.72,0.82),
('Unsafe split-brain service',0.28,0.18,0.30,0.22,0.12,0.30,0.26,0.22,0.20);
DROP TABLE IF EXISTS quorum_records;
CREATE TABLE quorum_records(cluster_id TEXT PRIMARY KEY,node_count INTEGER,quorum_size INTEGER,node_availability REAL,failure_model TEXT);
INSERT INTO quorum_records VALUES ('cluster_3',3,2,0.99,'crash'),('cluster_5',5,3,0.99,'crash'),('cluster_7',7,4,0.99,'crash'),('cluster_9',9,5,0.99,'crash');
