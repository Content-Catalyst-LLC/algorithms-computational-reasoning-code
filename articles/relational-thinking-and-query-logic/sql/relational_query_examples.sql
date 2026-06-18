.headers on
.mode column

-- Selection and projection
SELECT slug, title
FROM articles
WHERE publication_status = 'published';

-- Inner join: articles with references
SELECT a.slug, r.citation
FROM articles a
JOIN references_table r ON a.article_id = r.article_id
ORDER BY a.slug, r.citation;

-- Anti-join: articles without references
SELECT a.slug, a.title
FROM articles a
LEFT JOIN references_table r ON a.article_id = r.article_id
WHERE r.reference_id IS NULL;

-- Anti-join: articles without repositories
SELECT a.slug, a.title
FROM articles a
LEFT JOIN repositories repo ON a.article_id = repo.article_id
WHERE repo.repo_id IS NULL;

-- Aggregation
SELECT series, publication_status, COUNT(*) AS article_count
FROM articles
GROUP BY series, publication_status
ORDER BY series, publication_status;

-- Audit relation
SELECT a.slug, e.action, e.event_time
FROM articles a
JOIN audit_events e ON a.article_id = e.article_id
ORDER BY e.event_time;
