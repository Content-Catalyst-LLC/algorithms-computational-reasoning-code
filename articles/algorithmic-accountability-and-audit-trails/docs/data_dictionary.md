# Data Dictionary

## accountability_system_records.csv

- `system_id`: synthetic algorithmic system identifier.
- `required_records`: number of required audit records.
- `available_records`: number of available records.
- `documentation`: documentation completeness score.
- `provenance`: data/model provenance score.
- `reviewability`: ability to reconstruct and inspect decisions.
- `contestability`: ability to challenge and correct outcomes.
- `remediation`: ability to repair harm and prevent recurrence.
- `governance`: ownership, escalation, and control readiness.
- `stakes`: consequence level.

## accountability_audit.csv

- `audit_completeness_score`: available required records divided by required records.
- `accountability_capacity_score`: average of documentation, provenance, reviewability, contestability, remediation, and governance.
- `reconstruction_risk_score`: stakes multiplied by weak audit completeness.
- `status`: pass, review, or escalate.

## accountability_audit_summary.csv

- `systems_reviewed`: number of systems evaluated.
- `systems_passed`: systems meeting review thresholds.
- `systems_requiring_review`: systems requiring review.
- `systems_escalated`: systems requiring escalation.
- `mean_audit_completeness_score`: average audit completeness.
- `mean_accountability_capacity_score`: average accountability capacity.
- `mean_reconstruction_risk_score`: average reconstruction risk.
