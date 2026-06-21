-- Actions that should be blocked before deployment.
SELECT step, task, tool, approval_violation, status
FROM agent_tool_use_audit
WHERE approval_violation = 1 OR status = 'blocked';

-- High-risk tools requiring explicit review.
SELECT tool, action_type, risk, approval_required, permission_scope
FROM agent_tool_registry
WHERE risk >= 0.65
ORDER BY risk DESC;

-- Untrusted instruction sources that triggered escalation.
SELECT step, task, tool, instruction_source, status
FROM agent_tool_use_audit
WHERE untrusted_instruction = 1;

-- Actions exceeding autonomous step limits.
SELECT step, task, tool, step_limit_violation, status
FROM agent_tool_use_audit
WHERE step_limit_violation = 1;
