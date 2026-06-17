DROP TABLE IF EXISTS graph_relationship_cases;
DROP TABLE IF EXISTS graph_edges;

CREATE TABLE graph_relationship_cases (
  case_name TEXT PRIMARY KEY,
  problem_context TEXT NOT NULL,
  graph_choice TEXT NOT NULL,
  edge_meaning_clarity REAL NOT NULL,
  node_definition_clarity REAL NOT NULL,
  direction_clarity REAL NOT NULL,
  weight_interpretability REAL NOT NULL,
  path_validity REAL NOT NULL,
  connectivity_evidence REAL NOT NULL,
  metadata_provenance REAL NOT NULL,
  algorithm_fit REAL NOT NULL,
  representation_risk_documentation REAL NOT NULL,
  governance_readiness REAL NOT NULL
);

CREATE TABLE graph_edges (
  source TEXT NOT NULL,
  target TEXT NOT NULL,
  relationship TEXT NOT NULL,
  weight REAL NOT NULL
);

INSERT INTO graph_relationship_cases VALUES
('Transportation route graph','Locations and roads are represented for route planning and congestion review','Directed weighted graph with travel-time weights closure metadata and route provenance',0.90,0.86,0.88,0.86,0.88,0.84,0.82,0.90,0.80,0.82),
('Software dependency graph','Packages modules and services depend on one another across a software system','Directed dependency graph with version metadata cycle checks and critical-path summaries',0.88,0.84,0.92,0.74,0.86,0.84,0.88,0.86,0.84,0.86),
('Knowledge graph','Concepts claims documents and sources are connected for semantic retrieval and explanation','Typed property graph with edge labels source citations confidence scores and contradiction handling',0.84,0.82,0.80,0.76,0.76,0.78,0.90,0.82,0.90,0.88),
('Institutional workflow network','Cases move through departments review states approvals exceptions and escalation paths','Directed workflow graph with state transitions role metadata queue timestamps and audit trails',0.82,0.84,0.86,0.72,0.84,0.80,0.88,0.80,0.90,0.92);

INSERT INTO graph_edges VALUES
('source','review','transitions_to',1.0),
('review','approval','transitions_to',1.0),
('review','escalation','transitions_to',1.5),
('approval','archive','transitions_to',1.0),
('escalation','archive','transitions_to',1.0),
('review','quality_check','requires',1.0),
('quality_check','approval','enables',1.0);
