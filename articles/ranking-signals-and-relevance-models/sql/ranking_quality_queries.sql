.headers on
.mode column

-- Simple metadata/authority ranking example
SELECT doc_id, title, source_authority, metadata_completeness,
       ROUND(100.0 * (0.55 * source_authority + 0.45 * metadata_completeness), 2) AS metadata_authority_score
FROM ranking_documents
ORDER BY metadata_authority_score DESC;

-- Relevance judgment summary
SELECT query_text, doc_id, relevance_grade
FROM relevance_judgments
ORDER BY query_text, relevance_grade DESC;

-- Click and rank position review
SELECT query_text,
       AVG(rank_position) AS average_rank_position,
       SUM(clicked) AS clicks,
       COUNT(*) AS impressions
FROM ranking_events
GROUP BY query_text
ORDER BY query_text;

-- Potential position bias evidence
SELECT rank_position, COUNT(*) AS impressions, SUM(clicked) AS clicks
FROM ranking_events
GROUP BY rank_position
ORDER BY rank_position;
