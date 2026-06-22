# Data Dictionary

## human_review_contexts.csv

- `context_id`: synthetic human review workflow identifier.
- `time`: reviewer time and workload capacity.
- `information`: access to inputs, reasons, uncertainty, and context.
- `authority`: practical ability to override, pause, or escalate.
- `training`: preparation on system limits, uncertainty, errors, bias, and appeals.
- `protection`: institutional support for justified disagreement.
- `accepted_recommendations`: count of accepted algorithmic recommendations.
- `total_recommendations`: count of recommendations presented.
- `overrides`: count of human overrides.
- `reviewed_cases`: count of cases reviewed.
- `escalation_capacity`: ability to move uncertain or high-risk cases upward.
- `contestability`: ability for affected people to challenge and correct outcomes.
- `governance`: ownership, documentation, and remediation readiness.
- `stakes`: consequence level.

## human_review_audit.csv

- `review_capacity_score`: average of time, information, authority, training, and protection.
- `reliance_score`: accepted recommendations divided by total recommendations.
- `override_rate`: overrides divided by reviewed cases.
- `judgment_capacity_score`: average of review capacity, escalation, contestability, and governance.
- `review_risk_score`: stakes multiplied by weak judgment capacity.
- `status`: pass, review, or escalate.

## human_review_audit_summary.csv

- `contexts_reviewed`: number of workflows evaluated.
- `contexts_passed`: workflows meeting review thresholds.
- `contexts_requiring_review`: workflows requiring review.
- `contexts_escalated`: workflows requiring escalation.
- `mean_review_capacity_score`: average review capacity.
- `mean_reliance_score`: average automation reliance.
- `mean_override_rate`: average override rate.
- `mean_judgment_capacity_score`: average judgment capacity.
- `mean_review_risk_score`: average review risk.
