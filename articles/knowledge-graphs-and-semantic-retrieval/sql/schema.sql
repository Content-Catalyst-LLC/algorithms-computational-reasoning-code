DROP TABLE IF EXISTS graph_nodes;
CREATE TABLE graph_nodes (
  node_id INTEGER PRIMARY KEY,
  label TEXT NOT NULL UNIQUE,
  node_type TEXT NOT NULL
);

DROP TABLE IF EXISTS graph_edges;
CREATE TABLE graph_edges (
  edge_id INTEGER PRIMARY KEY,
  subject_label TEXT NOT NULL,
  predicate TEXT NOT NULL,
  object_label TEXT NOT NULL,
  source TEXT NOT NULL,
  confidence REAL NOT NULL,
  review_status TEXT NOT NULL
);

DROP TABLE IF EXISTS semantic_queries;
CREATE TABLE semantic_queries (
  query_id INTEGER PRIMARY KEY,
  query_text TEXT NOT NULL,
  target_entity TEXT NOT NULL,
  retrieval_goal TEXT NOT NULL
);

INSERT INTO graph_nodes(label,node_type) VALUES
('Information Retrieval','Concept'),
('Search Architecture','Concept'),
('Inverted Index','Concept'),
('Ranking Signals','Concept'),
('Relevance Models','Concept'),
('Knowledge Graphs','Concept'),
('Semantic Retrieval','Concept'),
('Entity Resolution','Concept'),
('Graph Traversal','Method'),
('Vector Retrieval','Method'),
('Ontology Governance','Governance'),
('Provenance','Evidence'),
('Traceability','Evidence'),
('Path Explanation','Explainability'),
('Linked Data','Standard'),
('RDF','Standard'),
('SPARQL','Standard');

INSERT INTO graph_edges(subject_label,predicate,object_label,source,confidence,review_status) VALUES
('Information Retrieval','related_to','Search Architecture','curated article map',0.94,'reviewed'),
('Search Architecture','uses','Inverted Index','article body',0.92,'reviewed'),
('Search Architecture','uses','Ranking Signals','article body',0.91,'reviewed'),
('Ranking Signals','related_to','Relevance Models','article body',0.95,'reviewed'),
('Knowledge Graphs','supports','Semantic Retrieval','article body',0.96,'reviewed'),
('Semantic Retrieval','uses','Entity Resolution','article body',0.91,'reviewed'),
('Semantic Retrieval','uses','Graph Traversal','article body',0.93,'reviewed'),
('Semantic Retrieval','uses','Vector Retrieval','article body',0.86,'reviewed'),
('Knowledge Graphs','requires','Ontology Governance','article body',0.88,'reviewed'),
('Knowledge Graphs','requires','Provenance','article body',0.92,'reviewed'),
('Provenance','supports','Traceability','article body',0.96,'reviewed'),
('Graph Traversal','supports','Path Explanation','article body',0.90,'reviewed'),
('Knowledge Graphs','related_to','Linked Data','article sequence',0.88,'planned'),
('Linked Data','uses','RDF','semantic web standard',0.94,'reviewed'),
('RDF','queried_by','SPARQL','semantic web standard',0.95,'reviewed');

INSERT INTO semantic_queries VALUES
(1,'semantic retrieval provenance','Semantic Retrieval','find evidence-backed retrieval concepts'),
(2,'knowledge graph standards','Knowledge Graphs','find standards and next concepts'),
(3,'path explanation graph retrieval','Graph Traversal','find explainability paths');
