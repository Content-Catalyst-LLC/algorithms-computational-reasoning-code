.headers on
.mode column

-- Basic lexical retrieval over title, body, and tags
SELECT doc_id, title, category, tags
FROM search_documents
WHERE lower(title || ' ' || body || ' ' || tags) LIKE '%search%'
ORDER BY title;

-- Zero-result query audit
SELECT query_text, COUNT(*) AS events
FROM search_logs
WHERE zero_result = 1
GROUP BY query_text;

-- Query click summary
SELECT query_text, COUNT(*) AS query_events, SUM(CASE WHEN clicked_doc_id IS NOT NULL THEN 1 ELSE 0 END) AS click_events
FROM search_logs
GROUP BY query_text
ORDER BY query_events DESC;

-- Relevance judgment summary
SELECT query_text, AVG(relevance_grade) AS avg_relevance, COUNT(*) AS judged_docs
FROM relevance_judgments
GROUP BY query_text
ORDER BY avg_relevance DESC;
