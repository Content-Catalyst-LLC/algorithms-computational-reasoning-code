# Data Dictionary

## platform_systems.csv

- `system_id`: synthetic media-platform or attention-system use case.
- `engagement_pressure`: degree to which the system optimizes sustained attention or interaction.
- `transparency`: clarity of objectives, rules, notices, and explanations.
- `contestability`: ability to challenge ranking, moderation, monetization, or recommendation decisions.
- `moderation_readiness`: quality of content-safety workflows, human review, and threshold governance.
- `creator_impact`: consequence level for creators, publishers, channels, or platform labor.
- `public_knowledge_impact`: consequence level for news, information, civic discourse, or public understanding.
- `user_control`: degree of meaningful control over feed, recommendations, notifications, and personalization.
- `governance`: readiness of policies, ownership, review, and accountability.
- `monitoring`: ability to track harm, drift, virality, manipulation, and metric gaming.

## attention_system_audit.csv

- `governance_readiness_score`: average transparency, contestability, moderation readiness, user control, governance, and monitoring.
- `attention_risk_score`: average engagement pressure, creator impact, public knowledge impact, weak user control, and weak contestability.
- `platform_risk_score`: attention risk multiplied by weak governance readiness.
- `recommendation`: suggested governance stance.

## attention_system_summary.csv

- `systems_reviewed`: number of synthetic platform systems reviewed.
- `systems_requiring_redesign`: systems requiring redesign before scaling.
- `systems_requiring_public_interest_review`: systems requiring independent public-interest review.
- `systems_requiring_governance_review`: systems requiring governance remediation.
