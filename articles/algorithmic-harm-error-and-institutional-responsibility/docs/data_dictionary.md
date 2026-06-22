# Data Dictionary

## algorithmic_harm_contexts.csv

- `case_id`: synthetic harm context.
- `domain`: operating domain.
- `error_likelihood`: probability-like score for likely error.
- `severity`: consequence severity score.
- `exposure`: scale of exposure to the system.
- `contestability`: ability to challenge and correct outcomes.
- `ownership`: clarity of institutional ownership.
- `monitoring`: monitoring capacity.
- `appeals`: appeal and contestability capacity.
- `repair`: remediation and repair capacity.
- `governance`: governance maturity.

## harm_responsibility_audit.csv

- `harm_risk_score`: error likelihood × severity × exposure × weak contestability.
- `responsibility_capacity`: average of ownership, monitoring, appeals, repair, and governance.
- `remediation_gap`: positive gap between severity and repair capacity.
- `high_harm`: 1 if harm risk exceeds threshold.
- `low_responsibility`: 1 if responsibility capacity is low.
- `high_remediation_gap`: 1 if severity exceeds repair capacity by too much.
- `status`: pass, review, or escalate.

## algorithmic_incident_register.csv

- `field`: incident-reporting field.
- `purpose`: why the field matters.
- `required`: whether field is required for incident review.
