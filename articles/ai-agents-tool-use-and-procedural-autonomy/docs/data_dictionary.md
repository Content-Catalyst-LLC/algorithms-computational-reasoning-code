# Data Dictionary

## agent_tool_registry.csv

- `tool`: tool name.
- `action_type`: read, compute, execute, draft, write, or external_write.
- `risk`: synthetic risk score from 0 to 1.
- `approval_required`: 1 if human approval is required.

## agent_planned_actions.csv

- `step`: workflow step.
- `task`: task label.
- `tool`: selected tool.
- `approved`: 1 if approval was granted.
- `observation_quality`: synthetic quality score for returned observation.

## agent_tool_use_audit.csv

- `approval_violation`: 1 when approval was required but missing.
- `step_limit_violation`: 1 when autonomy exceeds allowed steps.
- `escalation_required`: 1 when risk, approval, or step rules require review.
- `status`: pass, escalate, or blocked.

## agent_autonomy_profile.csv

- `autonomy_recommendation`: recommended level such as supervised_action or bounded_automation.
