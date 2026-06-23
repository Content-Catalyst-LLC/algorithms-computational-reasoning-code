# Data Dictionary

## health_systems.csv

- `system_id`: synthetic health algorithmic system.
- `patient_impact`: consequence level for individual patients and clinical decisions.
- `population_impact`: consequence level for communities, surveillance, public health, or population intervention.
- `clinical_validation`: readiness of validation for intended population, setting, workflow, and use.
- `equity_readiness`: readiness of subgroup, access, proxy, missingness, and health-equity review.
- `privacy_readiness`: readiness of minimization, access control, security, and secondary-use governance.
- `human_review`: meaningful clinician or public-health review, override, escalation, and accountability.
- `workflow_integration`: fit with timing, burden, usability, actionability, and care pathway.
- `monitoring`: post-deployment monitoring of outcomes, errors, drift, overrides, alert fatigue, and harm.
- `governance`: inventory, ownership, documentation, approval, audit trails, and stop authority.

## health_algorithm_safety_audit.csv

- `impact_score`: average patient impact and population impact.
- `governance_readiness_score`: average validation, equity readiness, privacy readiness, human review, workflow integration, monitoring, and governance.
- `health_algorithm_risk_score`: average impact, weak validation, weak equity readiness, and weak governance readiness.
- `recommendation`: suggested governance stance.

## health_algorithm_summary.csv

- `systems_reviewed`: number of synthetic health algorithm systems.
- `systems_requiring_redesign`: systems requiring redesign before use.
- `systems_requiring_clinical_safety_review`: systems requiring clinical safety review.
- `systems_requiring_public_health_review`: systems requiring public-health governance review.
- `systems_requiring_equity_review`: systems requiring health-equity review.
