# Data Dictionary

## public_algorithm_use_cases.csv

- `use_case_id`: synthetic public-sector algorithmic use case.
- `rights_impact`: consequence level for rights, access, benefits, burdens, or enforcement.
- `due_process`: readiness of notice, reasons, correction, appeal, and remedy.
- `transparency`: clarity of purpose, decision role, reasons, documentation, and public reporting.
- `human_review`: meaningful review authority, time, evidence, and override capacity.
- `data_quality`: quality, relevance, lawfulness, and correction-readiness of administrative data.
- `vendor_accountability`: documentation, audit rights, update controls, and exit options.
- `appeal_readiness`: ability of affected people to challenge and correct outcomes.
- `monitoring`: post-deployment monitoring of performance, errors, drift, reliance, appeals, and harm.
- `public_value`: whether system serves legitimate public purpose.

## public_governance_audit.csv

- `procedural_readiness_score`: average due process, transparency, human review, and appeal readiness.
- `governance_readiness_score`: average data quality, vendor accountability, monitoring, and procedural readiness.
- `public_algorithmic_risk_score`: rights impact multiplied by weak governance readiness.
- `recommendation`: deployment or governance stance.

## public_governance_summary.csv

- `use_cases_reviewed`: number of public algorithmic use cases.
- `use_cases_not_ready_for_deployment`: systems that should not deploy without due-process redesign.
- `use_cases_requiring_governance_review`: systems requiring governance remediation.
- `use_cases_requiring_independent_oversight`: high-impact systems requiring independent oversight.
