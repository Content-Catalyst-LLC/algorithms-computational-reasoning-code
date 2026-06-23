# Data Dictionary

## learning_systems.csv

- `system_id`: synthetic education or learning algorithmic system.
- `learner_impact`: consequence level for individual learners, support, placement, assessment, opportunity, or dignity.
- `instructional_impact`: consequence level for teaching, curriculum, assessment, feedback, or institutional instruction.
- `equity_readiness`: readiness of access, subgroup, tracking-risk, digital-divide, and opportunity review.
- `privacy_readiness`: readiness of data minimization, retention, secondary-use control, vendor review, security, and notice.
- `pedagogical_validity`: readiness of learning-goal, assessment-validity, feedback-quality, and instructional-purpose review.
- `human_review`: meaningful teacher, advisor, student, or institutional review, override, explanation, and contestability.
- `accessibility_readiness`: readiness of accessibility, accommodation, alternative formats, and inclusive design.
- `monitoring`: post-deployment monitoring of learning quality, burden, bias, privacy incidents, and unintended consequences.
- `governance`: inventory, ownership, documentation, audit trails, procurement review, and stop authority.

## learning_system_governance_audit.csv

- `impact_score`: average learner impact and instructional impact.
- `governance_readiness_score`: average equity readiness, privacy readiness, pedagogical validity, human review, accessibility readiness, monitoring, and governance.
- `learning_system_risk_score`: average impact score, weak equity readiness, weak pedagogical validity, and weak governance readiness.
- `recommendation`: suggested governance stance.

## learning_system_summary.csv

- `systems_reviewed`: number of synthetic learning systems reviewed.
- `systems_requiring_redesign`: systems requiring redesign before educational use.
- `systems_requiring_pedagogical_review`: systems requiring pedagogical-validity review.
- `systems_requiring_student_impact_review`: systems requiring student-impact review.
- `systems_requiring_equity_review`: systems requiring educational-equity review.
- `systems_requiring_privacy_review`: systems requiring student-privacy review.
