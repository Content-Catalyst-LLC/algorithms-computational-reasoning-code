WITH ns(n) AS (
  VALUES (10.0), (100.0), (1000.0), (10000.0)
)
SELECT
  n,
  log(n) / log(2.0) AS log2_n,
  n * log(n) / log(2.0) AS n_log2_n,
  n * n AS quadratic
FROM ns
ORDER BY n;
