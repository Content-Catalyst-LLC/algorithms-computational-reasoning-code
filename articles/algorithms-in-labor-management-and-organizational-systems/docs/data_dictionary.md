# Data Dictionary

## workplace_systems.csv

- `system_id`: synthetic workplace algorithmic system.
- `worker_impact`: consequence level for workers, applicants, pay, schedule, discipline, opportunity, safety, or dignity.
- `managerial_impact`: consequence level for managerial decision-making, organizational control, or operational coordination.
- `fairness_readiness`: readiness of subgroup, access, rating-bias, promotion, workload, and opportunity review.
- `privacy_readiness`: readiness of data minimization, monitoring limits, retention, vendor access, and secondary-use controls.
- `contestability`: readiness of notice, explanation, correction, human review, appeal, and remedy.
- `safety_readiness`: readiness of fatigue, workload, pace, ergonomic, hazard, and incident-learning review.
- `human_review`: meaningful manager review, override, worker voice, and contextual evaluation.
- `monitoring`: post-deployment monitoring of bias, burden, privacy incidents, safety risks, and metric distortion.
- `governance`: inventory, ownership, documentation, audit trails, procurement review, and stop authority.

## workplace_algorithm_governance_audit.csv

- `impact_score`: average worker impact and managerial impact.
- `governance_readiness_score`: average fairness readiness, privacy readiness, contestability, safety readiness, human review, monitoring, and governance.
- `workplace_algorithm_risk_score`: average impact score, weak fairness, weak privacy, weak contestability, and weak governance readiness.
- `recommendation`: suggested governance stance.

## workplace_algorithm_summary.csv

- `systems_reviewed`: number of synthetic workplace systems reviewed.
- `systems_requiring_redesign`: systems requiring redesign before workplace use.
- `systems_requiring_contestability_review`: systems requiring contestability and appeal review.
- `systems_requiring_worker_impact_review`: systems requiring worker-impact review.
- `systems_requiring_privacy_review`: systems requiring workplace privacy review.
- `systems_requiring_equity_review`: systems requiring workplace equity review.
