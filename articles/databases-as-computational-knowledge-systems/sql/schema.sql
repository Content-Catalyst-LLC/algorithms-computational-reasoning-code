DROP TABLE IF EXISTS database_knowledge_cases;
CREATE TABLE database_knowledge_cases (
  case_name TEXT PRIMARY KEY,
  system_context TEXT,
  database_role TEXT,
  schema_clarity REAL,
  relationship_modeling REAL,
  constraint_discipline REAL,
  query_expressiveness REAL,
  indexing_strategy REAL,
  transaction_reliability REAL,
  metadata_quality REAL,
  provenance_lineage REAL,
  access_control REAL,
  correction_workflow REAL,
  retention_policy REAL,
  interoperability REAL,
  governance_readiness REAL,
  communication_clarity REAL
);

DROP TABLE IF EXISTS research_library_articles;
CREATE TABLE research_library_articles (
  article_id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  publication_status TEXT NOT NULL CHECK(publication_status IN ('draft','planned','published')),
  created_at TEXT NOT NULL
);

DROP TABLE IF EXISTS research_library_repositories;
CREATE TABLE research_library_repositories (
  repo_id INTEGER PRIMARY KEY,
  article_id INTEGER NOT NULL,
  repo_url TEXT NOT NULL UNIQUE,
  license_status TEXT NOT NULL,
  FOREIGN KEY(article_id) REFERENCES research_library_articles(article_id)
);

INSERT INTO database_knowledge_cases VALUES
('Research library database','Articles authors categories references images repositories and metadata are connected for publication and discovery','institutional knowledge archive',0.88,0.86,0.80,0.84,0.78,0.76,0.90,0.84,0.78,0.76,0.82,0.78,0.82,0.84),
('AI feature store','Reusable features support model training inference monitoring and evaluation','model input knowledge infrastructure',0.82,0.78,0.76,0.80,0.82,0.72,0.80,0.86,0.82,0.70,0.76,0.84,0.78,0.76),
('Opaque spreadsheet like data store','Important institutional records are stored without stable schema keys constraints metadata provenance or correction workflow','fragile operational memory',0.24,0.20,0.16,0.30,0.18,0.18,0.18,0.14,0.26,0.16,0.22,0.18,0.16,0.22);

INSERT INTO research_library_articles VALUES
(1,'databases-as-computational-knowledge-systems','Databases as Computational Knowledge Systems','published','2026-06-18'),
(2,'relational-databases-and-structured-representation','Relational Databases and Structured Representation','planned','2026-06-18');

INSERT INTO research_library_repositories VALUES
(1,1,'https://github.com/Content-Catalyst-LLC/algorithms-computational-reasoning-code/tree/main/articles/databases-as-computational-knowledge-systems/','MIT');
