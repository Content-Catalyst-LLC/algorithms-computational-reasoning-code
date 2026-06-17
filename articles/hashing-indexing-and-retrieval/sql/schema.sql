DROP TABLE IF EXISTS hashing_retrieval_cases;
DROP TABLE IF EXISTS synthetic_documents;
DROP TABLE IF EXISTS inverted_index_terms;

CREATE TABLE hashing_retrieval_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  retrieval_structure_choice TEXT NOT NULL,
  key_clarity REAL NOT NULL,
  hash_suitability REAL NOT NULL,
  collision_handling REAL NOT NULL,
  index_coverage REAL NOT NULL,
  retrieval_speed_fit REAL NOT NULL,
  freshness_control REAL NOT NULL,
  ranking_transparency REAL NOT NULL,
  metadata_provenance REAL NOT NULL,
  security_boundary_clarity REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE synthetic_documents (
  doc_id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  source TEXT NOT NULL,
  version INTEGER NOT NULL
);

CREATE TABLE inverted_index_terms (
  term TEXT NOT NULL,
  doc_id TEXT NOT NULL,
  field_name TEXT NOT NULL,
  PRIMARY KEY (term, doc_id, field_name)
);

INSERT INTO hashing_retrieval_cases VALUES
('Article metadata dictionary','A knowledge library retrieves article metadata by stable slug','Hash-map dictionary keyed by canonical slug with source and version metadata',0.90,0.86,0.84,0.88,0.90,0.82,0.76,0.86,0.78,0.84),
('Case status database index','Institutional records need retrieval by status owner deadline and review stage','Composite database index with audit metadata freshness checks and access controls',0.86,0.72,0.80,0.88,0.86,0.86,0.78,0.90,0.86,0.90),
('Search inverted index','Documents are retrieved by query terms metadata filters and ranking signals','Inverted index with term positions field weights timestamps and ranking explanations',0.82,0.76,0.78,0.86,0.88,0.82,0.84,0.86,0.80,0.86),
('Cache for expensive computations','Repeated model calculations are reused when inputs and parameters are unchanged','Memoization cache keyed by normalized input hash parameter version and expiration policy',0.84,0.88,0.82,0.80,0.92,0.84,0.70,0.84,0.82,0.84);

INSERT INTO synthetic_documents VALUES
('doc-1','Hashing basics','Hashing supports fast lookup by key.','synthetic',1),
('doc-2','Indexing basics','Indexing supports retrieval across documents and metadata.','synthetic',1),
('doc-3','Retrieval quality','Retrieval quality depends on freshness provenance and ranking.','synthetic',1),
('doc-4','Scalable access','Hashing and indexing support scalable retrieval.','synthetic',1);

INSERT INTO inverted_index_terms VALUES
('hashing','doc-1','body'),
('lookup','doc-1','body'),
('indexing','doc-2','body'),
('retrieval','doc-2','body'),
('retrieval','doc-3','body'),
('freshness','doc-3','body'),
('provenance','doc-3','body'),
('ranking','doc-3','body'),
('hashing','doc-4','body'),
('indexing','doc-4','body'),
('retrieval','doc-4','body');
