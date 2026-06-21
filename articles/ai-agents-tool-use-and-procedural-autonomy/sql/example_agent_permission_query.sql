WITH action(tool, risk, approval_required, approved) AS (
  VALUES ('email_send', 0.85, 1, 0)
)
SELECT
  tool,
  CASE
    WHEN approval_required = 1 AND approved = 0 THEN 'blocked'
    WHEN risk >= 0.65 THEN 'escalate'
    ELSE 'pass'
  END AS status
FROM action;
