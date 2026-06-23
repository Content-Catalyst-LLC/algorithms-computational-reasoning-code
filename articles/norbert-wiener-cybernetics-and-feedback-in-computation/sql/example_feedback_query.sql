WITH RECURSIVE feedback(t, state, target, gain) AS (
  VALUES (0, 10.0, 0.0, 0.2)
  UNION ALL
  SELECT
    t + 1,
    state - gain * (state - target),
    target,
    gain
  FROM feedback
  WHERE t < 5
)
SELECT t, state
FROM feedback
ORDER BY t;
