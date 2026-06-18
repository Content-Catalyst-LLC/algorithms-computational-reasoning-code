.headers on
.mode column
SELECT case_name, database_role,
ROUND(100.0*(0.09*schema_clarity+0.08*relationship_modeling+0.08*constraint_discipline+0.08*query_expressiveness+0.07*indexing_strategy+0.08*transaction_reliability+0.08*metadata_quality+0.08*provenance_lineage+0.07*access_control+0.07*correction_workflow+0.06*retention_policy+0.06*interoperability+0.06*governance_readiness+0.04*communication_clarity),2) AS knowledge_system_score
FROM database_knowledge_cases
ORDER BY knowledge_system_score DESC;

SELECT a.slug, a.title
FROM research_library_articles a
LEFT JOIN research_library_repositories r ON a.article_id = r.article_id
WHERE r.repo_id IS NULL;
