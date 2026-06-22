# Data Dictionary

## candidate_decisions.csv

- `decision_id`: synthetic decision-support use case.
- `predicted_probability`: estimated probability of relevant event or need.
- `benefit_if_act`: normalized benefit if action is taken.
- `cost_if_act`: normalized cost, burden, or risk of action.
- `loss_if_miss`: normalized loss if no action occurs and the event is real.
- `calibration`: readiness of probability estimates.
- `uncertainty_communication`: quality of uncertainty communication.
- `human_review`: meaningful human review readiness.
- `contestability`: ability to challenge, correct, and appeal outcomes.
- `governance`: documentation, monitoring, ownership, and stop authority readiness.
- `stakes`: consequence level.

## decision_science_audit.csv

- `expected_value_of_action`: estimated probability-weighted benefit minus action cost.
- `expected_loss_if_no_action`: estimated probability-weighted loss if action is not taken.
- `threshold_action`: whether predicted probability meets action threshold.
- `decision_support_readiness_score`: average calibration, uncertainty communication, human review, contestability, and governance.
- `recommendation`: suggested governance stance.

## decision_science_summary.csv

- `decisions_reviewed`: number of candidate decisions.
- `decisions_supporting_action`: decisions where support action with review is appropriate.
- `decisions_escalated`: decisions requiring human escalation.
- `decisions_not_automated`: decisions where action should not be automated.
- `mean_decision_support_readiness_score`: average readiness.
- `mean_expected_value_of_action`: average expected value.
- `mean_expected_loss_if_no_action`: average expected loss if no action.
