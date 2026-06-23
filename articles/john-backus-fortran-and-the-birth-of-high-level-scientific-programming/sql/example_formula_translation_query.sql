WITH xs(x) AS (
  VALUES (-2.0), (-1.0), (0.0), (1.0), (2.0), (3.0)
)
SELECT
  x,
  2.0*x*x - 3.0*x + 1.0 AS y
FROM xs
ORDER BY x;
