DROP TABLE IF EXISTS graph_edges;
CREATE TABLE graph_edges (
  source TEXT,
  target TEXT,
  weight REAL,
  status TEXT,
  edge_type TEXT,
  risk_score REAL,
  notes TEXT
);

DROP TABLE IF EXISTS graph_search_cases;
CREATE TABLE graph_search_cases (
  case_name TEXT PRIMARY KEY,
  graph_definition REAL,
  node_edge_clarity REAL,
  weight_documentation REAL,
  constraint_documentation REAL,
  traversal_traceability REAL,
  alternative_path_reporting REAL,
  failure_handling REAL,
  update_freshness REAL,
  distributional_review REAL,
  governance_review REAL,
  communication_clarity REAL
);

INSERT INTO graph_edges VALUES
('A','B',2.0,'open','road',0.10,'low-cost link'),
('A','C',5.0,'open','road',0.20,'longer direct link'),
('B','C',1.0,'open','road',0.15,'connector'),
('B','D',4.0,'open','road',0.25,'moderate cost route'),
('C','D',1.5,'open','road',0.12,'short connector'),
('C','E',3.0,'open','road',0.18,'alternative destination path'),
('D','E',1.0,'open','road',0.08,'final low-cost link');

INSERT INTO graph_search_cases VALUES
('Road routing audit',0.86,0.84,0.78,0.76,0.82,0.74,0.76,0.72,0.62,0.70,0.78),
('Network packet routing',0.88,0.86,0.82,0.78,0.80,0.76,0.86,0.82,0.50,0.72,0.74),
('Knowledge graph retrieval',0.76,0.70,0.58,0.64,0.66,0.60,0.58,0.62,0.68,0.66,0.70),
('Opaque platform discovery path',0.42,0.34,0.20,0.26,0.24,0.18,0.30,0.46,0.24,0.28,0.36);
