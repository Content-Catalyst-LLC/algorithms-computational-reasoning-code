DROP TABLE IF EXISTS ranking_documents;
CREATE TABLE ranking_documents (
  doc_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  category TEXT NOT NULL,
  tags TEXT NOT NULL,
  publication_year INTEGER NOT NULL,
  source_authority REAL NOT NULL,
  metadata_completeness REAL NOT NULL
);

DROP TABLE IF EXISTS relevance_judgments;
CREATE TABLE relevance_judgments (
  judgment_id INTEGER PRIMARY KEY,
  query_text TEXT NOT NULL,
  doc_id TEXT NOT NULL,
  relevance_grade INTEGER NOT NULL CHECK(relevance_grade BETWEEN 0 AND 3)
);

DROP TABLE IF EXISTS ranking_events;
CREATE TABLE ranking_events (
  event_id INTEGER PRIMARY KEY,
  query_text TEXT NOT NULL,
  doc_id TEXT NOT NULL,
  rank_position INTEGER NOT NULL,
  clicked INTEGER NOT NULL CHECK(clicked IN (0,1))
);

INSERT INTO ranking_documents VALUES
('doc_1','Ranking Signals','Ranking signals combine lexical evidence metadata freshness authority and feedback.','Algorithms','ranking relevance search',2026,0.86,0.92),
('doc_2','Information Retrieval','Information retrieval systems use indexes query processing and evaluation.','Algorithms','search retrieval indexing',2026,0.82,0.88),
('doc_3','Semantic Embeddings','Semantic embeddings support similarity search and retrieval augmented AI systems.','Algorithms','semantic embeddings retrieval',2026,0.76,0.82),
('doc_4','Search Governance','Search governance reviews ranking explanations provenance and source quality.','Algorithms','governance ranking provenance',2026,0.88,0.90),
('doc_5','Database Optimization','Database optimization uses query plans indexes joins and cardinality estimates.','Algorithms','database query optimization',2026,0.80,0.84);

INSERT INTO relevance_judgments VALUES
(1,'ranking metadata search governance','doc_1',3),
(2,'ranking metadata search governance','doc_4',3),
(3,'ranking metadata search governance','doc_2',1),
(4,'semantic retrieval','doc_3',3),
(5,'semantic retrieval','doc_2',1);

INSERT INTO ranking_events VALUES
(1,'ranking metadata search governance','doc_4',1,1),
(2,'ranking metadata search governance','doc_1',2,1),
(3,'ranking metadata search governance','doc_2',3,0),
(4,'semantic retrieval','doc_3',1,1),
(5,'semantic retrieval','doc_2',2,0);
