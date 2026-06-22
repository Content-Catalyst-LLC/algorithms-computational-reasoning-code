# Data Dictionary

## algorithmic_due_process_contexts.csv

- `case_id`: synthetic decision context.
- `domain`: operating domain.
- `stakes`: severity of consequence.
- `notice`: score for notice and awareness.
- `reasons`: score for decision-specific reasons.
- `evidence_access`: score for data and evidence access.
- `human_review`: score for review authority and independence.
- `correction_capacity`: score for correcting decisions and records.
- `remedy_capacity`: score for repairing consequences.
- `appeal_burden`: burden imposed on appellant.
- `resolution_days`: time to resolve appeal.

## contestability_appeals_audit.csv

- `contestability_score`: average of procedural safeguard scores.
- `procedural_risk_score`: stakes multiplied by weak contestability.
- `high_stakes`: 1 if stakes exceed threshold.
- `weak_contestability`: 1 if contestability score is too low.
- `high_burden`: 1 if appeal burden is high.
- `slow_resolution`: 1 if appeal resolution exceeds limit.
- `status`: pass, review, or escalate.

## due_process_governance_register.csv

- `item`: due-process governance item.
- `review_question`: question to answer before relying on contestability claims.
- `status`: requirement status.
