# Data Dictionary

## explanation_cases.csv

- `case_id`: synthetic explanation artifact identifier.
- `audience`: intended audience for explanation.
- `faithfulness`: whether the explanation reflects actual system behavior.
- `stability`: whether similar cases receive similar explanations.
- `understandability`: whether the audience can understand the explanation.
- `actionability`: whether the explanation supports correction, review, or recourse.
- `uncertainty_communication`: whether confidence and limits are disclosed.
- `documentation_completeness`: completeness of model/data/evaluation/governance documentation.
- `contestability`: ability to challenge, correct, or appeal the outcome.
- `governance_readiness`: ownership, monitoring, escalation, and remediation readiness.
- `stakes`: consequence level.

## explanation_audit.csv

- `explanation_quality_score`: average of faithfulness, stability, understandability, actionability, and uncertainty communication.
- `transparency_capacity_score`: average of documentation completeness, governance readiness, and uncertainty communication.
- `accountability_capacity_score`: average of explanation quality, transparency capacity, contestability, and governance readiness.
- `explanation_risk_score`: stakes multiplied by weak accountability capacity.
- `status`: pass, review, or escalate.
