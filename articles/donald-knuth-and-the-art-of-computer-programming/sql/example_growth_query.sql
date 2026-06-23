WITH sizes(n) AS (
  VALUES (10), (100), (1000), (10000)
)
SELECT
  n,
  log(n) / log(2) AS log2_n,
  n * log(n) / log(2) AS n_log2_n,
  n * n AS n_squared
FROM sizes;
