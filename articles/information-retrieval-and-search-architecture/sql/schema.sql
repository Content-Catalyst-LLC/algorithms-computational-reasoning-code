DROP TABLE IF EXISTS search_documents;
CREATE TABLE search_documents (
  doc_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  category TEXT NOT NULL,
  tags TEXT NOT NULL,
  publication_year INTEGER NOT NULL
);

DROP TABLE IF EXISTS search_logs;
CREATE TABLE search_logs (
  log_id INTEGER PRIMARY KEY,
  query_text TEXT NOT NULL,
  result_count INTEGER NOT NULL,
  clicked_doc_id TEXT,
  zero_result INTEGER NOT NULL CHECK(zero_result IN (0,1))
);

DROP TABLE IF EXISTS relevance_judgments;
CREATE TABLE relevance_judgments (
  judgment_id INTEGER PRIMARY KEY,
  query_text TEXT NOT NULL,
  doc_id TEXT NOT NULL,
  relevance_grade INTEGER NOT NULL CHECK(relevance_grade BETWEEN 0 AND 3)
);

INSERT INTO search_documents VALUES
('doc_1','Information Retrieval','Information retrieval uses indexing ranking and evaluation to support search.','Algorithms','search indexing retrieval',2026),
('doc_2','Database Optimization','Database optimization uses query plans indexes joins and cardinality estimates.','Algorithms','database query optimization',2026),
('doc_3','Metadata Provenance','Metadata provenance and traceability improve knowledge system governance.','Algorithms','metadata provenance governance',2026),
('doc_4','Search Architecture','Search architecture combines documents metadata inverted indexes ranking filters and logs.','Algorithms','search architecture metadata',2026),
('doc_5','Vector Embeddings','Vector embeddings support semantic similarity search and retrieval augmented systems.','Algorithms','embeddings semantic retrieval',2026);

INSERT INTO search_logs VALUES
(1,'search indexing metadata',3,'doc_4',0),
(2,'query optimization',2,'doc_2',0),
(3,'missing source metadata',1,'doc_3',0),
(4,'nonexistent topic phrase',0,NULL,1);

INSERT INTO relevance_judgments VALUES
(1,'search indexing metadata','doc_1',2),
(2,'search indexing metadata','doc_4',3),
(3,'search indexing metadata','doc_2',1),
(4,'query optimization','doc_2',3),
(5,'query optimization','doc_4',1);
