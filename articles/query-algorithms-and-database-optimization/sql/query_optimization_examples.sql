.headers on
.mode column
SELECT slug,title FROM articles WHERE publication_status='published' AND publication_year=2026;
SELECT a.slug,r.citation FROM articles a JOIN references_table r ON a.article_id=r.article_id WHERE a.publication_status='published' ORDER BY a.slug,r.citation;
SELECT a.slug,a.title FROM articles a LEFT JOIN repositories repo ON a.article_id=repo.article_id WHERE repo.repo_id IS NULL;
SELECT publication_status,COUNT(*) AS article_count FROM articles GROUP BY publication_status ORDER BY publication_status;
SELECT query_name,baseline_ms,optimized_ms,ROUND(100.0*(baseline_ms-optimized_ms)/baseline_ms,2) AS improvement_percent,plan_note FROM query_benchmarks ORDER BY improvement_percent DESC;
