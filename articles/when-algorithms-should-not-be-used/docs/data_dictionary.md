# Data Dictionary

## candidate_use_cases.csv

- `use_case`: synthetic candidate algorithmic use case.
- `target_legitimacy`: whether the proposed prediction, score, ranking, or optimization target is appropriate.
- `data_legitimacy`: whether data are lawful, representative, documented, correctable, and appropriate.
- `contestability`: whether affected people can understand, challenge, correct, and appeal.
- `human_judgment`: whether the workflow preserves meaningful human judgment where needed.
- `governance_capacity`: whether the institution can monitor, audit, pause, rollback, and retire the system.
- `repairability`: whether harms can be detected, corrected, remedied, and prevented from recurring.
- `stakes`: consequence level.
- `irreversibility`: difficulty of undoing or repairing harm.
- `proxy_illegitimacy`: degree to which variables substitute for concepts they cannot responsibly measure.

## algorithmic_non_use_audit.csv

- `responsible_use_readiness_score`: average target legitimacy, data legitimacy, contestability, human judgment, governance capacity, and repairability.
- `non_use_pressure_score`: average stakes, irreversibility, governance weakness, and proxy illegitimacy.
- `recommendation`: allow with controls, limited support, support-only, human-led, or do not use.
- `status`: pass, review, or refuse.

## algorithmic_non_use_summary.csv

- `use_cases_reviewed`: number of use cases evaluated.
- `use_cases_passed`: use cases meeting review thresholds.
- `use_cases_requiring_review`: use cases requiring review.
- `use_cases_refused`: use cases refused.
- `mean_responsible_use_readiness_score`: average responsible-use readiness.
- `mean_non_use_pressure_score`: average non-use pressure.
