.headers on
.mode column

-- Direct semantic neighborhood
SELECT subject_label, predicate, object_label, confidence, review_status
FROM graph_edges
WHERE subject_label = 'Knowledge Graphs'
ORDER BY confidence DESC;

-- Provenance-backed relationships
SELECT subject_label, predicate, object_label, source, confidence
FROM graph_edges
WHERE review_status = 'reviewed' AND confidence >= 0.90
ORDER BY confidence DESC;

-- Relationship type inventory
SELECT predicate, COUNT(*) AS edge_count, ROUND(AVG(confidence), 3) AS avg_confidence
FROM graph_edges
GROUP BY predicate
ORDER BY edge_count DESC, avg_confidence DESC;

-- Semantic query to candidate edge matching
SELECT q.query_text, e.subject_label, e.predicate, e.object_label, e.confidence
FROM semantic_queries q
JOIN graph_edges e
  ON e.subject_label = q.target_entity OR e.object_label = q.target_entity
ORDER BY q.query_id, e.confidence DESC;
