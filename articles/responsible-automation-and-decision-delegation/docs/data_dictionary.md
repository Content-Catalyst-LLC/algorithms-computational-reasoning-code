# Data Dictionary

## delegation_contexts.csv

- `context_id`: synthetic decision context identifier.
- `evidence_quality`: data, labels, features, and measurement adequacy.
- `validation`: context-specific testing and evaluation readiness.
- `reversibility`: ability to detect, correct, remedy, and prevent recurrence.
- `contestability`: notice, reasons, appeal, and correction readiness.
- `governance`: ownership, monitoring, escalation, rollback, and retirement readiness.
- `human_review`: meaningful review capacity.
- `automated_final_actions`: number of final actions taken automatically.
- `total_decisions`: total decisions in the workflow.
- `stakes`: consequence level.

## delegation_readiness_audit.csv

- `delegation_readiness_score`: average of evidence quality, validation, reversibility, contestability, governance, and human review.
- `automation_reliance_score`: automated final actions divided by total decisions.
- `delegation_risk_score`: stakes multiplied by weak delegation readiness.
- `recommendation`: suggested delegation mode or control response.
- `status`: pass, review, or escalate.

## delegation_audit_summary.csv

- `contexts_reviewed`: number of contexts evaluated.
- `contexts_passed`: contexts meeting review thresholds.
- `contexts_requiring_review`: contexts requiring review.
- `contexts_escalated`: contexts requiring escalation.
- `mean_delegation_readiness_score`: average readiness.
- `mean_delegation_risk_score`: average risk.
- `mean_automation_reliance_score`: average automation reliance.
