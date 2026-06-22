# Data Dictionary

## failure_modes.csv

- `failure_id`: synthetic failure-mode identifier.
- `category`: failure layer such as data, model, objective, workflow, governance, or infrastructure.
- `likelihood`: probability-like score for expected failure occurrence.
- `severity`: consequence severity score.
- `detectability`: ability to detect the failure before harm grows.
- `controllability`: ability to contain or control the failure.
- `monitoring`: monitoring capacity.
- `fallback`: safe fallback capacity.
- `rollback`: ability to reverse unsafe change.
- `escalation`: ability to route severe failure to accountable owners.
- `repair`: ability to correct affected outcomes and source conditions.

## failure_mode_audit.csv

- `failure_risk_score`: likelihood × severity × weak detectability × weak controllability.
- `priority_score`: likelihood × severity × weak detectability.
- `resilience_capacity`: average of monitoring, fallback, rollback, escalation, and repair.
- `status`: pass, review, or escalate.
