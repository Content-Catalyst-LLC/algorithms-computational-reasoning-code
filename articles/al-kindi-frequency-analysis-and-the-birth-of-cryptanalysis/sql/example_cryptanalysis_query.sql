WITH sample(symbol, count) AS (
  VALUES ('e', 8), ('t', 6), ('a', 5), ('x', 2)
),
total(n) AS (
  SELECT SUM(count) FROM sample
)
SELECT
  symbol,
  count,
  CAST(count AS REAL) / total.n AS relative_frequency,
  RANK() OVER (ORDER BY count DESC) AS rank
FROM sample, total
ORDER BY rank;
