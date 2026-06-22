WITH object(object_id, metadata_completeness, taxonomy_fit, search_readiness, link_quality, recommendation_quality, provenance, freshness, editorial_review, representation_risk) AS (
  VALUES ('article_map_algorithms', 0.92, 0.88, 0.86, 0.90, 0.82, 0.86, 0.84, 0.90, 0.28)
)
SELECT
  object_id,
  (metadata_completeness + taxonomy_fit + search_readiness + link_quality + recommendation_quality + provenance + editorial_review) / 7.0 AS architecture_readiness_score,
  ((1.0 - metadata_completeness) + (1.0 - link_quality) + (1.0 - freshness) + (1.0 - provenance)) / 4.0 AS maintenance_risk_score,
  (provenance + editorial_review + metadata_completeness + freshness) / 4.0 AS governance_readiness_score
FROM object;
