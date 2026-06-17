DROP TABLE IF EXISTS embedding_system_cases;
DROP TABLE IF EXISTS synthetic_vectors;

CREATE TABLE embedding_system_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  embedding_structure_choice TEXT NOT NULL,
  representation_fit REAL NOT NULL,
  model_documentation REAL NOT NULL,
  vector_compatibility REAL NOT NULL,
  similarity_interpretability REAL NOT NULL,
  retrieval_evidence REAL NOT NULL,
  metadata_provenance REAL NOT NULL,
  bias_review REAL NOT NULL,
  drift_monitoring REAL NOT NULL,
  access_boundary_clarity REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE synthetic_vectors (
  item_id TEXT PRIMARY KEY,
  dimension_1 REAL NOT NULL,
  dimension_2 REAL NOT NULL,
  dimension_3 REAL NOT NULL,
  dimension_4 REAL NOT NULL,
  source TEXT NOT NULL,
  model_version TEXT NOT NULL
);

INSERT INTO embedding_system_cases VALUES
('Semantic article search','A knowledge library retrieves related articles by semantic similarity','Document embeddings with source metadata model version chunk references and hybrid keyword filters',0.86,0.82,0.88,0.78,0.86,0.90,0.80,0.78,0.84,0.86),
('Case similarity review','Institutional cases are compared to prior records for review support','Case embeddings with policy metadata decision provenance uncertainty flags and human review workflow',0.82,0.80,0.84,0.74,0.86,0.90,0.88,0.80,0.90,0.90),
('Content recommendation','Articles and reader behavior are represented as vectors for recommendation','Hybrid item and behavior embeddings with diversity controls freshness metadata and explanation snippets',0.82,0.78,0.82,0.72,0.78,0.82,0.86,0.82,0.80,0.84),
('Image-text retrieval','Images are retrieved using text queries and multimodal similarity','Multimodal embeddings with source image metadata prompt query logs model versioning and access controls',0.84,0.82,0.86,0.70,0.78,0.86,0.84,0.78,0.86,0.84);

INSERT INTO synthetic_vectors VALUES
('article-search',0.92,0.12,0.18,0.08,'synthetic','embedding-demo-v1'),
('document-index',0.84,0.20,0.24,0.10,'synthetic','embedding-demo-v1'),
('image-retrieval',0.20,0.86,0.22,0.18,'synthetic','embedding-demo-v1'),
('policy-review',0.36,0.18,0.82,0.34,'synthetic','embedding-demo-v1');
