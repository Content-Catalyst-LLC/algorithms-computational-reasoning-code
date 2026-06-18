DROP TABLE IF EXISTS distributed_cases;
CREATE TABLE distributed_cases (
  case_name TEXT PRIMARY KEY,
  computational_goal TEXT NOT NULL,
  message_discipline REAL NOT NULL,
  failure_handling REAL NOT NULL,
  replication_strategy REAL NOT NULL,
  consistency_clarity REAL NOT NULL,
  observability REAL NOT NULL,
  security_trust REAL NOT NULL,
  provenance_support REAL NOT NULL
);

DROP TABLE IF EXISTS network_nodes;
CREATE TABLE network_nodes (
  node_id TEXT PRIMARY KEY,
  node_type TEXT NOT NULL,
  region TEXT NOT NULL,
  role TEXT NOT NULL,
  replica_group TEXT NOT NULL,
  availability REAL NOT NULL,
  trust_boundary TEXT NOT NULL
);

DROP TABLE IF EXISTS distributed_messages;
CREATE TABLE distributed_messages (
  message_id TEXT PRIMARY KEY,
  source_node TEXT NOT NULL,
  target_node TEXT NOT NULL,
  message_type TEXT NOT NULL,
  requires_ack INTEGER NOT NULL CHECK(requires_ack IN (0,1)),
  security_requirement TEXT NOT NULL,
  governance_note TEXT NOT NULL
);

INSERT INTO distributed_cases VALUES
('Distributed search index','serve search results with shard coverage ranking consistency and partial-failure disclosure',0.84,0.80,0.82,0.78,0.84,0.78,0.80),
('AI retrieval architecture','produce source-backed AI responses with traceable service paths and versioned retrieval evidence',0.78,0.72,0.74,0.68,0.76,0.74,0.82),
('Replicated database cluster','preserve availability and consistency guarantees under crash failures',0.86,0.86,0.90,0.88,0.82,0.80,0.76),
('Opaque microservice chain','compose operational decisions from networked services',0.38,0.30,0.34,0.24,0.22,0.42,0.18);

INSERT INTO network_nodes VALUES
('search_shard_a','search_shard','us-central','document partition A','search_index',0.995,'internal'),
('search_shard_b','search_shard','us-east','document partition B','search_index',0.993,'internal'),
('coordinator','service','us-central','query coordinator','search_frontend',0.997,'internal'),
('vector_store','vector_database','us-central','embedding retrieval','ai_retrieval',0.992,'internal'),
('document_store','database','us-east','source document records','ai_retrieval',0.991,'internal'),
('model_endpoint','model_service','us-west','generation endpoint','ai_retrieval',0.989,'external'),
('logger','observability','us-central','trace and provenance logs','observability',0.996,'internal');

INSERT INTO distributed_messages VALUES
('m001','coordinator','search_shard_a','query',1,'signed_request','trace query fanout'),
('m002','coordinator','search_shard_b','query',1,'signed_request','trace query fanout'),
('m003','search_shard_a','coordinator','response',1,'integrity_check','include shard version'),
('m004','search_shard_b','coordinator','response',1,'integrity_check','include shard version'),
('m005','coordinator','logger','event',0,'signed_event','record partial failures'),
('m006','vector_store','document_store','lookup',1,'access_control','preserve provenance'),
('m007','document_store','model_endpoint','context_payload',1,'encryption','do not expose restricted records'),
('m008','model_endpoint','logger','event',0,'signed_event','record generation version');
