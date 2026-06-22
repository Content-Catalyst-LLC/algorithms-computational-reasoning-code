# Data Dictionary

## documentation_records.csv

- `system_id`: synthetic algorithmic system identifier.
- `required_fields`: number of required documentation fields.
- `completed_fields`: number of completed required fields.
- `accuracy`: whether documentation claims match evidence and system behavior.
- `specificity`: whether documentation uses concrete purposes, metrics, limits, and responsibilities.
- `timeliness`: whether documentation is current after changes.
- `accessibility`: whether documentation is understandable by intended audiences.
- `actionability`: whether documentation supports approve, use, audit, challenge, maintain, or retire decisions.
- `model_card`: whether a model card exists.
- `datasheet`: whether a datasheet exists.
- `risk_register`: whether a risk register exists.
- `change_log`: whether a change log exists.
- `appeal_documentation`: whether affected-person documentation exists.
- `stakes`: consequence level.

## documentation_audit.csv

- `documentation_completeness_score`: completed required fields divided by total required fields.
- `artifact_coverage_score`: model-card, datasheet, risk-register, change-log, and appeal-documentation coverage.
- `documentation_quality_score`: average of accuracy, completeness, specificity, timeliness, accessibility, and actionability.
- `documentation_risk_score`: stakes multiplied by weak documentation quality.
- `status`: pass, review, or escalate.

## documentation_audit_summary.csv

- `systems_reviewed`: number of systems evaluated.
- `systems_passed`: systems meeting review thresholds.
- `systems_requiring_review`: systems requiring review.
- `systems_escalated`: systems requiring escalation.
- `mean_documentation_completeness_score`: average completeness.
- `mean_documentation_quality_score`: average quality.
- `mean_artifact_coverage_score`: average artifact coverage.
- `mean_documentation_risk_score`: average documentation risk.
