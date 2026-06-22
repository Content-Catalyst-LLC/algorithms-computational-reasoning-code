# Data Dictionary

## knowledge_objects.csv

- `object_id`: synthetic knowledge object or subsystem.
- `metadata_completeness`: required descriptive fields present and usable.
- `taxonomy_fit`: quality of category placement.
- `search_readiness`: readiness for indexing and retrieval.
- `link_quality`: quality and usefulness of internal links.
- `recommendation_quality`: quality of related-content or next-step recommendations.
- `provenance`: source, origin, review, and evidence records.
- `freshness`: update status and maintenance recency.
- `editorial_review`: human editorial review readiness.
- `representation_risk`: risk that categories, ranking, or recommendation misrepresent knowledge.

## knowledge_architecture_audit.csv

- `architecture_readiness_score`: average metadata, taxonomy, search, link, recommendation, provenance, and editorial review readiness.
- `maintenance_risk_score`: average weak metadata, weak links, weak freshness, and weak provenance.
- `governance_readiness_score`: average provenance, editorial review, metadata completeness, and freshness.
- `recommendation`: suggested governance stance.

## knowledge_architecture_summary.csv

- `objects_reviewed`: number of knowledge objects evaluated.
- `objects_ready`: objects ready for algorithmic discovery support.
- `objects_requiring_editorial_review`: objects requiring editorial governance review.
- `objects_requiring_metadata_or_link_review`: objects requiring metadata or linking remediation.
- `objects_requiring_rebuild`: objects requiring rebuild before algorithmic discovery.
