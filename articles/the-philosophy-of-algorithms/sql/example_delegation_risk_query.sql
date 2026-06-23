WITH delegation(case_id, decision_severity, automation_level, opacity) AS (
  VALUES ('low_risk_calculation', 0.20, 0.60, 0.20), ('decision_support_score', 0.70, 0.60, 0.50), ('automated_eligibility_decision', 0.95, 0.95, 0.80), ('agentic_tool_workflow', 0.85, 0.90, 0.85)
)
SELECT case_id, decision_severity * automation_level * opacity AS delegation_risk FROM delegation ORDER BY delegation_risk DESC;
