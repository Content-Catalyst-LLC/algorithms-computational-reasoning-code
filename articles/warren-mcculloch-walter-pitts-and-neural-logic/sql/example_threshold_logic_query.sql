WITH examples(gate, x1, x2, threshold) AS (
  VALUES
    ('AND', 0, 0, 2),
    ('AND', 1, 1, 2),
    ('OR', 1, 0, 1),
    ('OR', 0, 0, 1)
)
SELECT
  gate,
  x1,
  x2,
  threshold,
  CASE WHEN x1 + x2 >= threshold THEN 1 ELSE 0 END AS output
FROM examples
ORDER BY gate, x1, x2;
