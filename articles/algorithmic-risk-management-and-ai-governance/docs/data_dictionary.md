# Data Dictionary

## risk_items.csv

- `risk_id`: synthetic risk identifier.
- `system`: synthetic algorithmic system identifier.
- `severity`: consequence level if the risk occurs.
- `likelihood`: estimated probability or frequency of the risk.
- `detectability`: ability to detect the risk before or during harm.
- `ownership`: named ownership and authority readiness.
- `documentation`: documentation and evidence readiness.
- `monitoring`: monitoring and signal readiness.
- `contestability`: appeal, challenge, and correction readiness.
- `remediation`: repair and recurrence-prevention readiness.
- `stop_authority`: authority to pause, rollback, or retire the system.
- `control_effectiveness`: estimated effectiveness of current controls.

## risk_governance_audit.csv

- `inherent_risk_score`: severity multiplied by likelihood and weak detectability.
- `governance_readiness_score`: average of ownership, documentation, monitoring, contestability, remediation, and stop authority.
- `residual_risk_score`: inherent risk after current controls.
- `status`: controlled, review, or escalate.

## risk_governance_summary.csv

- `risks_reviewed`: number of risks evaluated.
- `risks_controlled`: risks meeting review thresholds.
- `risks_requiring_review`: risks requiring review.
- `risks_escalated`: risks requiring escalation.
- `mean_inherent_risk_score`: average inherent risk.
- `mean_governance_readiness_score`: average governance readiness.
- `mean_residual_risk_score`: average residual risk.
